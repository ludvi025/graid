from os import path
import json
from ..tools import parseSub
from ..debug import dbprint

FILE_NAME = 'status.json'

class HW:
    statuses = ('not started', 'in progress', 'graded', 'error')

    def __init__(_, file_path):
        _.file_path = file_path
        _.first_name, _.last_name, _.moodle_id = parseSub(file_path)
        _.status = 'not started'

    def getStatusPath(_):
        file_dir = _.getFileDir()
        return path.join(file_dir, FILE_NAME)

    def getFileDir(_):
        return path.dirname(_.file_path)

    def getStudentInfo(_):
        student_info = {
            'first_name': _.first_name,
            'last_name': _.last_name,
            'moodle_id': _.moodle_id
        }
        return student_info
            
    def getStatus(_, force_check_graded=False):
        # Save time by not reading file if graded
        if _.status == 'graded' and not force_check_graded:
            return _.status
        else:
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
