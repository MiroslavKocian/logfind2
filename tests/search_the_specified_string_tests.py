from nose.tools import *
from logfind2.search_the_specified_string import *
from sys import argv

def test_empty_single_space_string():
    argv = " "
    assert_equal("xargs -0 grep -H -s ", search_the_specified_string(argv))

def test_one_character_string():
    argv = ["logfind2", "b"]
    assert_equal("xargs -0 grep -H -s b", search_the_specified_string(argv))
