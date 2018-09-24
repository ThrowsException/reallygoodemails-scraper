FROM tensorflow/tensorflow:latest-gpu-py3

WORKDIR /
COPY . /
RUN pip install -r requirements/rnn.txt

