#!/bin/bash
<<COMMENT
This script sets up the environment and downloads the necessary datasets for the project.

It performs the following steps:
1. Creates a virtual environment named 'venv'
2. Activates the virtual environment
3. Installs the dependencies listed in the 'requirements.txt' file
4. Installs the 'vgtk' package
5. Downloads and extracts the 'EvenAlignedModelNet40PC' dataset
6. Downloads and extracts the '3dsgrasp_ycb_train_test_split' dataset
7. Creates the 'YCB40' dataset by running the 'createYCB40.py' script

After running this script, the environment will be set up and the required datasets will be available.
To use the environment in the future, activate the virtual environment using 'source venv/bin/activate'.

If your system uses python3/pip3 instead of python/pip in terminal, make sure to change this respective within this bash file.
COMMENT

pip3 install virtualenv
python3 -m venv venv
echo "ENVIRONMENT CREATED: use source venv/bin/activate for future activations" 
source venv/bin/activate
echo "INSTALLING DEPENDENCIES"
pip install -r requirements.txt
echo "DEPENDENCIES INSTALLED"
echo "INSTALLING vgtk"
cd vgtk
python setup.py install
cd ..
echo "vgtk INSTALLED"

echo "DOWNLOADING DATASETS"
gdown --id 1xRoYjz2KCwkyIPf21E-WKIZkjLYabPgJ -O EvenAlignedModelNet40PC.tar.gz
tar -xzvf EvenAlignedModelNet40PC.tar.gz
gdown --id 1rnJP3Q2zvcj5uImxRu8yYwgk0O7md8dJ -O 3dsgrasp_ycb_train_test_split.zip
unzip -o 3dsgrasp_ycb_train_test_split.zip -d 3dsgrasp_ycb_train_test_split/
unzip 3dsgrasp_ycb_train_test_split/gt.zip
unzip 3dsgrasp_ycb_train_test_split/input.zip

echo "CREATING YCB40"
python createYCB40.py

echo "INSTALLATION FINISHED. ACTIVATE VIRTUAL ENVIRONMENT FOR FUTURE TIMES YOU USE THIS REPO."

