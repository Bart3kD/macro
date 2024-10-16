import pyautogui

from macro import Macro

class MelonMacro(Macro):
    def loop(self, rep: int, sd: float, fd: float) -> None:
        pattern = [
            ("right", sd),
            ("forward", fd),
            ("left", sd),
            ("forward", fd),
        ]

        while self.running:
            
            if not self.running:
                break

            if self.running:
                pyautogui.typewrite("/")
                pyautogui.press("up")
                pyautogui.press("enter")

            pyautogui.mouseDown()

            for _ in range(rep):
                if not self.running:
                    break
                for direction, duration in pattern:
                    if not self.running:
                        break
                    self.move(direction, duration)

            if self.running:
                self.move("right", sd)

            pyautogui.mouseUp()