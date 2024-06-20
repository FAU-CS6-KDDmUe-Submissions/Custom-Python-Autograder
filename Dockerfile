FROM python:3.11.2-slim

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN apt-get update \
    && apt-get install jq -y \
    && apt-get autoremove -y \
    && apt-get install coreutils -y \
    && rm -rf /var/lib/apt/lists/*

COPY . /python-autograder

WORKDIR /python-autograder

ENTRYPOINT [ "/python-autograder/grading.sh" ]