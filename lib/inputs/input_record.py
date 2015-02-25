from .prompt import Points
from ..gradebook import Record
import os

class InputRecord:
    def __init__(_, maxpoints):
        _.maxpoints = maxpoints

    def get(_, student_info=None):
        if not student_info:
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            moodle_id = input('Enter moodle id: ')
        else:
            first_name = student_info['first_name']
            last_name = student_info['last_name']
            moodle_id = student_info['moodle_id']

        grade = Points(_.maxpoints).get()
        comments = input('Enter comments: ').strip('\\')
        grader = os.getlogin()

        return Record(moodle_id, first_name, last_name, grade, comments, grader) 


