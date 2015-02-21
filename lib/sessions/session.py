from os import path
import json
from ..debug import dbprint, db_exec_info

class Session:
    def __init__(_, name, patterns, test, points):
        _.name = name
        _.patterns = patterns
        _.test = test
        _.points = points

    @property
    def file_name(_):
        return Session.__file_name(_.name)

    def __file_name(name):
        return name + '.session'

    def fromFile(name, file_dir='.'):
        file_name = Session.__file_name(name)
        file_path = path.join(file_dir, file_name) 

        if path.isfile(file_path):
            try:
                fin = open(file_path, 'r')
                d = json.load(fin)
                dbprint('JSON Loaded: ',d)
                patterns = d['patterns']
                test = d['test']
                points = d['points']
                fin.close()
                session = Session(name, patterns, test, points)
                return session
            except:
                dbprint(db_exec_info()[0])
                return None
        else:
            return None

    def toFile(_, file_dir='.'):
        try:
            file_path = path.join(file_dir, _.file_name)
            fout = open(file_path, 'w')
            json.dump({
                'patterns': _.patterns,
                'points': _.points,
                'test': _.test
            }, fout);
            fout.close()
            return True
        except:
            return False
