import os
import csv
from ..recurse.rfind import rfind

# Shall be the same as header of grade book
FIELDS = 'User id,Moodle id,First name,Last name,Grade,Comments,Grader ID'
FIELDS = FIELDS.split(',')

# Shall be the same as header of user id to moodle id pairing file
# and match the fields in FIELDS
MOODLE_ID = 'Moodle id'
USER_ID = 'User id'

# Takes a Gradebook class and output file and creates CSV file ready to
# be uploaded to moodle
def exportGradebook(grade_book, user_ids_path=None, output_file=None):
    if not output_file:
        output_file = input('Enter output file name: ')

    try:
        # Load user id map
        uids = {}
        if user_ids_path:
            fin = open(user_ids_path)
            for row in csv.DictReader(fin, [USER_ID, MOODLE_ID]):
                uids[row[MOODLE_ID]] = row[USER_ID]
            fin.close()

        fout = open(output_file, 'w', newline='')
        cout = csv.DictWriter(fout, FIELDS)
        cout.writeheader()

        for record in grade_book:
            if user_ids_path:
                record[USER_ID] = uids[record['moodle_id']]
            else:
                record[USER_ID] = '#######'
            cout.writerow(record)

        fout.close()
        return True

    except:
        return False
