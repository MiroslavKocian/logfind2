from nose.tools import *
from logfind2.search_the_specified_string import *

def test_one_string():
    expected_output = "xargs -0 grep -H -s \"lolo\""
    assert_equal(expected_output, search_the_specified_string("lolo"))

