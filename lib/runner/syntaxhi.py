# Syntax highlighting program for graid
# Bridger Herman 2015

# ANSI color codes
RED = "\x1b[1;31m"
GREEN = "\x1b[1;32m"
YELLOW = "\x1b[1;33m"
CYAN = "\x1b[1;36m"
END = "\x1b[0m"

# Is a string an official python keyword or an operator?
def is_keyword(s):
    s = str(s)
    keywords = ['and', 'as', 'assert', 'bool', 'break', 'chr', 'class',
    'continue', 'def', 'del', 'del', 'dict', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'int', 'input',
    'is', 'lambda', 'len', 'list', 'nonlocal', 'not', 'open', 'or', 'pass',
    'print', 'raise', 'return', 'set', 'str', 'try', 'while', 'with', 'yield']
    return s in keywords

# Is a string a value? (bool / number / None)
def is_value(s):
    s = str(s)
    values = ['False', 'None', 'True']
    return s in values or is_number(s)

# Is a string a number? (float / int)
def is_number(s):
    s = str(s)
    for c in s:
        if not c.isdigit() and c != "." and c != "\n":
            return False
    return True

# Is a string a string "with quotes around it?"
def is_string(s):
    if not s:
        return False
    s = str(s)
    s_chars = ['"', "'", '"""', "'''"]
    for c in s_chars:
        if s[0] == c and s[-1] == c or s[:3] in s_chars:
            return True
    return False

# Is a string a #comment?
def is_comment(s):
    s = str(s)
    if not s:
        return False
    if (s[0] == "#"):
        return True
    return False

# Syntax highlight a string using ANSI colors
def color_word(s):
    s = str(s)
    if is_value(s):
        return RED + s + END
    elif is_keyword(s):
        return YELLOW + s + END
    elif is_string(s):
        return GREEN + s + END
    elif is_comment(s):
        return CYAN + s + END
    else:
        return s

# List of words and symbols in a string
def words(s):
    s = str(s)
    separators = " ()[]{}+=-/*%&^|><,:;"
    s_chars = ["'",'"', '"""', "'''"]
    cur_s = '"'
    word_list = []
    in_string = False
    start = 0
    end = 1
    while end < len(s):
        if s[start:start + 3] in s_chars:
            cur_s = s[start:start + 3]
            in_string = True
        elif s[start] in s_chars:
            cur_s = s[start]
            in_string = True
        if not in_string:
            if s[end] in separators:
                word_list.append(s[start:end])
                start = end
            elif s[start] in separators:
                word_list.append(s[start])
                start += 1
        else:
            if (end + 3) < len(s) and s[end:end + 3] == cur_s:
                in_string = False
                word_list.append(s[start:end + 1])
                start = end + 1
            elif s[end] == cur_s:
                in_string = False
                word_list.append(s[start:end + 1])
                start = end + 1
        end += 1
    word_list.append(s[start:])
    return word_list

def mline_string(s):
    s = str(s)
    tquotes = s.count("'''") + s.count('"""')
    return tquotes == 1

# Colors a string of Python syntax
def color_line(line, mline_string = False):
    line = str(line)
    lwords = words(line)
    i = 0
    if not is_comment(line.lstrip()) and not mline_string:
        while i < len(lwords):
            # Comment out rest of line if it's a comment
            if is_comment(lwords[i]):
                lwords[i] = CYAN + lwords[i]
                lwords[len(lwords) - 1] += END
                i = len(lwords)
            else:
                lwords[i] = color_word(lwords[i])
                i += 1
        return "".join(lwords)
    elif mline_string:
        line = GREEN + line + END
    else:
        line = CYAN + line + END
    return line

if __name__ == '__main__':
    # Check to see if we're running linux (syntax highlighting only supports Linux terminals)
    import os
    linux = (os.name == "posix")
    fin = open("test.py",'r')
    contents = fin.readlines()
    fin.close()

    # If we are in a multi-line string
    in_string = False
    # Print out the code line-by-line
    for i in range(len(contents)):
        if linux:
            print(str(i + 1).rjust(4,' '),': ', color_line(contents[i], in_string), end = '')
            if mline_string(contents[i]):
                in_string = not in_string
        else:
            print(str(i + 1).rjust(4,' '),': ', contents[i], end = '')
