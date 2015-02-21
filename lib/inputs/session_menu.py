from .menu import Menu

opts = 'Create Load Edit Save Back'

desc = [   
    'Create a new session',
    'Load a session from a file',
    'Edit the current session',
    'Save the current session',
    'Return to Main Menu',
]

helpme = [
'''Input session info: patterns to match for finding homework,
maximum points, paths to tests, etc.''',

'''Load a pre-created session file from file.''',

'''Edit the currently loaded session.''',

'''Save the current session to file.''',

'''Go back to the Main Menu...''',
]

session_menu = Menu(opts, desc, helpme, 'Session Manager', decor='+')
