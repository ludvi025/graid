# HW File Pool
# 
# Handles maintaining the list of files to be graded:
# 1. Allow multiple TA's to grade simultaneously by keeping track of who's 
#    grading what
# 2. Selects files matching a pattern from the grading directory
# 3. Ensure that all files are graded

from .recurse.rfind import rfind

# Folders to ignore
IGNORE = "__MACOSX"

class Pool:
    def __init__(_, patterns, root_dir):
        _.files = []
        for pattern in patterns:
            files = rfind.find(pattern, root_dir, IGNORE)
            for f in files:
                if f not in _.files:
                    _.files.append(f)

    def __iter__(_):
        return PoolIter(_.files)

    def checkRemaining(_):
        pass

    def getNext(_):
        # Get the next file that hasn't been graded and isn't in the 
        # process of being graded
        pass

class PoolIter:
    def __init__(_, files):
        _.files = files
        _.index = 0
        _.end = len(files - 1)

    def __next__(_):
        if _.index == _.end:
            raise StopIteration
        _.index += 1
        # TODO: Make this do something more useful
        return _.files[_.index]
