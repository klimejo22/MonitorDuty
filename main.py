import keyboard as kb


def on_press():
    # simulace stisku více kláves najednou (např. Ctrl + C)
    kb.press_and_release('ctrl+c')

kb.add_hotkey('f', on_press)
