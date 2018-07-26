# ml

## Install Tensorflow
1. sudo apt-get install python3-pip python3-dev python-virtualenv 
2. virtualenv --system-site-packages -p python3 targetDirectory 
3. source ~/targetDirectory/bin/activate
4. (tensorflow)$
5. (tensorflow)$ easy_install -U pip
6. (tensorflow)$ pip3 install --upgrade tensorflow-gpu
7. (tensorflow)$ pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.9.0-py3-none-any.whl 

## Install Keras 
7. pip install keras

## Install Notebook
8. python3 -m pip install jupyter
9. jupyter notebook


## Docker Version
1. docker pull jupyter/tensorflow-notebook
2. docker run --name tensorflow -d -p 8888:8888 jupyter/tensorflow-notebook
