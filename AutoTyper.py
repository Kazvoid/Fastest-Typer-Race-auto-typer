from pynput.keyboard import Key, Listener
import pydirectinput

def typeS():
    pydirectinput.PAUSE = 0.0001
    f = open('text.txt', 'r')

    for c in f.read():
        if c == ' ':
            pydirectinput.press('space')
        elif c.isupper():
            pydirectinput.keyDown('shift')
            pydirectinput.press(c.lower())
            pydirectinput.keyUp('shift')
        elif c == '?':
            pydirectinput.keyDown('shift')
            pydirectinput.press('/')
            pydirectinput.keyUp('shift')
        elif c == '!':
            pydirectinput.keyDown('shift')
            pydirectinput.press('1')
            pydirectinput.keyUp('shift')
        else:
            pydirectinput.press(c)
    f.close()

def onPress(key):
    if key == Key.end:
        typeS()
def onRelease(key):
    if key == Key.esc:
        return False

try:
    f = open('text.txt', 'r')
except:
    f = open('text.txt', 'w')
f.close()

with Listener(on_press = onPress, on_release = onRelease) as listener:
    listener.join()

