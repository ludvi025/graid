from ..tools import rfind
from .record import Record
from ..debug import dbprint

class Gradebook:
    def __init__(_, records=None):
        if records == None:
            _.records = []
        else:
            _.records = records

    def __iter__(_):
        return iter(_.records)

    def addRecord(_, record):
        _.records.append(record)

    def fromFiles(grade_file_name, root_dir='.'):
        files = rfind(grade_file_name, root_dir)
        records = []

        for f in files:
            record = Record.fromFile(f)
            if record:
                records.append(record)
            else:
                print('Failed to load record: {}'.format(f))

        return Gradebook(records)
