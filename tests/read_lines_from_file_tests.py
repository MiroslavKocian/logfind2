from nose.tools import *
from logfind2.read_lines_from_file import *

def test_read_lines_from_file():
    expected_list = [".txt", ".log", ".tmp", ".wav"]
    assert_equal(expected_list, read_lines_from_file())
    print read_lines_from_file()