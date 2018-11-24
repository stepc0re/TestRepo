import os
import time
import shutil
import subprocess
import pygame
from pygame.locals import *


import click

k = click.getchar()
if k == 'a':
    print True






import pynput
import msvcrt

# x = msvcrt.getch()
# if x.decode() == 's':
#     print True

from pynput.keyboard import Key, Controller

keyboard = Controller()
# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'

from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print type(key)

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()








    # for event in pygame.get_array_interface():
#     if (event.type == 1) or (event.type == 2):
#         print ("key pressed")

# time.sleep(10)
# print (1)
# os.system('shutdown -t 5 -r')
# src = r'C:\Users\Steph\Desktop\mahsa.txt'
# ord = r'C:\Users\Steph\Desktop\nana.txt'
# os.system('copy C:\\Users\\Steph\\Desktop\\mahsa.txt C:\\Users\\Steph\\Desktop\\nana.txt')

#f = os.startfile(r'C:\Users\Steph\Desktop\mahsa.txt')
#print (f)
#shutil.copyfile(ord, src)

#mode_1 = int(input('Enter 1'))
#with os.popen(r'C:\Users\Steph\Desktop\nana.json', 'w') as f:


#lines = [line.rstrip() for line in os.popen(r'C:\Users\Steph\Desktop\nana.txt')]
#print (lines)