import pyautogui
import time
from pynput import mouse

class Macro:
    def __init__(self):
        self.running = True

    def move(self, direction: str, duration: float) -> None:
        """Perform a key press in the given direction for a specified duration."""
        keys = {
            "left": "A",
            "right": "D",
            "forward": "W",
            "back": "S"
        }
        key = keys.get(direction, "W")
        pyautogui.keyDown(key)
        time.sleep(duration)
        pyautogui.keyUp(key)

    def melon_loop(self, repetitions: int = 9, forward_duration: float = 0.5, side_duration: float = 8.7) -> None:
        movement_pattern = [
            ("right", side_duration),
            ("forward", forward_duration),
            ("left", side_duration),
            ("forward", forward_duration),
        ]

        while self.running:
            
            if not self.running:
                break

            if self.running:
                pyautogui.typewrite("/")
                pyautogui.press("up")
                pyautogui.press("enter")

            pyautogui.mouseDown()

            for _ in range(repetitions):
                if not self.running:
                    break
                for direction, duration in movement_pattern:
                    if not self.running:
                        break
                    self.move(direction, duration)

            if self.running:
                self.move("right", side_duration)

            pyautogui.mouseUp()
        
    def wheat_loop(self, repetitions: int=11, forward_duration: float = 0.5, side_duration: float = 15) -> None:
        movement_pattern = [
            ("back", side_duration),
            ("right", 0.1),
            ("forward", side_duration - 1),
        ]

        while self.running:
            
            if not self.running:
                break

            if self.running:
                pyautogui.typewrite("/")
                pyautogui.press("up")
                pyautogui.press("enter")
            
            pyautogui.mouseDown()

            if self.running:
                self.move("forward", side_duration + 0.2)

            for _ in range(repetitions):
                if not self.running:
                    break
                for direction, duration in movement_pattern:
                    if not self.running:
                        break
                    self.move(direction, duration)

            if self.running:
                self.move("back", side_duration)

            pyautogui.mouseUp()


    def stop(self):
        """Stop the macro."""
        self.running = False
        pyautogui.keyUp("W")
        pyautogui.keyUp("D")
        pyautogui.keyUp("A")
        pyautogui.keyUp("S")
        pyautogui.mouseUp()


def on_click(x, y, button, pressed):
    if button == mouse.Button.x1 and pressed:
        macro.stop()
        print("Macro stopped")


macro = Macro()

listener = mouse.Listener(on_click=on_click)
listener.start()

time.sleep(2)

macro.wheat_loop()

listener.stop()
