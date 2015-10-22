from os.path import expanduser

def read_lines_from_file():
    home = expanduser("~")
    with open('%s/.logfind'% home) as f:
        lines = f.read().splitlines()
    return lines