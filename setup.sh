python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
gdown --id 1xRoYjz2KCwkyIPf21E-WKIZkjLYabPgJ -O EvenAlignedModelNet40PC.tar.gz
tar -xzvf EvenAlignedModelNet40PC.tar.gz
gdown --id 1rnJP3Q2zvcj5uImxRu8yYwgk0O7md8dJ 3dsgrasp_ycb_train_test_split.zip
unzip 3dsgrasp_ycb_train_test_split.zip
python createYCB40.py

cd vgtk
python setup.py install
cd ..
echo "INSTALLATION FINISHED. ACTIVATE VIRTUAL ENVIRONMENT FOR FUTURE TIMES YOU USE THIS REPO. THERE MAY BE SOME ISSUES WITH np.bool or np.float in the packages when running training or evaluation. Follow python recommendation by changing these instances to bool and float to make everything work."

#install vgtk

#print into terminal that we may have to fix manually some np.bool stuff as well as np.float when running training and evaluation

