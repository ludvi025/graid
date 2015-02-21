from ..recurse.rfind import rfind
from . import record

class Gradebook:
    def __init__(_):
        _.records = []

    def __iter__(_):
        return iter(_.records)

    def addRecord(_, record):
        _.records.append(record)

    # Should this be grade_file_name or a list of paths???
    def fromFiles(_, grade_file_name, root_dir='.'):
        files = rfind(grade_file_name, root_dir)
        records_loaded = 0

        for f in files:
            record = Record.fromFile(f)
            if record:
                records_loaded += 1
                _.addRecord(record)
            else:
                print('Failed to load record: {}'.format(f))
