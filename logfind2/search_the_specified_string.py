def search_the_specified_string(arguments):
   specified_string = "xargs -0 grep -H -s " + ' '.join([str(item) for item in arguments]) 
   return specified_string