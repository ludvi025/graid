import os
from ..tools import runzip, parseSub

FILE_TEXT_TO_REMOVE = ['_assignsubmission_file']

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
        # Create new directories named with the moodle submission
        directory = os.path.join(root, moodle_id)
        if not os.path.isdir(directory):
            os.mkdir(directory)

        # Move all files into new directories
        for file_path in file_map[moodle_id]:
            old_name = os.path.basename(file_path)
            # Remove common text and spaces
            new_name = removeCommonText(old_name).replace(' ', '')
            new_path = os.path.join(moodle_id, new_name)
            print('Moving', old_name, 'to', new_path)
            os.renames(file_path, os.path.join(root, new_path))

def removeCommonText(file_path):
    for text in FILE_TEXT_TO_REMOVE:
        file_path = file_path.replace(text, '')
    return file_path

def mapMoodleIdsToFiles(directory):
# Creates a map of all the files that belong to a particular 
# moodle submission

    file_map = {}

    # Walk the directory
    for root, dirs, files in os.walk(directory):

        # For everything in the directory that has a moodle_id in the 
        # name, add it to the list for that moodle_id
        for f in files:
            info = parseSub(f)

            if info['moodle_id'] != '':
                moodle_id = info['moodle_id']

                if moodle_id not in file_map:
                    file_map[moodle_id] = []

                file_map[moodle_id].append(os.path.join(root, f))

        for d in dirs:
            info = parseSub(d)
            if info['moodle_id'] != '':
                moodle_id = info['moodle_id']

                if moodle_id not in file_map:
                    file_map[moodle_id] = []

                file_map[moodle_id].append(os.path.join(root, d))

    return file_map
