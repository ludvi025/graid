from random import randint

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
