from abc import ABC, abstractmethod
import pyautogui
import time

class Macro(ABC):
    def __init__(self) -> None:
        super().__init__()
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

    @abstractmethod
    def loop(self, rep: int, sd: float, fd: float) -> None:
        ...
    
    def stop(self):
        """Stop the macro."""
        self.running = False
        pyautogui.keyUp("W")
        pyautogui.keyUp("D")
        pyautogui.keyUp("A")
        pyautogui.keyUp("S")
        pyautogui.mouseUp()