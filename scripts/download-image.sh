#!/bin/bash
#Make a pull request to Docker hub Image
docker pull alarav/python
#Crete a Docker container that will run as a daemon and 
#create a mapping betwen 80 port of server to 5000 port of container
docker run --rm -d --name=web-server -p 80:5000 alarav/python


