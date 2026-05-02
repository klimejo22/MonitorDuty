import keyboard as kb


def viewMonitor():
    kb.press_and_release('v+i+e+w+space+m+o+n+i+t+o+r')
def switch():
    kb.press_and_release('s+w+i+t+c+h')
def transmit():
    kb.press_and_release('t+r+a+n+s+m+i+t')

kb.add_hotkey('r', viewMonitor, suppress=True)
kb.add_hotkey('f', switch, suppress=True)
kb.add_hotkey('q', transmit, suppress=True)

kb.wait()