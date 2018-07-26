# ml
## mac

###Install & Update Homebrew
1. /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
2. brew update
3. brew tap brewsci/bio
4. brew install opencv3 --with-contrib --with-python3


## Install OpenCV
1. sudo apt-get install python3-pip python3-dev python-virtualenv 
2. virtualenv --system-site-packages -p python3 [targetDirectory]
3. cd [targetDirectory]
4. cd lib/python3.7/site-packages
5. ln -s /usr/local/Cellar/opencv/3.4.2/lib/python3.7/site-packages/cv2.cpython-37m-darwin.so cv2.so

## Install Tensorflow
1. cd [targetDirectory]
2. source bin/activate
3. (tensorflow)$
4. (tensorflow)$ easy_install -U pip
5. (tensorflow)$ pip3 install --upgrade tensorflow-gpu
6. (tensorflow)$ pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.9.0-py3-none-any.whl 


## Install Keras 
7. pip install keras

## Install Notebook
8. python3 -m pip install jupyter
9. jupyter notebook


## Docker Version
1. docker pull jupyter/tensorflow-notebook
2. docker run --name tensorflow -d -p 8888:8888 jupyter/tensorflow-notebook
