# What is this?

This is the wolt-sort-app , a tiny Flask app that returns sorted results from the Wolt API.
The docker image is using alpine linux.

## How to use?

Pull and run this image, the app itself is hosted on port 8080.

### Instructions:
First, pull the image from dockerhub.
```
docker pull geosmeos/wolt-sort-app:latest
```

Once the pull is complete, run a container from the image:
```
docker run -d --name wolt-sort -p 8080:8080  geosmeos/wolt-sort-app:latest
```

Navigate to localhost:8080 in your web browser.

Enjoy :) 


## Problems? Concerns?

Feel free to open an issue in the [repository](https://github.com/GeosMeos/wolt-sort-app).

Contact the developer on [GitHub](https://github.com/GeosMeos).