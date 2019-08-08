from pynput import mouse
from  pynput.mouse import Button, Controller
import time 

def on_click(x, y , button, pressed):

    button_name = ''
    #print(button)
    if button == Button.left:
        button_name = 'Left Button'
        working = False
    elif button == Button.middle:
        button_name = 'Middle Button'
        working = False
    elif button == Button.right:
        button_name = 'Right Button'
        working = True
    else:
        button_name = 'Unknown'
    if pressed:
        print('{0} Pressed at {1} at {2}'.format(button_name, x, y))
    else:
        print('{0} Released at {1} at {2}'.format(button_name=='', x, y))
        
    if not pressed:
        return False

while True:
    with mouse.Listener(on_click = on_click,suppress = False) as listener:
        listener.join()