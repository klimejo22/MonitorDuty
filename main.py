import keyboard as kb


def viewMonitor():
    kb.press_and_release('v+i+e+w+space+m+o+n+i+t+o+r')

kb.add_hotkey('f', viewMonitor, suppress=True)
kb.wait()