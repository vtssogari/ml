#First, in your remote machine:

ipython notebook --no-browser --port=7000

#Then, in your local machine:

ssh -N -f -L localhost:7000:localhost:7000 username@remote.computer.name
