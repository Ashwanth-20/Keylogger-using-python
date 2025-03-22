# Keylogger - Cyber Security Project

## Overview
This project is a simple Python-based keylogger that logs keystrokes and saves them to a file. Additionally, it includes an auto-start mechanism to execute the script on system startup. This tool is intended strictly for educational and ethical cybersecurity research purposes.

## Features
- Captures and logs keystrokes.
- Runs in the background.
- Saves keystrokes to a log file.
- Automatically executes on system startup (Windows).

## Prerequisites
- Python 3.x installed.
- Required library:
  ```bash
  pip install pynput
  ```

 Run the script once to create the necessary startup batch file.
 Restart your system to ensure it runs automatically.

## How It Works
- The script listens for keyboard events.
- Captured keystrokes are logged in `keylog.txt`.
- The script creates a batch file in the Windows Startup folder to ensure auto-execution.

## Important Notice
This project is strictly for educational purposes. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission before using this tool in any environment.

