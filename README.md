# Away From Keyboard (AFK Bot)

AFK Bot is a lightweight macOS menu bar application designed to simulate user activity by periodically moving the mouse and performing occasional clicks. This tool ensures that your computer remains active, preventing screensavers, sleep mode, or idle timeouts.

## Features
- Minimalistic macOS menu bar integration.
- Start/Stop functionality with dynamic control.
- Periodic mouse movements to random positions on the screen.
- Optional occasional clicks to mimic real activity.
- Customizable time intervals for actions.

## Technology Stack
- **Python**: Core logic and implementation.
- **rumps**: For seamless macOS menu bar integration.
- **pyautogui**: For simulating mouse movements and clicks.
- **PyInstaller**: To package the application into a standalone `.app`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/krohmos/afk-bot.git
   cd afk-bot
   ```
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
1. Run the app:
   ```bash
   python app.py
   ```

## Building the app
To build a standalone macOs .app:
1. Install pyinstaller:
   ```bash
   pip install pyinstaller
   ```
1. Build the app:
   ```bash
   sh build.sh
   ```
The .app will be available in the dist/ folder.

## Usage
1.	Launch the app, and you’ll see its icon appear in the macOS menu bar.
1.	Click the icon to access the “Start” and “Stop” controls.
1.	Click “Start” to begin simulating user activity.
1.	Click “Stop” to pause the simulation.

## Notes
- Ensure you have a valid icon.png file if you’re building the app.
- The tool is intended for legitimate use cases, such as preventing screensavers or sleep mode during presentations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
   
