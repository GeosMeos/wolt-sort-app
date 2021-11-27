FROM alpine:latest
MAINTAINER George Musayev "George.Musayev@gmail.com" 
RUN apk add --no-cache python3 py3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP app.py
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]