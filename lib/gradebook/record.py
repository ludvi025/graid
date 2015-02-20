import json

class Record(dict):
    def __init__(_, moodle_id, first_name, last_name, \
                 grade, comments, grader, complete=False):
        _['moodle_id'] = moodle_id
        _['first_name'] = first_name
        _['last_name'] = last_name
        _['grade'] = grade
        _['comments'] = comments
        _['grader'] = grader
        _['complete'] = complete

    def toFile(_, output_path):
        try:
            fout = open(output_path, 'w')
            fout.write(_.toJSON()) 
            fout.close()
            return True
        except:
            return False

    def toJSON(_):
        return json.dumps(_)# Because inherits dict

    def fromFile(file_path):
        try:
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
