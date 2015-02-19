from .Menu import Menu

opts = 'RunTests RunShell ViewCode GradeCode PrintHelpText NextHomework'

desc = [   
    'Run the code',
    'Start a python shell',
    'Print the code',
    'Enter grades for the code',
    'Print help text',
    'Continue / Main Menu',
]

helpme = [
'''Run the homework code in a Python subprocess, optionally piping input if
so defined by the session file.''',

'''Open the student's code in an interactive python shell. Press Ctrl+D to 
return to script. Hint: Call `dir()` to see what's available.''',

'''Print the code to the console.''',

'''Enter a grade and comments for the code before saving the finished grade
file. Will then select the next file and enter this menu again.''',

'''Unsurprisingly, print this help text.''',

'''Uhm... grade the next homework...''',
]

grade_menu = Menu(opts, desc, helpme, 'Grade Menu', decor='$')
