# Hypixel Skyblock Farming Macro

This project is a **macro program** I desinged to automate the farming in Hypixel Skyblock. The script will work only for a specific setup in game. If you want to use this program for yourself, you would have to edit the [melon_macro](melon_macro.py) file or the [wheat_macro](wheat_macro.py) file by changing the loop function.

---

## Prerequisites

1. **Python 3.9+**: Ensure you have Python installed on your system.
2. **Dependencies**: Install required Python libraries using the following command:

   ```bash
   pip install pynput pyautogui
   ```
3. **Minecraft Client**: Ensure your Minecraft client is open and you are logged into Hypixel Skyblock.

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

4. Wait 2 seconds after starting the script for initialization.

### Stopping the Macro

- **Mouse**: Press the **X1 (side button)** on your mouse.
- **Keyboard**: Press the **`Y` key**.

Both actions will immediately stop the macro.

---

## Macro Descriptions

### MelonMacro

Automates the farming of melons with the following actions:
1. Executes a `/` command to re-enable movement.
2. Simulates mouse clicks to break melons.
3. Moves in a repetitive pattern:
   - Right
   - Forward
   - Left
   - Forward

### WheatMacro

Automates the farming of wheat with the following actions:
1. Executes the `/warp garden` command to ensure correct location.
2. Simulates mouse clicks to harvest wheat.
3. Moves in a repetitive pattern:
   - Back
   - Right
   - Forward

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

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Disclaimer

This project is intended for educational purposes only. The author does not endorse or encourage rule-breaking activities in any online game.

