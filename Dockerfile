FROM ubuntu
COPY . /webservice 
WORKDIR /webservice
RUN apt-get update && apt-get install -y
RUN apt install python3 -y
CMD python3 webservice.py

