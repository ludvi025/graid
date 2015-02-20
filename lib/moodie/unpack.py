# Moodle Interface
# 
# Handles all data tasks associated with moodle including:
# 1. Unpacking a moodle .zip file download
# 2. Exporting a moodle ready gradebook

import os
from .runzip import runzip
from .sub_parser import parseSub

def unpack(moodle_zip_path):
    root_dir = runzip(moodle_zip_path)
    file_map = mapMoodleIdsToFiles(root_dir)
    normalizeDirectory(root_dir, file_map)

# Rearrange the files so all files are placed directly under
# a directory with the students moodle id as its name
def normalizeDirectory(root, file_map):
    # For each moodle id, create a new directory and move all 
    # the items in the list into that new directory, removing
    # any residual directories.

    for moodle_id in file_map:
        d = os.path.join(root, moodle_id)
        if not os.path.isdir(d):
            os.mkdir(d)
        for file_path in file_map[moodle_id]:
            f = file_path.split(getJoinStr())[-1]
            print('Adding', f, 'to', moodle_id)
            os.renames(file_path, os.path.join(root, moodle_id, f))

def mapMoodleIdsToFiles(directory):
    file_map = {}
    # Walk the directory
    for root, dirs, files in os.walk(directory):
    # For everything in the directory that has a moodleid in the 
    # name, add it to the list for that moodleid
        for f in files:
            info = parseSub(f)
            if info['moodleid'] != '':
                moodle_id = info['moodleid']
                if moodle_id not in file_map:
                    file_map[moodle_id] = []
                file_map[moodle_id].append(os.path.join(root, f))
        for d in dirs:
            info = parseSub(d)
            if info['moodleid'] != '':
                moodle_id = info['moodleid']
                if moodle_id not in file_map:
                    file_map[moodle_id] = []
                file_map[moodle_id].append(os.path.join(root, d))
    return file_map

def getJoinStr():
    return os.path.join('.','.')[1:-1]

