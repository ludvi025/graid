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
    def __init__(_, maxpoints=float('inf')):
        _.maxpoints = maxpoints

    def get(_):
        grade = -1
        while (grade > _.maxpoints) or (grade < 0):
            try:
                grade = float(input('Enter points: '))
                if grade < 0:
                    print("Invalid points.")
            except ValueError:
                print("Invalid points.")
        return grade

class FilePath:
    def __init__(_, must_exist=False, must_not_exist=False):
        _.must_exist = must_exist
        _.must_not_exist = must_not_exist

    def get(_):
        if _.must_exist:
            exists = False
            while not exists:
                file_path = input("Enter path to file: ")
                file_path = path.abspath(file_path)
                if path.exists(file_path):
                    exists = True
                else:
                    print('Error, file does not exist...')

        elif _.must_not_exist:
            exists = True
            while exists:
                file_path = input("Enter path to file: ")
                file_path = path.abspath(file_path)
                if path.exists(file_path):
                    print('Error, file already exists...')
                else:
                    exists = False

        else:
            file_path = input("Enter path to file: ")
            file_path = path.abspath(file_path)

        return file_path


