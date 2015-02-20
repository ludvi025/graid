from lib.moodie.unpack import unpack
from lib.moodie.sub_parser import parseSub

#unpack('./test/test1.zip')

# Weird Subs
print(parseSub('Kaitlin (Kate) Kuehl_1330270_assignsubmission_file_hw1.py'))
print(parseSub('Jay Adams III_1330266_assignsubmission_file_hw1.py'))
print(parseSub('Tom Van Deusen_1330123_assignsubmission_file_hw1.py'))
