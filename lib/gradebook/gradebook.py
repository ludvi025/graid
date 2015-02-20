from ..recurse.rfind import rfind
from . import record

class Gradebook:
    def __init__(_, user_ids):
        _.records = []

    def __iter__(_):
        return iter(_.records)

    def addRecord(_, record):
        _.records.append(record)

    def fromFiles(_, grade_file_name, root_dir='.'):
        files = rfind(grade_file_name, root_dir)
        records_loaded = 0

        for f in files:
            record = Record.fromFile(f)
            if record:
                records_loaded += 1
            else:
                print('Failed to load record: {}'.format(f))
