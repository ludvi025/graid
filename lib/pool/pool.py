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
        return PoolIter(_.hws)

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
    def __init__(_, hws):
        _.hws = hws
        _.index = 0
        _.end = len(hws - 1)

    def __next__(_):
        if _.index == _.end:
            raise StopIteration
        _.index += 1
        return _.hws[_.index]
