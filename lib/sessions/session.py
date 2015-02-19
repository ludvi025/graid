import os
import json

class Session:
    def __init__(_, name, patterns, tests, points):
        _.name = name
        _.patterns = patterns
        _.tests = tests
        _.points = points

    @property
    def filename(_):
        return Session.__filename(_.name)

    def __filename(name):
        return name + '.session'

    def fromFile(name):
        filename = Session.__filename(name)

        if os.path.isfile(filename):
#            try:
            fin = open(filename)
            patterns = json.loads(fin.readline())
            tests = json.loads(fin.readline())
            points = float(json.loads(fin.readline()))
            fin.close()

            return Session(name, patterns, tests, points)
            #except:
            #    return None
        else:
            return None
