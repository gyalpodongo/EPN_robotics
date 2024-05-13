pip install virtualenv
python -m venv venv
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

