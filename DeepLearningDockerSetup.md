
# Deep Learning Docker Environment Setup - Ubuntu

## Steps
1. Install NVIDIA Docker
    * Install NVIDIA Driver
      
      ``` 
      docker run -it --name nvidia-driver --privileged --pid=host \
         -v /run/nvidia:/run/nvidia:shared nvidia/driver:396.37-ubuntu16.04
      ```
    * Install Docker engine 
2. Install Tensorflow
