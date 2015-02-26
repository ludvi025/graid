from .menu import Menu

#opts = 'GradeHomeworks CheckGradeFiles GradingStatistics ConsolidateGrades ' + \
#       'PrintHelpText TerminateProgram' 
opts = 'ManageSession Grade Admin Quit'

desc = [   
    'Manage session',
    'Grade homework',
    'Admin',
    'Exit Graid',
]

helpme = [
'''Manage grading sessions including file patterns to match and 
tests to run.''',

'''Grade individual homework submissions. If you're an undergraduate TA,
this is all you only need to go here.''',

'''Administrative functions to be run before and after grading.''',

'''Cleanly exit the Graid.''',
]

main_menu = Menu(opts, desc, helpme, 'Main Menu')
