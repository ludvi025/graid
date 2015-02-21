from enum import Enum

LINE_LEN = 78

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
        print(decor * LINE_LEN)
        print(decor + _.name.center(LINE_LEN - 2) + decor)
        print(decor * LINE_LEN)
        for i in range(len(_.options)):
            first = True
            for line in descriptions[i].split('\n'):
                if first:
                    p = decor + str(i+1).rjust(3) + ' : ' \
                              + line.ljust(LINE_LEN - 8) + decor
                    first = False
                else:
                    p = decor + ' '*6 + line.ljust(LINE_LEN - 8) + decor
                print(p)

        print(' Enter ? For Help '.center(LINE_LEN, decor))
        print()

    def print(_):
        _.__print(_.decor, _.short)

    def print_help(_):
        _.__print('?', _.helpme)

    def get_option(_):
        _.print()
        opt = None
        while not opt:
            opt = input("Select an option: ")
            if opt == '?':
                _.print_help()
                opt = None
            else:
                try:
                    opt = _.options(int(opt)) # Converts alias to enum
                except:
                    print("Invalid option.")

        return opt

    def loop(_, actions):
        done = False
        while not done:
            option = _.get_option()
            if option in actions:
                done = actions[option]()
            else:
                print('Not implemented')

        return False
