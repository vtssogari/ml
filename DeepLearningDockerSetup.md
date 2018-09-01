
# Deep Learning Docker Environment Setup - Ubuntu

## Steps
1. Install NVIDIA Docker
   * Install Docker engine
   * Install NVIDIA Driver
      
``` 
      sudo apt-get nvidia-375 nvidia-modprobe, and then reboot the machine.
```
  * Run NVIDA Docker 
```
      # If you have nvidia-docker 1.0 installed: we need to remove it and all existing GPU containers
      docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
      sudo apt-get purge -y nvidia-docker

      # Add the package repositories
      curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
        
      curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
      sudo apt-get update

      # Install nvidia-docker2 and reload the Docker daemon configuration
      sudo apt-get install -y nvidia-docker2
      sudo pkill -SIGHUP dockerd

      # Test nvidia-smi with the latest official CUDA image
      docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```
    
2. Install Tensorflow
```
nvidia-docker run -it -p 8888:8888 tensorflow/tensorflow:latest-gpu
```
Go to your browser on http://localhost:8888/

3. Install Object Detection API Library


```
git clone https://github.com/tensorflow/models.git 
cd ./models/research

sudo apt-get install protobuf-compiler python-pil python-lxml python-tk
pip install --user Cython
pip install --user contextlib2
pip install --user jupyter
pip install --user matplotlib

wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
unzip protobuf.zip
./bin/protoc object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim 

python object_detection/builders/model_builder_test.py

```
4. Custom Training object
    * Build TFRecord Training set and Testing set
    * Create Label Set
    * 

5. Choose Model and configure file
```
+data
  -label_map file
  -train TFRecord file
  -eval TFRecord file
+models
  + model
    -pipeline config file
    +train
    +eval
    
TensorFlow
├─ addons
│ └─ labelImg
├─ models
│ ├─ official
│ ├─ research
│ ├─ samples
│ └─ tutorials
└─ workspace
   └─ training_demo
      ├─ annotations
      ├─ images
      │ ├─ test
      │ └─ train
      ├─ pre-trained-model
      ├─ training
      └─ README.md   
```    

    * annotations: This folder will be used to store all *.csv files and the respective TensorFlow *.record files, which contain the list of annotations for our dataset images.
    * images: This folder contains a copy of all the images in our dataset, as well as the respective *.xml files produced for each one, once labelImg is used to annotate objects.
    * images\train: This folder contains a copy of all images, and the respective *.xml files, which will be used to train our model.
    * images\test: This folder contains a copy of all images, and the respective *.xml files, which will be used to train our model.
    * pre-trained-model: This folder will contain the pre-trained model of our choice, which shall be used as a starting checkpoint for our training job.
    * training: This folder will contain the training pipeline configuration file *.config, as well as a *.pbtxt label map file and all files generated during the training of our model.
    * README.md: This is an optional file which provides some general information regarding the training conditions of our model. It is not used by TensorFlow in any way, but it generally helps when you have a few training folders and/or you are revisiting a trained model after some time.

--move images to "images" folder
create TFRecord
create label_map.pbtxt and move to "training" folder
select model configuration models/research/object_detection/samples/configs then copy to "training" folder
configure the model 
download pre-trained-model

6. Running the Training Job

7. Running Tensorboard
