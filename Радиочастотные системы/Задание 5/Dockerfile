FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
        wget \
        python3 \
        python3-pip 

COPY . /tmp/

RUN chmod +x /tmp/search_path.sh \
             /tmp/extract_path_value.py
