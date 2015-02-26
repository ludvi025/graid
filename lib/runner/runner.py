import os
import subprocess
import sys
from ..debug import dbprint, db_exec_info


from .tester import runWithInput

# TODO: Handle infinite loops

print_src_msg = '''
+------------------------+
| Printing File Contents |
+------------------------+
'''

run_in_interpreter_msg = '''
+------------------------------+
| Launching Python Interpreter |
|  (Press Ctrl+D to quit...)   |
+------------------------------+    
'''

run_tests_msg = '''
+---------------------------+
| Calling Tests For Session |
+---------------------------+
'''

# Display the contents of the student's homework file
# for manual inspection and partial credit. Displays 
# with line numbers for easy reference.
def printCode(file_path):
    print(print_src_msg)

    try:
        fin = open(file_path,'r')
        contents = list(fin)
        fin.close()

        while contents[-1] == '\n' and len(contents) > 0:
            contents.pop()

        for i in range(len(contents)):
            print(str(i+1).rjust(4,' '),': ', contents[i], end='')
        print()
    except:
        print('Failed to open file: {}\n'.format(file_path))
        dbprint(db_exec_info())

def runCode(file_path, interactive=False):

    # Store current directory so we can switch back to it
    current_dir = os.getcwd()

    file_dir, file_name = os.path.split(file_path)
    os.chdir(file_dir)

    # TODO: Ctrl+C handler

    # Call the student code
    if interactive:
        subprocess.call([sys.executable, '-i', file_name])
    else:
        subprocess.call([sys.executable, file_name])

    # Return to original directory
    os.chdir(current_dir)

def runInteractive(file_path):
    print(run_in_interpreter_msg)
    runCode(file_path, interactive=True)

def runTests(file_path, test):
    print(run_tests_msg)
    mod_load_error = False
    out, err = runWithInput(file_path, open(test).read())
    if out:
        out = out.replace('>>>','\n').replace('...','\n')
    if err:
        err = err.replace('>>>','\n').replace('...','\n')
    print('Output from', test, '\n------')
    print(out)
    if not err.replace('\n','').replace(' ','')=='':
        print('Errors from', test, '\n------')
        print(err)
