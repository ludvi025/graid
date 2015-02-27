import os
import csv
from ..debug import db_exec_info, dbprint

# Fields to take from each instance of `Record` in the `Gradebook`
FIELDS = 'user_id,moodle_id,grade,comments,grader'
FIELDS = FIELDS.split(',')

# Header row for the exported gradebook, shall parallel FIELDS
MOODLE_FIELDS = 'User id,Moodle id,Grade,Comments,Grader ID'
MOODLE_FIELDS = MOODLE_FIELDS.split(',')

assert len(FIELDS) == len(MOODLE_FIELDS)

# Hack for outputting the header in the exported gradebook
HEADER_ROW = {FIELDS[i]: MOODLE_FIELDS[i] for i in range(len(FIELDS))}

# Shall be the same as header of user id to moodle id pairing file
# and match the fields in FIELDS
TO_USER_ID_KEY = 'moodle_id'
USER_ID_KEY = 'user_id'

# Takes a Gradebook class and output file and creates CSV file ready to
# be uploaded to moodle
def exportGradebook(grade_book, output_file, user_ids_path=None):
    try:
        # Load user id map
        uids = {}
        if user_ids_path != None:
            fin = open(user_ids_path)
            for row in csv.DictReader(fin, [TO_USER_ID_KEY, USER_ID_KEY]):
                to_user_id = row[TO_USER_ID_KEY]
                user_id = row[USER_ID_KEY]
                uids[to_user_id] = user_id

            fin.close()
        dbprint(uids)

        fout = open(output_file, 'w')
        cout = csv.DictWriter(fout, FIELDS)
        cout.writerow(HEADER_ROW)

        for record in grade_book:
            if user_ids_path != None:
                if record[TO_USER_ID_KEY] in user_ids_path:
                    to_user_id = uids[record[TO_USER_ID_KEY]]
                    record[USER_ID_KEY] = uids[to_user_id]
                else:
                    record[USER_ID] = 'xxxxx000'
            else:
                record[USER_ID] = 'xxxxx000'
            cout.writerow(record)

        fout.close()
        return True

    except:
        dbprint(db_exec_info())
        return False
