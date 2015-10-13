from sys import argv

def run():
    search_the_specified_string = "xargs -0 grep -H -s " + ' '.join([str(item) for item in argv[1:]]) 
    print search_the_specified_string