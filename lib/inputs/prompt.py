# TODO: Split this file up

from random import randint
from os import path

class YesNo:
    yesses = ['y', 'yes', 'yep', 'yeah']

    def __init__(_, prompt):
        _.prompt = prompt

    def get(_):
        result = input(_.prompt + ' (y/n): ')
        return result.lower() in YesNo.yesses

class Points:
    def __init__(_, maxpoints=float('inf'), accept_empty=False):
        _.maxpoints = maxpoints
        _.accept_empty = accept_empty

    def get(_):
        while True:
            try:
                grade = input('Enter points: ')
                if grade == '' and _.accept_empty:
                    return grade
                else:
                    grade = float(grade)
                    if grade < 0:
                        print("Grade must be positive.")
                    elif grade > _.maxpoints:
                        print("Max points are {}".format(_.maxpoints))
                    else:
                        return grade
            except ValueError:
                print("Invalid points.")

class PressEnter:
    def __init__(_, msg):
        _.msg = msg

    def get(_):
        input('{} [Press Enter]'.format(_.msg))

class Path:
    def __init__(_, msg, validator, accept_empty=False, must_exist=False, must_not_exist=False):
        _.validator = validator
        _.msg = msg
        _.accept_empty = accept_empty
        _.must_exist = must_exist
        _.must_not_exist = must_not_exist

    def get(_):
        if _.must_exist:
            exists = False
            while not exists:
                file_path = input(_.msg)
                if _.accept_empty and file_path == '':
                    exists = True
                else:
                    file_path = path.abspath(file_path)
                    if _.validator(file_path):
                        exists = True
                    else:
                        print('Error, path does not exist...')

        elif _.must_not_exist:
            exists = True
            while exists:
                file_path = input(_.msg)
                if _.accept_empty and file_path == '':
                    exists = False
                else:
                    file_path = path.abspath(file_path)
                    if _.validator(file_path):
                        print('Error, path already exists...')
                    else:
                        exists = False

        else:
            file_path = input("Enter path to file: ")
            file_path = path.abspath(file_path)

        return file_path

class FilePath(Path):
    def __init__(_, msg, accept_empty=False, must_exist=False, must_not_exist=False):
        super().__init__(msg, path.isfile, accept_empty, must_exist, must_not_exist)

class DirPath(Path):
    def __init__(_, msg, accept_empty=False, must_exist=False, must_not_exist=False):
        super().__init__(msg, path.isdir, accept_empty, must_exist, must_not_exist)
