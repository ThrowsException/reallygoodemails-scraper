# reallygoodemails-scraper
Pull html from the reallygoodemails.com site


# Machine Learning
## Getting Started

### Running the tensorflow training program

This uses just the CPU of your machine and its fairly slow

```
pip install -r requirements/rnn-dev.txt
python rnn/train.py
```

### Running the docker image with GPU support 

Way faster than just using the cpu

#### Prerequisites
- docker
- nvidia-docker https://github.com/NVIDIA/nvidia-docker
- nvidia-drivers https://www.nvidia.com/object/unix.html
- nvidia cuda support https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

The docker container handles the rest including installing the tensorflow package with gpu support enabled

```
docker build . -t ml-nvidia
docker run --runtime=nvidia -v $PWD:/tmp/ ml-nvidia python /tmp/rnn/train.py
```
