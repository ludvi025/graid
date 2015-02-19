# Session Manager
#
# Handle creation and loading of sessions.

import os
import json

class SessionManager:
    def __init__(_):
        pass

    def loadSession(_, name):
        file_name = name+'.session'
        if os.path.isfile(file_name):
            fin = open(file_name)
            patterns = json.loads(fin.readline())
            tests = json.loads(fin.readline())
            maxpoints = float(json.loads(fin.readline()))
            fin.close()
            return {"patterns": patterns, "tests": tests, "maxpoints": maxpoints}
        else:
            return False

class Session:
    def __init__(_, filename, patterns, tests, points):
        _.filename = filename
        _.patterns = patterns
        _.tests = tests
        _.points = points

    def load(_):
        file_name = name+'.session'
        if os.path.isfile(file_name):
            fin = open(file_name)
            patterns = json.loads(fin.readline())
            tests = json.loads(fin.readline())
            maxpoints = float(json.loads(fin.readline()))
            fin.close()
            return {"patterns": patterns, "tests": tests, "maxpoints": maxpoints}
        else:
            return False

def getSession(name):

def writeSession(name, patterns, tests, maxpoints):
    fn = name+'.session'
    fout = open(fn, 'w')
    fout.write(json.dumps(patterns)+'\n')
    fout.write(json.dumps(tests)+'\n')
    fout.write(json.dumps(maxpoints)+'\n')
    fout.close()
