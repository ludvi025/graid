from lib.inputs import main_menu, grade_menu, session_menu, admin_menu
from lib.debug import dbprint

dbprint('Running with debug statements...')

main_actions = {
    main_menu.options.ManageSession: lambda: session_menu.loop(session_actions),
    main_menu.options.Grade: lambda: grade_menu.loop(grade_actions),
    main_menu.options.Admin: lambda: admin_menu.loop(admin_actions),
    main_menu.options.Quit: lambda: True,
}

session_actions = {
    session_menu.options.Back: lambda: True
}

grade_actions = {
    grade_menu.options.Back: lambda: True
}

admin_actions = {
    admin_menu.options.Back: lambda: True
}

main_menu.loop(main_actions)
