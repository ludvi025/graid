from os import path
from ..gradebook import Record

class HW:
    def __init__(_, file_path):
        _.file_path = file_path
        _.graded()

    def graded(_, grade_file_name):
        file_dir = path.dirname(_.file_path)
        grade_path = path.join(file_dir, grade_file_name)
        if path.exists(grade_path)
            record = Record.fromFile(grade_path)
            return record['complete']
        else:
            return False
            


