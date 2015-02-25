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
#helpme = [
#'''Enter the grade homework assignment menu, after passing verification
#that there are still homeworks that need grading.''',
#
#'''Enter the check grade files menu to cleanup any grade files
#corresponding to unfinished or in progress grading.''',
#
#'''Show some grading statistics. Will compute average grade, number graded
#per grader, average grade per grader, and maybe even grading rate. Note
#that this may be slow as it will compute the statistics upon calling and
#not continually in the background.''',
#
#'''The graduate TA part of the job that consolidates all the individual
#grade files into one large CSV.''',
#
#'''Unsurprisingly, print this help text.''',
#
#'''A way to cleanly exit the grading script. This is much preferred to
#mashing Ctrl-C like a monkey with a bone after encountering a monolith.''',
#]

main_menu = Menu(opts, desc, helpme, 'Main Menu')
