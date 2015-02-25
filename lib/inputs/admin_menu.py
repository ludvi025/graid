from .menu import Menu

opts = 'Unpack Export Stats Verify Back'

desc = [   
    'Unpack *.zip',
    'Export gradebook',
    'Show homework stats',
    'Verify all graded',
    'Return to Main Menu',
]

helpme = [
'''Unpack a moodle *.zip homework download for grading.''',

'''Export all grades to a CSV ready for uploading to moodle.''',

'''Print out some useful statistics about the homework grades.''',

'''Verify that all homework submissions have been graded.''',

'''Go back to the Main Menu...''',
]

admin_menu = Menu(opts, desc, helpme, 'Admin Menu', decor='!')
