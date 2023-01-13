#!/bin/bash
#Script to get requirements on a file, 
cd ~/python
pip freeze > ~/python/web_rates/requirements.txt
#build a Docker Image with the proyect
docker build -t alarav/python .
#Make a push to Dockerhub
docker push alarav/python:latest

