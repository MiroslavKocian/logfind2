from sys import argv

def search_the_specified_string():
    specified_string = "xargs -0 grep -H -s " + ' '.join([str(item) for item in argv[1:]]) 
    print specified_string