
import os


def read_file():
    infile = open("data\crappy_db.txt")
    for line in infile:
        yield line
    infile.close()


for line in read_file():
    print(line)
