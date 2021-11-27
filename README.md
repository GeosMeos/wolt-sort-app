# Idea

I want to filter wolt resutrants based on rating or price.


## Method 1 - Local Install

### Using virtual env:
Start the virtual environment
```
python3 -m venv venv
```
Activate the virtual environment
```
# Windows
.\venv\Scripts\Activate.ps1
# Linux
source venv/bin/activate
```

### Installing requirements:
Execute
```
pip3 install -r requirements.txt
```

### Environment variables:
Create environment variables for Flask application
```
# Windows
setx FLASK_APP "app.py"
# Linux
export FLASK_APP=app.py
```
### Run the flask application:
```
flask run
```
and navigate to localhost:8080 

## Method 2 - Dockerfile:

Install docker and execute the following commands:

build the image
```
docker build -t geosmeos/wolt-sort-app:latest .
```
run the container from image
```
docker run -d --name wolt-sort -p 8080:8080  geosmeos/wolt-sort-app:latest
```
and navigate to localhost:8080

## Pulling from DockerHub:

You can pull and run this image from [DockerHub](https://hub.docker.com/r/geosmeos/wolt-sort-app)
