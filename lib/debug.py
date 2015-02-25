from sys import argv, exc_info

# Use dbprint to add print statements that only print if
# graid.py called with debug as a command line argument
debug = 'debug' in argv
dbprint = print if debug else lambda *args, **kwargs: None
db_exec_info = exc_info
