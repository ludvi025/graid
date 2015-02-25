from .menu import Menu

opts = 'PrintCode RunCode RunInteractive RunTests EnterGrade NextHW Back'

desc = [   
    'Print the code',
    'Run the code',
    'Run the code interactively',
    'Run the session tests',
    'Enter grade',
    'GoTo next homework',
    'Return to Main Menu',
]

helpme = [
'''Print the code to the console.''',

'''Run the student's code in a separate instance of python.''',

'''Open the student's code in an interactive python shell. 
Press Ctrl+D to return to script. Hint: Call `dir()` to see 
what's available.''',

'''Run the tests stored in the session against the student's code''',

'''Enter a grade and comments for the code before saving the finished 
grade file. Will then select the next file and enter this menu again.''',

'''Uhm... grade the next homework...''',

'''Go back to the Main Menu...''',
]

grade_menu = Menu(opts, desc, helpme, 'Grade Menu', decor='$')
