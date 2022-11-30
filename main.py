from tkinter import *
import time
from threading import Thread

SPEED = 5

writing = True


def destroy_text():
    global writing
    while writing:
        current_text = text.get('1.0', 'end-1c')
        word_list = current_text.split(' ')
        if word_list[-1] == 'STOP':
            break
        time.sleep(SPEED)
        new_text = text.get('1.0', 'end-1c')
        while current_text == new_text:
            time.sleep(0.1)
            text.delete('end-2c', 'end-1c')
            current_text = text.get('1.0', 'end-1c')
            time.sleep(0.2)
            new_text = text.get('1.0', 'end-1c')


def create_thread():
    thread = Thread(target=destroy_text)
    thread.start()


window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("%dx%d" % (screen_width, screen_height))
window.title('Text Destroyer')

title_label = Label(text='Write or DIE', font=('Arial', 25))
title_label.config(pady=20, foreground='red')
title_label.grid(column=0, row=0)

instructions = Label(text='Press "Start" and the Text Destroyer will silently wait until you stop writing to gobble up '
                          'everything you have written so far. Wait too long and soon you will have nothing left!\nOnce'
                          ' you are done, type "STOP" to deactivate the Destroyer.',
                     wraplength=500)
instructions.config(pady=10)
instructions.grid(column=0, row=1)

text = Text(wrap=WORD)
text.config(width=185, height=45)
text.grid(column=0, row=3)

start = Button(text='Start', command=create_thread, width=30, font=('Arial', 12))
start.config(pady=5)
start.grid(column=0, row=4)

window.mainloop()
