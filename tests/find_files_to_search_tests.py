from nose.tools import *
from logfind2.find_files_to_search import *

def test_file_regex(): 
    assert_equal('".*\\(\.txt\\)"', file_regex('\.txt'))
    assert_equal('".*\\(\.txt\\|\.log\\)"', file_regex('\.txt', '\.log'))
    
    expected_string = '".*\\(\.txt\\|\.log\\|\.tmp\\)"'
    assert_equal(expected_string, file_regex('\.txt', '\.log', '\.tmp'))