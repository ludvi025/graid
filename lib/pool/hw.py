from os import path
import json
from ..tools import parseSub
from ..debug import dbprint

FILE_EXT = '.status'

class HW:
    statuses = ('not started', 'in progress', 'graded', 'error')

    def __init__(_, file_path, session_name):
        _.file_path = file_path
        _.student_info = parseSub(file_path)
        _.session_name = session_name
        _.status = 'not started'

    def getStatusPath(_):
        file_dir = _.getFileDir()
        return path.join(file_dir, _.session_name + FILE_EXT)

    def getFileDir(_):
        return path.dirname(_.file_path)

    def getStudentInfo(_):
        return _.student_info
            
    def getStatus(_, force_check_graded=False):
        # Save time by not reading file if graded
        if _.status == 'graded' and not force_check_graded:
            return _.status
        else:
            dbprint('there')
            status_path = _.getStatusPath()
            if path.exists(status_path):
                try: 
                    f = open(status_path, 'r')
                    _.status = json.load(f)
                    f.close()
                    return _.status
                except:
                    return 'error'
            else:
                return 'not started'

    def setStatus(_, status):
        if status not in HW.statuses:
            return False # TODO: Change this to raise an error
        else:
            status_path = _.getStatusPath()
            try:
                f = open(status_path, 'w')
                json.dump(status, f)
                f.close() 
                _.status = status
                return True
            except:
                _.status = 'error'
                return False
