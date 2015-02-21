from sys import argv
from lib.inputs import main_menu, grade_menu, session_menu, admin_menu

# Use dbprint to add print statements that only print if
# graid.py called with debug as a command line argument
debug = 'debug' in argv
dbprint = print if debug else lambda *args, **kwargs: None

main_choice = None
while main_choice != main_menu.options.Quit:
    main_choice = main_menu.get_option()

    if main_choice == main_menu.options.ManageSession:
        session_choice = None
        while session_choice != session_menu.options.Back:
            session_choice = session_menu.get_option()
            dbprint(session_choice)

    if main_choice == main_menu.options.Grade:
        grade_choice = None
        while grade_choice != grade_menu.options.Back:
            grade_choice = grade_menu.get_option()
            dbprint(grade_choice)

    if main_choice == main_menu.options.Admin:
        admin_choice = None
        while admin_choice != admin_menu.options.Back:
            admin_choice = admin_menu.get_option()
            dbprint(admin_choice)

    dbprint(main_choice)
