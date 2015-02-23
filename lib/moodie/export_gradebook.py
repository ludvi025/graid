import os
import csv
from ..debug import db_exec_info, dbprint

# Shall be the same as header of grade book
FIELDS = 'user_id,moodle_id,first_name,last_name,grade,comments,grader'
FIELDS = FIELDS.split(',')

MOODLE_FIELDS = 'User id,Moodle id,First name,Last name,Grade,Comments,Grader ID'
MOODLE_FIELDS = MOODLE_FIELDS.split(',')

assert len(FIELDS) == len(MOODLE_FIELDS)

HEADER_ROW = {FIELDS[i]: MOODLE_FIELDS[i] for i in range(len(FIELDS))}

# Shall be the same as header of user id to moodle id pairing file
# and match the fields in FIELDS
STUDENT_INFO_FIELDS = 'user_id,first_name,last_name'.split(',')

# Takes a Gradebook class and output file and creates CSV file ready to
# be uploaded to moodle
def exportGradebook(grade_book, output_file, user_ids_path=None):
    try:
        # Load user id map
        uids = {}
        if user_ids_path != None:
            fin = open(user_ids_path)
            for row in csv.DictReader(fin, STUDENT_INFO_FIELDS):

                # TODO: Fix this. Too hacky
                key = getNameKey(row['first_name'], row['last_name'])
                uids[key] = row['user_id']

            fin.close()
        dbprint(uids)

        fout = open(output_file, 'w')
        cout = csv.DictWriter(fout, FIELDS)
        cout.writerow(HEADER_ROW)

        for record in grade_book:
            if user_ids_path != None:
                key = getNameKey(record['first_name'], record['last_name'])
                record['user_id'] = uids[key]
            else:
                record[USER_ID] = '#######'
            cout.writerow(record)

        fout.close()
        return True

    except:
        dbprint(db_exec_info())
        return False

def getNameKey(first, last):
    key = (last+first)
    for c in ' \'\"':
        key = key.replace(c, '')
        key = key.lower()
    return key
