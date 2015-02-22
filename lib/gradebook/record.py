import json
from os import path

FILE_EXT = '.grade'

class Record(dict):
    def __init__(_, moodle_id, first_name, last_name, \
                 grade, comments, grader):
        _['moodle_id'] = moodle_id
        _['first_name'] = first_name
        _['last_name'] = last_name
        _['grade'] = grade
        _['comments'] = comments
        _['grader'] = grader

    def toFile(_, name, directory):
        try:
            file_path = path.join(directory, name + FILE_EXT)
            fout = open(file_path, 'w')
            fout.write(_.toJSON()) 
            fout.close()
            return True
        except:
            return False

    def toJSON(_):
        return json.dumps(_)# Because inherits dict

    def fromFile(name, directory):
        try:
            file_path = path.join(directory, name + FILE_EXT)
            d = json.load(file_path)
            return Record(*d)
        except:
            return None

    def fromJSON(json_str):
        try:
            d = json.loads(json_str)
            return Record(*d)
        except:
            return None
