from .recurse.rfind import rfind
from .hw import HW

# Folders to ignore
IGNORE = "__MACOSX"

class Pool:
    def __init__(_, patterns, root_dir):
        _.hws = []

        # Locate all files that might need to be graded
        files = []
        for pattern in patterns:
            files += rfind.find(pattern, root_dir, IGNORE)
        # Remove duplicates
        files = sorted(set(files))

        for f in files:
            _.hws.append(HW(f))

    def __iter__(_):
        return PoolIter(_.files)

    def getStatusCounts(_):
        counts = {status: 0 for status in HW.statuses}
        for hw in _:
            status = hw.getStatus()
            counts[status] += 1
        return counts

    def getNextHW(_):
        for hw in _:
            if hw.getStatus() == 'not started':
                return hw

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
