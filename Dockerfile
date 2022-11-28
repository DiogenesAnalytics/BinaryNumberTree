# base image
FROM python:3.10.6

# set workdir
WORKDIR /BinaryNumberTree

# get src
COPY . /BinaryNumberTree

# now install requirements
RUN apt-get update && pip install -r requirements.txt

# set entry
ENTRYPOINT ["python3", "/BinaryNumberTree/bntree.py"]

# set default command
CMD ["-h"]
