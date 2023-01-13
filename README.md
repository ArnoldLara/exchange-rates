# exchange-rates
This is a public repositoty for a Currency convertor project that use the following API https://apilayer.com/marketplace/exchangerates_data-api for make conversions. This project was build using Flask which is lightweight Framework for build web services and APIs in Python.
You have two options to deploy this project, one of then using this repository and the second one using a Docker Image stored in Docker hub(docker pull alarav/python:latest). To running this project you will have to meet following requirements depend the way that you choose to deploy:
 - Linux/Windows Machine with Docker installed(Deploy using Docker Image)
 - Linux machine with Git, python, pip and virtualenv(Deploy using github repository)
 - Allow your machine can listen connections on port 80(Deploy using Docker Image)
 - Allow your machine can listen connections on port 5000(Deploy using github repository)
 - Garantee internet connection on the server

 Steps to deploy using Docker
- In the server you have to run the script download-image.sh located on web_rates/script folder. This script download a docker image and run the docker container

 Steps to deploy using Kubernetes
 - In script folder you can find a Manifest that allows you to run a pod with the docker image of the project.
