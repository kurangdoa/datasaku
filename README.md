# datasaku Readme

The package contains several function to make analysis easier. Several function included in the packages are:
- **datasaku.calendar** = Calendar operation in pandas.
- **datasaku.geo** = Manipulation of geolocation data based on geopandas.
- **datasaku.google** = Connection to google environment such as google sheets.
- **datasaku.nlp** = NLP related module such as fuzzy matching.
- **datasaku.pandas** = Function related to pandas.
- **datasaku.presto** = Connection to Presto.
- **datasaku.s3** = API connection to S3.
- **datasaku.snowflake** = Function to make connection to Snowflake.
- **datasaku.starburst** = Function to do operation in Starburst.
- **datasaku.viz** = Function to do advance visualization such as sankey.

There are pre-requisite to connect to google as described here:

(wip)

# Instalation

Since the package will consist of geo related package so installing gdal is necessary (be patient, takes time)
```
brew install gdal
```
Install the datasaku package using pip
```
pip install --upgrade --force-reinstall datasaku
```