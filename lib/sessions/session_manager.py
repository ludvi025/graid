import json

from .. import inputs
from .session import Session

class SessionManager:
    patterns_help = """
Enter one or more UNIX file name patterns to identify the scripts which 
need grading. Separate patterns with a comma.
"""

    tests_help = """
Enter paths to all testing scripts you would like to run against the 
homework, separated by commas.
"""

    points_help = """
Enter the maximum point value for the assignment to verify that students 
are not given extra credit.
"""

    # TODO: Add root directory?
    def __init__(_):
        pass

    def createSession(_):
        name = input('Enter session name: ')
        patterns = input('Enter patterns: ').replace(' ','').split(',')
        tests_str = input('Enter test paths: ')
        if tests_str != '':
            tests = tests_str.replace(' ','').split(',')
        else:
            tests = None
        points = inputs.prompt.Points().get()
        return Session(name, patterns, tests, points)

    def loadSession(_, name):
        return Session.fromFile(name)

    def saveSession(_, session):
        try:
            fout = open(session.filename, 'w')
            fout.write(json.dumps(session.patterns)+'\n')
            fout.write(json.dumps(session.tests)+'\n')
            fout.write(json.dumps(session.points)+'\n')
            fout.close()
            return True
        except:
            return False


