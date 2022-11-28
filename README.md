# BinaryNumberTree
Simple Python 3 :snake: script to generate a binary tree :evergreen_tree:
corresponding to all possible binary numbers :zero::one::zero::one:
of a given bit-length.

## Usage
Below are instructions for how to run the script.

### Docker
The easiest way is to use `Docker` and run the following command:
```
docker run --rm -it ghcr.io/diogenesanalytics/binarynumbertree:master #DEPTH
```
where `DEPTH` is the *depth* of the binary tree that you want to generate, and
also the *bit-length* of the binary numbers that will be generated. Also,
simply running the *container* without the *depth argument* will generate the
help message:
```
usage: bntree [-h] depth

Generate binary tree of all binary numbers of a certain bit-length.

positional arguments:
  depth       depth of the binary tree or bit-length of binary numbers

options:
  -h, --help  show this help message and exit
```
