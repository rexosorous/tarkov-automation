import keyboard
import random
import threading
import os
from time import sleep



on = False




def toggle():
    global on
    on = not on



def stop():
    os._exit(0)


# RELOAD
def reloader():
    while True:
        while on:
            keyboard.press('r')
            sleep(random.uniform(0.01, 0.08))
            keyboard.release('r')
            sleep(random.uniform(0.3, 1))



keyboard.add_hotkey('\\', toggle)
keyboard.add_hotkey('/', stop)


reload_thread = threading.Thread(target=reloader)
reload_thread.daemon = True
reload_thread.start()


keyboard.wait()