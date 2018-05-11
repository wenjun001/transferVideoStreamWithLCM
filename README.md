# transferVideoStreamWithLCM

#### firslty run /gen-types.sh

#### then pub video python pubVideoStream.py
#### open other termals to sub video python pubVideoStream.py

####if in different machines need configure following:

sudo ifconfig eth1 multicast  
sudo route add -net 224.0.0.0 netmask 240.0.0.0 dev eth1

you need change eth1 to your local network interface


TO DO: need compress video stream to improve performance.
