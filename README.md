# Installation Instructions
The following instructions will show you how to install Z3 using Docker.

## Prerequisites
This guide assumes you have Docker installed. If this is not the case, you can follow the official [installation instructions](https://docs.docker.com/get-docker/).

## Cloning the Repository
Once you have Docker installed, you can clone this repository and enter the newly created directory. You can either use [GitHub Desktop](https://desktop.github.com/) and a file manager or enter the following commands in the terminal or command line.
```bash
git clone https://github.com/sebivenlo/ESDE-2021-z3-workshop.git z3-workshop/
cd z3-workshop/workshop
```
## Building the Base Image
After cloning the repository, build the base image and start the container in the background. Note: On Linux, you might have to use `sudo` before each docker command.
```bash
docker build -t docker-python .
docker run --name z3-container -td docker-python
```
## Verifing the Installation
You can verify that z3 has been installed correctly by executing `z3 --version` within the container:
```bash
docker exec -it z3-container z3 --version
```
The output should be the version of Z3, for example `Z3 version 4.8.12 - 64 bit`. This could be different depending on your operating system.

## Usage
To use Python with Z3 from within the container, use the following command to copy the script to the container, then execute the file within the container. Replace `tasks.py` after `docker cp` with the name of your script, if required.
```bash
docker cp tasks.py z3-container:/usr/src/app/tasks.py && docker exec -it z3-container python tasks.py
```

# Workshop
The workshop file is included in the repository under `tasks.py`. The assignments are shown as comments.
<hr>

## Background Knowledge: Run Z3 scripts with the smtlib2 syntax
Although not required for the workshop, the docker container also contains the Z3 binary, allowing you to run z3 scripts with the smtlib2 syntax similar to the way Python scripts are run within the container.
```bash
docker cp script.z3 z3-container:/usr/src/app/script.z3 && docker exec -it z3-container z3 script.z3
```
