
import socket
from contextlib import contextmanager
import findspark

class DatasakuSparkIceberg:

    def __init__(self
                 , spark_home:str
                 , minio_username:str
                 , minio_password:str
                 , spark_master_uri:str="spark://spark-master.spark-dev.svc.cluster.local:7077"
                 , minio_endpoint_uri:str="http://minio-service.minio-dev.svc.cluster.local:6544"
                 , nessie_catalog_uri:str="http://nessie-service.nessie-dev.svc.cluster.local:6788/api/v1"
                ):
        findspark.init(spark_home=spark_home)
        import pyspark

        self.spark_master_uri = spark_master_uri
        self.minio_endpoint_uri = minio_endpoint_uri
        self.minio_username = minio_username
        self.minio_password = minio_password
        self.nessie_catalog_uri = nessie_catalog_uri
        self.spark_conf = pyspark.SparkConf().setAll([
            # ip of current notebook
            ('spark.driver.host', socket.gethostbyname(socket.gethostname()))
            , ('spark.master', self.spark_master_uri)
            , ("spark.sql.extensions"
                   , """org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
                    , org.projectnessie.spark.extensions.NessieSparkSessionExtensions
                    """
              )
            # for minio spark
            , ('spark.hadoop.fs.s3a.endpoint', self.minio_endpoint_uri)
            , ('spark.hadoop.fs.s3a.access.key','minio')
            , ('spark.hadoop.fs.s3a.secret.key', 'minio123')
            , ('spark.hadoop.fs.s3a.path.style.access', 'true')
            , ("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
            # nessie catalog
            , ('spark.sql.catalog.nessie_catalog', 'org.apache.iceberg.spark.SparkCatalog')
            , ("spark.sql.catalog.nessie_catalog.catalog-impl", "org.apache.iceberg.nessie.NessieCatalog")
            , ('spark.sql.defaultCatalog', 'nessie_catalog')
            , ('spark.sql.catalog.nessie_catalog.warehouse', 's3a://iceberg/')
            # ip of service postgre
            , ('spark.sql.catalog.nessie_catalog.uri', self.nessie_catalog_uri)
            , ('spark.sql.catalog.nessie_catalog.ref', 'main')
            , ("spark.sql.catalog.nessie_catalog.authentication.type", 'NONE')
            ])
        # self.spark_context = pyspark.SparkContext(conf=conf)
        # self.spark = SparkSession.builder.config(conf=conf).getOrCreate()

    @contextmanager
    def spark_session(self):
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.config(conf=self.spark_conf).getOrCreate()
        try:
            yield spark
        finally:
            spark.stop()
        