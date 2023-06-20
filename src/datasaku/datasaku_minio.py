"""package for minio operations"""

from minio import Minio
import pandas as pd
import io

class ConnMinio:
    """Class for Minio"""
    def __init__(self, minio_host, minio_access_key, minio_secret_key):
        self.minio_access = minio_access_key
        self.minio_secret = minio_secret_key
        self.minio_host = minio_host

        self.minio_client = Minio(
                    self.minio_host,
                    access_key=self.minio_access,
                    secret_key=self.minio_secret,
                    secure=False
                    )
        
    def minio_list_bucket(self):
        """list bucket inside minio"""
        minio_client = self.minio_client # create minio client
        buckets = minio_client.list_buckets()
        buckets = [bucket.name for bucket in buckets]
        return buckets
    
    def minio_list_all_file_folder(self, minio_bucket_def):
        """list files inside bucket minio"""
        minio_client = self.minio_client # create minio client
        objects = minio_client.list_objects(minio_bucket_def, recursive=True)
        objects = [obj.object_name for obj in objects]
        return objects
    
    def minio_list_all_file_folder(self, minio_bucket_def, minio_prefix_def):
        """list files inside bucket minio"""
        minio_client = self.minio_client # create minio client
        objects = minio_client.list_objects(minio_bucket_def, prefix = minio_prefix_def)
        objects = [obj.object_name for obj in objects]
        return objects
    
    def minio_upload_file(self, minio_bucket_def, minio_prefix_def, df_def, file_def):
        minio_client = self.minio_client # create minio client

        filetype = file_def.split('.', 1)[1]
        # filename = file_def.split('.', 1)[0]
        
        if filetype == 'parquet':
            bytes_data = df_def.to_parquet()
        elif filetype == 'csv':
            bytes_data = df_def.to_csv().encode('utf-8')
        buffer = io.BytesIO(bytes_data)

        minio_client.put_object(minio_bucket_def,
                                    minio_prefix_def+file_def,
                                    data=buffer,
                                    length=len(bytes_data),
                                    content_type='application/{}'.format(filetype)
                                )