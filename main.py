import keyboard as kb
from pynput import mouse

# def on_click(x, y, button, pressed):
#     if pressed:
#         if button == mouse.Button.x1:
#             print("Mouse 4 / Back button")
#         elif button == mouse.Button.x2:
#             print("Mouse 5 / Forward button")

# Doplnkovy fce
def enter():
    kb.press_and_release('enter')
def printStatus(status):
    if status:
        return "ON"
    
    return "OFF"

def viewMonitor():
    kb.press_and_release('v+i+e+w+space+m+o+n+i+t+o+r')
    enter()
def switch():
    kb.press_and_release('s+w+i+t+c+h')
    enter()
def transmit():
    kb.press_and_release('t+r+a+n+s+m+i+t')
def moons():
    kb.press_and_release('m+o+o+n+s')
    enter()
def assurance():
    kb.press_and_release("a+s+s")
    enter()
    kb.press_and_release("c")
    for i in range(20):
        print("[INFO]: Assurance pressed")
        enter()
def vow():
    kb.press_and_release("v+o+w")
    enter()
    kb.press_and_release("c")
    for i in range(20):
        print("[INFO]: " + "Vow pressed")
        enter()
def adamance():
    kb.press_and_release("a+d+a")
    enter()
    kb.press_and_release("c")
    for i in range(20):
        print("[INFO]: " + "Adamance pressed")
        enter()
def dine():
    kb.press_and_release("d+i+n+e")
    enter()
    kb.press_and_release("c")
    for i in range(20):
        print("[INFO]: " + "Dine pressed")
        enter()

kb.add_hotkey('r', viewMonitor, suppress=True)
kb.add_hotkey('f', switch, suppress=True)
kb.add_hotkey('q', transmit, suppress=True)

kb.add_hotkey('m', moons, suppress=True)
kb.add_hotkey('1', assurance, suppress=True)
kb.add_hotkey('2', vow, suppress=True)
kb.add_hotkey('3', adamance, suppress=True)
kb.add_hotkey('4', dine, suppress=True)

print("=== Monitor Duty ON ===")

mouse_controller = mouse.Controller()
AutoAttack = False
def on_press(key):
    try:
        if key.char == 'x':
            AutoAttack = not AutoAttack
            print("[INFO]: AutoAttack mode " + printStatus(AutoAttack))
            while(AutoAttack):
                mouse_controller.click(mouse.Button.left, 1)
            
    except AttributeError:
        pass
# with kb.Listener(on_press=on_press) as listener:
#     listener.join()
kb.wait()
