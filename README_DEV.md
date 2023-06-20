# Instalation

Since the package will consist of geo related package so installing gdal is necessary (be patient, takes time)
```
brew install gdal
```
Install the datasaku package
```
pip install /path/to/project --upgrade --upgrade-strategy eager
```

# Import the library

```
import importlib
import datasaku
importlib.reload(datasaku)
```

# How to update the wheels

Install pipreqs
```
pip install pipreqs
```
Inside the project folder, run this command
```
pipreqs /path/to/project --force
```
Create the distribution file
```
pip install build
python -m build
```

# Upload the project
Follow this link to upload the project 
https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives

Install twine
```
pip install twine
```

Upload to testpypi
```
python -m twine upload --repository testpypi dist/*
```
Upload to pypi
```
python -m twine upload --repository pypi dist/*
```

# Versioning Guideline

X1.X2.X3

X1 = major update  
X2 = minor update  
X3 = very small improvement   