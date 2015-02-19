import lib.sessions

sm = lib.sessions.SessionManager()

ss = sm.loadSession('test')

print(ss)
