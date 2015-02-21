from sys import argv

# Use dbprint to add print statements that only print if
# graid.py called with debug as a command line argument
debug = 'debug' in argv
dbprint = print if debug else lambda *args, **kwargs: None
