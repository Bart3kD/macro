import time
import sys
from pynput import mouse, keyboard

from melonMacro import MelonMacro
from wheatMacro import WheatMacro
from macro import Macro

def get_macro(macro_type: str) -> Macro:
    match macro_type:
        case "melon":
            return MelonMacro()
        case "wheat":
            return WheatMacro()
        case _:
            raise ValueError(f"Unknown macro type: {macro_type}")

def on_click(x, y, button, pressed):
    if button == mouse.Button.x1 and pressed:
        macro.stop()
        print("Macro stopped")

def on_press(key):
    try:
        if key.char == 'y':
            macro.stop()
            print("Macro stopped")
    except AttributeError:
        pass

def start_listeners():
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener.start()
    keyboard_listener.start()
    return mouse_listener, keyboard_listener

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <macro_type>")
        sys.exit(1)

    macro_type = sys.argv[1]
    global macro
    try:
        macro = get_macro(macro_type)
    except ValueError as e:
        print(e)
        sys.exit(1)

    mouse_listener, keyboard_listener = start_listeners()

    time.sleep(2)

    if macro_type == "melon":
        macro.loop(9, 8.7, 0.5)
    elif macro_type == "wheat":
        macro.loop(9, 15, 0.1)

    mouse_listener.stop()
    keyboard_listener.stop()

if __name__ == "__main__":
    main()
