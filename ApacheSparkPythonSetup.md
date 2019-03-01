
# Install Spark

## Linux
export SPARK_HOME=/YourSparkHome

export PATH=$SPARK_HOME/bin:$PATH

## Window
set SPARK_HOME=C:\YourSparkHome

set HADOOP_HOME=C:\YourHadoopHome

* download the https://github.com/steveloughran/winutils/blob/master/hadoop-2.6.0/bin/winutils.exe?raw=true to bin folder

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


# start pyspark
pyspark

# Notebook sc and spark variable should be available
