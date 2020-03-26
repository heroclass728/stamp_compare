# StampComparison

## Overview

This project is to compare two stamp images to estimate the similarity score between them. When the client sends the 
request url with the image https urls, the project returns the response with similarity score. The web server is run by 
Flask.

## Structure

- src

    The source code to compare two stamp images and get the https image url.

- utils

    The source code for image processing and folder, file management.

- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    The several settings for folder, file path and web server.

## Installation

- Environment

    Ubuntu 18.04, Python 3.6
    
- Dependency Installation

    ```
        pip3 install -r requirements.txt
    ```
  
## Execution

- Please go ahead the project directory and run the following command.

    ```
        python3 app.py
    ```
