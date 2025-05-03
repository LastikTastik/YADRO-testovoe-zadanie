FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip

WORKDIR /script

COPY . /script/

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "script_http.py" ]