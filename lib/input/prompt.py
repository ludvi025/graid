from random import randint

class YesNo:
    yesses = ['y', 'yes', 'yep', 'yeah']

    def __init__(_, prompt):
        _.prompt = prompt


    def get(_):
        result = input(_.prompt + ' (y/n): ')
        return result.lower() in YesNo.yesses

class Grade:
    def __init__(_, maxpoints=float('inf')):
        _.maxpoints = maxpoints

    def get(_):
        grade = -1
        while (grade > _.maxpoints) or (grade < 0):
            try:
                grade = float(input('Enter grade: '))
                if grade < 0:
                    print("Not a valid grade.")
            except ValueError:
                print("Not a valid grade.")
        return grade
