# Menu Interface
#
# Deliver custom intuitive interfaces

from enum import Enum

class Menu:
# options : A space-separated string of menu options (or a list)
# short   : An ordered list of explanations
# helpme  : An ordered list of longer explanations
# name    : (opt) The name of the menu to print
# decor   : (opt) The decoration to print around the menu

    def __init__(_, options, short, helpme, name='Menu', decor='#'):
        _.options = Enum('_.options', options)
        _.short = short
        _.helpme = helpme
        _.name = name
        _.decor = decor

    def __print(_, decor, descriptions):
        print()
        print(decor * 80)
        print(decor + _.name.center(78) + decor)
        print(decor * 80)
        for i in range(len(_.options)):
            first = True
            for line in descriptions[i].split('\n'):
                if first:
                    p = decor + str(i+1).rjust(3) + ' : ' + line.ljust(72) + decor
                    first = False
                else:
                    p = decor + ' '*6 + line.ljust(72) + decor
                print(p)

        print(decor * 80)
        print()

    def print(_):
        _.__print(_.decor, _.short)

    def print_help(_):
        Menu.__print('?', _.name + 'Help', _.options, _.helpme)

    def get_option(_):
        opt = None
        while True:
            try:
                opt = int(input("Select an option: "))
                opt = _.options(opt) # Converts alias to enum
                break
            except:
                print("Invalid option.")
        return opt


