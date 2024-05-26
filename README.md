# learn-RAG

  

This app is uses The RAG model for Qestion answering.

  

## Table of Contents

- [Requirmnt](#Requirmnt)

- [Installation](#Installation)

- [Run the project](#Runtheproject)

- [Run the FastAPI server](#run-the-FastAPI-server)

- [License](#license)

  

## Requirmnt

  

- Python 3.12.3

  

## Installation

  

### Steps to Run on the Server

1.  Redirect to home 
```bash
 $ cd ~
```
2. Download and install MiniConda by runing : 
``` bash
$  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
``` 

3. Change the mood of miniconda
``` bash 
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
```
4.  Execute the Miniconda installer script on a Linux system
``` bash
$ ./Miniconda3-latest-Linux-x86_64.sh
```
5. press q then write "yes"

6. Runs the `.profile` script to apply any changes made to the user’s environment setup
``` bash
$ bash ~/.profile
```
7.  Create a new environment using the following command:
``` bash 
$ conda create -n learn-rag-app python==3.12.3
```
8. Activate the environment
``` bash
$ conda activate learn-rag-app
```

## Runtheproject
``` bash
$ pip install -r requirements.txt
```

## Run the FastAPI server
``` bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```