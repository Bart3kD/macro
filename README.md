# Hypixel Skyblock Farming Macro

This project is a **macro program** I desinged to automate the farming in Hypixel Skyblock. The script will work only for a specific setup in game. If you want to use this program for yourself, you would have to edit the [melon_macro](melon_macro.py) file or the [wheat_macro](wheat_macro.py) file by changing the loop function.

---

## Prerequisites

1. **Python 3.9+**: Ensure you have Python installed on your system.
2. **Dependencies**: Install required Python libraries using the following command:

   ```bash
   pip install pynput pyautogui
   ```

---

## Usage

### Running the Program

1. Clone the repository or download the files.
2. Open a terminal in the project directory.
3. Run the script with the following command:

   ```bash
   python main.py <macro_type>
   ```

   Replace `<macro_type>` with:
   - `melon` for MelonMacro
   - `wheat` for WheatMacro

   Example:

   ```bash
   python main.py melon
   ```

4. You have 2 seconds to open the minecraft tab and then the macro starts.

### Stopping the Macro

- **Mouse**: Press the **X1 (side button)** on your mouse.
- **Keyboard**: Press the **`Y` key**.

Both actions will immediately stop the macro.

---

## File Structure

### `main.py`
- Entry point for the program.
- Handles command-line arguments and user input.

### `macro.py`
- Abstract base class defining shared functionality for all macros.

### `melon_macro.py`
- Implements the `MelonMacro` logic.

### `wheat_macro.py`
- Implements the `WheatMacro` logic.

---

## Safety Note

Hypixel enforces strict rules against automation and macros. Use this program responsibly and at your own risk.

---

## Disclaimer

This project is intended for educational purposes only. I do not endorse or encourage rule-breaking activities in any online game.

