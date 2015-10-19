from sys import argv
from logfind2.search_the_specified_string import search_the_specified_string

def run():
    search_the_specified_string(argv[1:])
    