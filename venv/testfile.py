# from tkinter import *
#
# root = Tk()
#
# frame = Frame(root)
#
# def key(event):
#     print("pressed", repr(event.keycode))
#
# def callback(event):
#     print("clicked at", event.x, event.y)
#
# frame.focus_set()
# frame.bind("<Key>", key)
# frame.pack()
#
# root.mainloop()
# -----------TRIAL---------
# import tkinter as TK
#
# root = TK.Tk()
# button= TK.Button(root)
# button.pack()
#
# def func1():
#     print('func1 is called!')
#     button.config(text='call func2', command=func2)
# def func2():
#     print('func2 is called!')
#
# button.config(text='call func1', command=func1)
#
# root.bind('<Return>', lambda event=None: button.invoke())
# root.mainloop()

from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()