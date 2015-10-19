from sys import argv

def search_the_specified_string(argv):
    specified_string = "xargs -0 grep -H -s " + ' '.join([str(item) for item in argv[1:]]) 
    return specified_string