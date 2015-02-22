import json

from .. import inputs
from .session import Session

class SessionManager:
    patterns_help = """
Enter one or more UNIX file name patterns to identify the scripts which 
need grading. Separate patterns with a comma.
"""

    test_help = """
Enter paths to all testing scripts you would like to run against the 
homework, separated by commas.
"""

    points_help = """
Enter the maximum point value for the assignment to verify that students 
are not given extra credit.
"""

    def __init__(_, root_dir='.'):
        _.root_dir = root_dir

    # TODO: Add input validation to make sure all fields were correct
    def createSession(_):
        name = input('Enter session name: ')
        dp = inputs.DirPath('Enter homework directory path: ', \
                            must_exist=True)
        hw_dir = dp.get()

        patterns = input('Enter patterns: ').replace(' ','').split(',')

        fp = inputs.FilePath('Enter test path: ', \
                             must_exist=True, accept_empty=True)
        test = fp.get()

        points = inputs.Points().get()
        return Session(name, hw_dir, patterns, test, points)

    def editSession(_, session):
        print('Leave blank and press enter to leave unchanged.')
        name = input('Enter session name: ')
        dp = inputs.DirPath('Enter hw directory path: ', \
                            must_exist=True, accept_empty=True)
        hw_dir = dp.get()

        patterns = input('Enter patterns: ').replace(' ','').split(',')

        fp = inputs.FilePath('Enter test path: ', \
                             must_exist=True, accept_empty=True)
        test = fp.get()

        points = inputs.Points(accept_empty=True).get()
        if name != '':
            session.name = name
        if hw_dir != '':
            session.hw_dir = hw_dir
        if patterns != '':
            session.patterns = patterns
        if test != '':
            session.test = test
        if points != '':
            session.points = points

    def loadSession(_):
        name = input('Enter session name: ')
        return Session.fromFile(name, _.root_dir)

    def saveSession(_, session):
        return session.toFile(_.root_dir)


