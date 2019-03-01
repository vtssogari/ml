
# Install Spark

## Linux
export SPARK_HOME=/YourSparkHome
export PATH=$SPARK_HOME/bin:$PATH

## Window
set SPARK_HOME=C:\YourSparkHome
set PATH=%PATH%;C:\YourSparkHome\bin

## python spark shell
pyspark

# Using Jupyter Notebook for pyspark
pip install jupyter

## Linux
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'

## Windows
set PYSPARK_DRIVER_PYTHON=jupyter
set PYSPARK_DRIVER_PYTHON_OPTS='notebook'
