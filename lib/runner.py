import os

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

class Runner:

    def __init__(_, file_path):
        _.file_path = file_path

    # Display the contents of the student's homework file
    # for manual inspection and partial credit. Displays 
    # with line numbers for easy reference.
    def printCode(_):
        print(print_src_msg)

        try:
            fin = open(file_path,'r')
            contents = fin.readlines()
            fin.close()

            for i in range(len(contents)):
                print(str(i+1).rjust(4,' '),': ', contents[i], end='')
            print()
        except:
            print('Failed to open file: {}\n'.format(_.file_path))

    def runCode(_, interactive=False):
        print(run_in_interpreter_msg)

        # Store current directory so we can switch back to it
        current_dir = os.getcwd()

        file_dir, file_name = os.path.split(_.file_path)
        os.chdir(file_dir)

        # TODO: Ctrl+C handler

        # Call the student code
        if interactive:
            subprocess.call([sys.executable, '-i', file_name])
        else:
            subprocess.call([sys.executable, file_name])

        # Return to original directory
        os.chdir(current_dir)

    def runInteractive(_):
        _.runCode(interactive=True)

    def runTests(_):
        print('Not yet implemented')
