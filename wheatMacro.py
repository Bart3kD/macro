import pyautogui

from macro import Macro

class WheatMacro(Macro):
    def loop(self, rep: int, sd: float, fd: float) -> None:
        pattern = [
            ("back", sd),
            ("right", fd),
            ("forward", sd - 1),
        ]

        while self.running:
            
            if not self.running:
                break

            if self.running:
                pyautogui.typewrite("/")
                pyautogui.typewrite("warp garden")
                pyautogui.press("enter")
            
            pyautogui.mouseDown()

            if self.running:
                self.move("forward", sd + 0.2)

            for _ in range(rep):
                if not self.running:
                    break
                for direction, duration in pattern:
                    if not self.running:
                        break
                    self.move(direction, duration)

            if self.running:
                self.move("back", sd)

            pyautogui.mouseUp()