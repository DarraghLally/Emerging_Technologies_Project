# Emerging Technology Project 2020

## Power Prediction Application
*Darragh Lally, 4th year Computer Science student, GMIT. G00220290*

### Introduction
This repositiory contains my solution to the 2020 project for Emerging Technologies, delivered by Dr. Ian McLoughlin. The task requires me to create a model that will predict the power generated from a wind speed value provided by a user. To do this I will need to implement a number of steps:
1. Create a prediction model in jupyter notebook.
2. Create a web application that will accept a value and return a prediction.
3. Use Docker to create an image of my application and a container in which my application will run. 
The above 3 items and git repo standard items make up the submission for this project.

#### Repository Contents
* misc folder:
    * Assesment spec.
    * power production data x2 - .csv and .xlsx.
* static folder:
    * index.html: Web page that displays the application.
    * Web page background image.
* .dockerignore
    * File similar to a .gitignore, which tells Docerfile what to ignore when creating the container.
* Dockerfile:
    * Used to create an Image, and then a Container within which my project will run.
* Jupyter-notebook:
    * Used to train a model that can predict a power output from a wind speed input.
* model.h5:
    * A model created from the power production .csv
* requirements.txt:
    * Used by the Dockerfile to get a list of required packages.
* web-service.py
    * A python script that runs our web application.
* General repo files
    * .gitignore - python
    * README.md

### Useful Commands
#### LINUX: How to run web-service
``` bash
$ export FLASK_APP=web-service.py
$ python3 -m flask run
 * Running on http://127.0.0.1:5000/
```

#### WINDOWS: How to run web-service
``` bash
set FLASK_APP=web-service.py
python -m flask run
 * Running on http://127.0.0.1:5000/
```

#### Docker: Create image and container, run
* navigate to repo
* run cmder
``` bash
docker --version
docker build -t web-service
docker run --name web-service-container -d -p 5000:5000 web-service-image
```

#### References
random-app - Dr. Ian McLoughlin; GitHub: https://github.com/ianmcloughlin/random-app/blob/master/rando.py

Flask: https://www.tutorialspoint.com/flask/flask_templates.htm

Docker - What is a container?: https://www.docker.com/resources/what-container


