from ..tools import rfind
from ..debug import dbprint
from .hw import HW

# Folders to ignore
IGNORE = "__MACOSX"

class Pool:
    def __init__(_, patterns, root_dir, session_name):
        _.hws = []
        _.session_name = session_name

        # Locate all files that might need to be graded
        files = []
        for pattern in patterns:
            files += rfind(pattern, root_dir, IGNORE)
        # Remove duplicates
        files = sorted(set(files))

        for f in files:
            _.hws.append(HW(f, session_name))

    def __iter__(_):
        return PoolIter(_.hws)

    def getStatusCounts(_):
        counts = {status: 0 for status in HW.statuses}
        for hw in _:
            status = hw.getStatus()
            counts[status] += 1
        return counts

    def recheckAll(_):
        for hw in _:
            status = hw.getStatus(force_check_graded=True)

    def getNextHW(_):
        for hw in _:
            if hw.getStatus() == 'not started':
                return hw
        return None

    def clearInProgress(_):
        count = 0
        for hw in _:
            if hw.getStatus() == 'in progress':
                hw.setStatus('not started')
                count += 1
        return count

class PoolIter:
    def __init__(_, hws):
        _.hws = hws
        _.index = 0
        _.end = len(hws)

    def __next__(_):
        if _.index == _.end:
            raise StopIteration
        hw = _.hws[_.index]
        dbprint(hw.file_path)
        _.index += 1
        return hw
