import fnmatch, os

def rfind(pattern, directory, ignore=""):
    matches = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if fnmatch.fnmatch(f,pattern):
                path = os.path.abspath(os.path.join(root,f))
                if ignore:
                    if not ignore in path:
                        matches.append(path)
                else:
                    matches.append(path)
    return matches
