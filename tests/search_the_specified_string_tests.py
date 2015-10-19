from nose.tools import *
from logfind2.search_the_specified_string import *
from sys import arguments

def test_empty_single_space_string():
    arguments = " "
    assert_equal("xargs -0 grep -H -s  ", search_the_specified_string(arguments))

def test_one_character_string():
    arguments = "b"
    assert_equal("xargs -0 grep -H -s b", search_the_specified_string(arguments))
