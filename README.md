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

### Example
What the output looks like for a *binary tree* of `depth = 4`:
```
{}
├── 0
│   ├── 0
│   │   ├── 0
│   │   │   ├── 0
│   │   │   └── 1
│   │   └── 1
│   │       ├── 0
│   │       └── 1
│   └── 1
│       ├── 0
│       │   ├── 0
│       │   └── 1
│       └── 1
│           ├── 0
│           └── 1
└── 1
    ├── 0
    │   ├── 0
    │   │   ├── 0
    │   │   └── 1
    │   └── 1
    │       ├── 0
    │       └── 1
    └── 1
        ├── 0
        │   ├── 0
        │   └── 1
        └── 1
            ├── 0
            └── 1

Total combinations: 16
```
Notice that the *root* of the tree is the *empty set* denoted by `{}`. Also the
*total combinations* (i.e. all possible binary numbers of the given bit-length)
are printed at the bottom.
