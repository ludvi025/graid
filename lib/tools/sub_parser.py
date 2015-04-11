import re
from pathlib import Path

regex = r"(?:.*/)?(?P<firstname>[^/]*) (?P<lastname>[^/]*)_(?P<moodleid>\d*)_\w*/?.*"
#compileing the regex is optional. It is a performance optimization.
cmp_regex = re.compile(regex)

def parseSub(file_path):
    file_path = Path(file_path).as_posix()
    m = re.match(cmp_regex, file_path)
    if m:
      return {
          'last_name' : m.group('lastname'), 
          'first_name' : m.group('firstname'), 
          'moodle_id' : m.group('moodleid')
      }
    else:
      return {
          'last_name' : '', 
          'first_name' : '', 
          'moodle_id' : ''
          }

def test():
    test1 = "firstname lastname_1128269_HW2/"
    test2 = "firstname(alternatefirstname) lastname_1093811_HW2/"
    test3 = "stuff/directories/firstname lastname_1128269_HW2/"
    test4 = "stuff/directories/firstname lastname_1128269_HW2/stuffagain/file.py"
    test5 = "stuff/directories/firstname(alternatefirstname) lastname_1093811_HW2/moredire/file.py"
    test6 = ""

    for test in [test1, test2, test3, test4, test5, test6]:
        print(parseSub(test))
