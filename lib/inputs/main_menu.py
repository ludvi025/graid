from .menu import Menu

opts = 'GradeHomeworks CheckGradeFiles GradingStatistics ConsolidateGrades ' + \
       'PrintHelpText TerminateProgram' 

desc = [   
    'Go to grading homeworks',
    'Go to checking grade files',
    'Compute some statistics',
    'Consolidate grade files',
    'Print help text',
    'Cleanly exit this script',
]

helpme = [
'''Enter the grade homework assignment menu, after passing verification
that there are still homeworks that need grading.''',

'''Enter the check grade files menu to cleanup any grade files
corresponding to unfinished or in progress grading.''',

'''Show some grading statistics. Will compute average grade, number graded
per grader, average grade per grader, and maybe even grading rate. Note
that this may be slow as it will compute the statistics upon calling and
not continually in the background.''',

'''The graduate TA part of the job that consolidates all the individual
grade files into one large CSV.''',

'''Unsurprisingly, print this help text.''',

'''A way to cleanly exit the grading script. This is much preferred to
mashing Ctrl-C like a monkey with a bone after encountering a monolith.''',
]

main_menu = Menu(opts, desc, helpme, 'Main Menu')
