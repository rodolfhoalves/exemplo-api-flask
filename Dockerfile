FROM ubuntu:20.04

RUN apt-get update \
    && apt-get check \
    && apt-get clean -y \ 
    && apt-get autoclean -y \
    && apt-get autoremove --purge -y

RUN apt-get install python3 -y
RUN  apt-get install python3-pip -y

WORKDIR /api
COPY . /api

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
