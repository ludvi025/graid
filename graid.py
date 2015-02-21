from lib.inputs import main_menu, grade_menu, session_menu, admin_menu, FilePath
from lib.sessions import SessionManager
from lib.moodie import unpack, exportGradebook 
from lib.gradebook import Gradebook
from lib.debug import dbprint

# TODO: Add changing root directory
# TODO: Structue in a singleton object instead of using global

dbprint('Running with debug statements...')

session = None
session_manager = SessionManager()

def main():
    main_actions = {
        main_menu.options.ManageSession:  lambda: session_menu.loop(session_actions),
        main_menu.options.Grade:          lambda: grade_menu.loop(grade_actions),
        main_menu.options.Admin:          lambda: admin_menu.loop(admin_actions),
        main_menu.options.Quit:           lambda: True,
    }

    session_actions = {
        session_menu.options.Create:  session_create,
        session_menu.options.Load:    session_load,
        session_menu.options.Edit:    session_edit,
        session_menu.options.Save:    session_save,
        session_menu.options.Back:    lambda: True,
    }

    grade_actions = {
        grade_menu.options.Back: lambda: True
    }

    admin_actions = {
        admin_menu.options.Unpack:  admin_unpack,
        admin_menu.options.Export:  admin_export,
        admin_menu.options.Stats:   admin_stats,
        admin_menu.options.Verify:  admin_verify,
        admin_menu.options.Back:    lambda: True,
    }

    main_menu.loop(main_actions)

# Admin Menu Callbacks
def admin_unpack():
    fp = FilePath('Enter path to *.zip: ', must_exist=True) 
    moodle_zip_pah = fp.get()
    unpack(moodle_zip_path)
    return False

def admin_export():
    gb = Gradebook.fromFiles(session.name + '.grade') # add root_dir
    exportGradebook(gb)
    return False
    
def admin_stats():
    dbprint('Not implemented.')
    return False

def admin_verify():
    dbprint('Not implemented.')
    return False

# Session Menu Callbacks
def session_create():
    global session, session_manager
    session = session_manager.createSession()
    return False

def session_load():
    global session, session_manager
    session = session_manager.loadSession()
    return False

session_edit = session_create

def session_save():
    global session, session_manager
    session_manager.saveSession(session)
    return False

if __name__ == '__main__':
    main()
