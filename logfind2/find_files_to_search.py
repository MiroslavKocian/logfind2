~/.logfind
.txt
.log
.tmp
.wav

file_regex(".txt", ".log", ".tmp", ".wav")

def file_regex(*regexes_in_config):
    return '".*\\({}\\)"'.format(make_or_regex(regexes_in_config))

def make_or_regex(regexes):
    return "\\|".join([regex for regex in regexes])
