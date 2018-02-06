FROM python:3.6

RUN pip install --no-cache-dir python-qpid-proton==0.20.0

COPY . /usr/local/src
WORKDIR /usr/local/src

ENTRYPOINT ["python", "helloworld_blocking.py"]

