from lib.moodie.unpack import unpack
from lib.tools import parseSub
from lib.gradebook import Gradebook
import csv

#unpack('./test/test1.zip')

# Weird Subs
#print(parseSub('Kaitlin (Kate) Kuehl_1330270_assignsubmission_file_hw1.py'))
#print(parseSub('Jay Adams III_1330266_assignsubmission_file_hw1.py'))
#print(parseSub('Tom Van Deusen_1330123_assignsubmission_file_hw1.py'))

gb = Gradebook.fromFiles('testy.grade', 'test/test1')

FIELDS = 'user_id,moodle_id,first_name,last_name,grade,comments,grader'
FIELDS = FIELDS.split(',')

fout = open('test.csv', 'w', newline='')
cout = csv.DictWriter(fout, FIELDS)
cout.writeheader()
for record in gb:
    cout.writerow(record)
