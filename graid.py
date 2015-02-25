from lib.inputs import main_menu, grade_menu, session_menu, admin_menu
from lib.inputs import PressEnter, FilePath, InputRecord
from lib.sessions import SessionManager
from lib.moodie import unpack, exportGradebook 
from lib.gradebook import Gradebook
from lib.pool import Pool
from lib.runner import printCode, runCode, runInteractive, runTests
from lib.debug import dbprint

# TODO: Add changing root directory
# TODO: Structue in a singleton object instead of using global

dbprint('Running with debug statements...')

session = None
session_manager = SessionManager()

menus_lst=[main_menu, admin_menu, grade_menu, session_menu]

hw_pool = None
current_hw = None

def main():
    main_menu.loop(main_actions)

# Main Menu Callbacks
def session_loop():
    session_menu.loop(session_actions)
    return False

def grade_loop():
    global session, hw_pool, current_hw
    if session == None:
        session_load()
    
    if hw_pool == None:
        hw_pool = Pool(session.patterns, session.hw_dir, session.name)

    current_hw = hw_pool.getNextHW()
    if current_hw == None:
        dbprint('here')
        hw_pool.recheckAll()
        current_hw = hw_pool.getNextHW()
        if current_hw == None:
            in_progress = hw_pool.getStatusCounts()['in progress']
            msg = 'No homeworks left for you, ' \
                + 'but {} still in progress.'.format(in_progress)
            PressEnter(msg).get()
        else:
            current_hw.setStatus('in progress')
            grade_menu.loop(grade_actions)
    else:
        current_hw.setStatus('in progress')
        grade_menu.loop(grade_actions)
    return False

def admin_loop():
    admin_menu.loop(admin_actions)
    return False

main_actions = {
    main_menu.options.ManageSession:  session_loop,
    main_menu.options.Grade:          grade_loop,
    main_menu.options.Admin:          admin_loop,
    main_menu.options.Quit:           lambda: True,
}

# Grade Menu Callbacks
def grade_print_code():
    global current_hw
    printCode(current_hw.file_path)
    return False

def grade_run_code():
    global current_hw
    runCode(current_hw.file_path)
    return False

def grade_run_interactive():
    global current_hw
    runInteractive(current_hw.file_path)
    return False

def grade_run_tests():
    global current_hw, session
    runTests(current_hw.file_path, session.test)
    return False

def grade_enter_grade():
    global current_hw
    record = InputRecord(session.points).get(current_hw.getStudentInfo())
    if record.toFile(session.name, current_hw.getFileDir()):
        current_hw.setStatus('graded')
    else:
        PressEnter('Failed to record grade.').get()
    return False

def grade_next_hw():
    global current_hw, hw_pool
    if current_hw.getStatus() == 'graded':
        current_hw = hw_pool.getNextHW()
        if current_hw != None:
            current_hw.setStatus('in progress')
            return False
        else:
            hw_pool.recheckAll()
            current_hw = hw_pool.getNextHW()
            if current_hw == None:
                PressEnter('No homework left to grade!').get()
                return True
            else:
                current_hw.setStatus('in progress')
                return False
    else:
        PressEnter('Finish grading this homework first.').get()
        return False

def grade_back():
    if current_hw.getStatus() != 'graded':
        current_hw.setStatus('not started')
    return True


grade_actions = {
    grade_menu.options.PrintCode:      grade_print_code,
    grade_menu.options.RunCode:        grade_run_code,
    grade_menu.options.RunInteractive: grade_run_interactive,
    grade_menu.options.RunTests:       grade_run_tests,
    grade_menu.options.EnterGrade:     grade_enter_grade,
    grade_menu.options.NextHW:         grade_next_hw,
    grade_menu.options.Back:           grade_back,
}

# Admin Menu Callbacks
def admin_unpack():
    fp = FilePath('Enter path to *.zip: ', must_exist=True) 
    moodle_zip_path = fp.get()
    unpack(moodle_zip_path)
    return False

def admin_export():
    if session == None:
        session_load()
    gb = Gradebook.fromFiles(session.name + '.grade', session.hw_dir)
    fp1 = FilePath('Enter output file path: ', must_not_exist=True)
    file_path = fp1.get()
    fp2 = FilePath('Enter path to user id map: ', \
                   must_exist=True, accept_empty=True)
    user_ids_map = fp2.get()

    exportGradebook(gb, file_path, user_ids_map)
    return False
    
def admin_stats():
    dbprint('Not implemented.')
    return False

def admin_verify():
    global hw_pool
    if session == None:
        session_load()

    if hw_pool == None:
        hw_pool = Pool(session.patterns, session.hw_dir, session.name)

    count = hw_pool.clearInProgress()
    msg = '{} were still in progress and were reset'.format(count)
    PressEnter(msg).get()
    
    return False

admin_actions = {
    admin_menu.options.Unpack: admin_unpack,
    admin_menu.options.Export: admin_export,
    admin_menu.options.Stats:  admin_stats,
    admin_menu.options.Verify: admin_verify,
    admin_menu.options.Back:   lambda: True,
}

# Session Menu Callbacks
def session_create():
    global session, session_manager
    session = session_manager.createSession()
    return False

def session_load():
    # TODO: Add error message for bad load
    global session, session_manager
    if session == None:
        session = session_manager.loadSession()
        while session == None:
            print('Error, session not found.')
            session = session_manager.loadSession()
        add_session_name()
    else:
        new_session = session_manager.loadSession()
        if new_session != None:
            session = new_session
            add_session_name()
        else:
            PressEnter('Failed to load new session.').get()
    return False

def session_edit():
    global session, session_manager
    dbprint(session)
    session_manager.editSession(session)
    return False

def session_save():
    global session, session_manager
    session_manager.saveSession(session)
    return False

def add_session_name():
    global session, menus_lst
    n=session.name
    for i in menus_lst:
        if ':' in i.name:
            i.name=(i.name.split(':')[0])+":  "+n
        else:
            i.name=i.name+":  "+n
    

session_actions = {
    session_menu.options.Create: session_create,
    session_menu.options.Load:   session_load,
    session_menu.options.Edit:   session_edit,
    session_menu.options.Save:   session_save,
    session_menu.options.Back:   lambda: True,
}

if __name__ == '__main__':
    main()
