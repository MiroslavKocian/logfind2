from nose.tools import *
from logfind2.search_the_specified_string import *
from sys import argv

def test_empty_string():
    specified_string = "xargs -0 grep -H -s " + ' '.join([str(item) for item in argv[1:]])
    assert_equal("xargs -0 grep -H -s ", specified_string)

def test_short_string():
    specified_string = "xargs -0 grep -H -s b" + ' '.join([str(item) for item in argv[1:]])
    assert_equal("xargs -0 grep -H -s b", specified_string)
