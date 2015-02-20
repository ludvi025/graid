from os import path
import json

FILE_NAME = 'status.json'

class HW:
    def __init__(_, file_path):
        _.file_path = file_path
        _.status = 'not started'

    def getStatusPath(_):
        file_dir = path.dirname(_.file_path)
        return path.join(file_dir, FILE_NAME)

    def getStatus(_, force_check_finished=False):
        # Save time by not reading file if finished
        if _.status == 'finished' and not force_check_finished:
            return _.status
        else:
            status_path = _.getStatusPath()
            if path.exists(status_path):
                try: 
                    f = open(status_path, 'r')
                    _.status = json.load(f)['status']
                    return _.status
                except:
                    return 'not started'
            else:
                return 'not started'

    def setStatus(_, status):
        if status not in ('not started', 'in progress', 'finished'):
            return False
        else:
            status_path = _.getStatusPath()
            f = open(status_path, 'w')
            try:
                json.dump({'status': status}, f)
                 
