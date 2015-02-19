import zipfile as z
import os

def removeExt(zip_path):
    return '.'.join(zip_path.split('.')[0:-1])

# Unzip all files at file_path, recursively
def runzip(file_path, delete=False):
    if os.path.isdir(file_path):
        for file_name in os.listdir(file_path):
            sub_path = os.path.join(file_path, file_name)
            runzip(sub_path)

        return file_path

    elif z.is_zipfile(file_path):
        unzipped_path = removeExt(file_path)
        print("unzipping:", file_path)
        os.mkdir(unzipped_path)

        z.ZipFile(file_path).extractall(unzipped_path)

        if delete:
            os.remove(file_path)

        for file_name in os.listdir(unzipped_path):
            sub_path = os.path.join(unzipped_path, file_name)
            runzip(sub_path, delete=True)

        return unzipped_path
