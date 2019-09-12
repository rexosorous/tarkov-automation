import keyboard
import pyautogui as pag
import random
import threading
import os
from time import sleep





# CLICKER
def click():
    for i in range(8):
        pag.press('r')
        sleep(random.uniform(5, 10))
        cycles = random.randint(90, 120)
        for j in range(cycles):
            pag.click()
            sleep(random.uniform(0.05, 0.1))
    sleep(random.uniform(0.3, 3))
    pag.press('tab')


def start():
    click_thread = threading.Thread(target=click)
    click_thread.daemon = True
    click_thread.start()


def stop():
    os._exit(0)



keyboard.add_hotkey('\\', start)
keyboard.add_hotkey('/', stop)
keyboard.wait()