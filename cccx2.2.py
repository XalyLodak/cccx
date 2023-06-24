from pathlib import Path
import string
import tkinter as tk
from tkinter import *

w = tk.Tk()
w.title("CCCX 2.0 GUI")

image_path = "icon.png"
icon_image = PhotoImage(file=image_path)
w.iconphoto(True, icon_image)

txt0 = tk.Label(w, text="Cesar Code Creator by XalyLodak")
txt0.pack()

txt1 = tk.Label(w, text="Your Offset (0-25) :")
txt1.pack()

entry0 = tk.Entry(w)
entry0.pack()

txt2 = tk.Label(w, text="Your Word :")
txt2.pack()

entry1 = tk.Entry(w)
entry1.pack()

def cccx():
    offset = int(entry0.get())
    word = entry1.get()

    if offset >= 0 and offset <= 25:
        letters = string.ascii_uppercase
        letters_offset = letters[offset:] + letters[:offset]
        encrypted_word = ""

        for lettre in word:
            if lettre.isalpha():
                v1 = (letters.index(lettre.upper()) + offset) % 26
                encrypted_word += letters_offset[v1]
            else:
                encrypted_word += lettre

        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encrypted_word)
        result_text.configure(state="disabled")
    else:
        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Your offset is out of range. Please try again with a value between 0 and 25.")
        result_text.configure(state="disabled")
    
empty_space = tk.Frame(w, height=10)
empty_space.pack()

result_text = tk.Text(w, height=5)
result_text.configure(state="disabled")
result_text.pack()

b1 = tk.Button(w, text="Encrypt", command=cccx)
b1.pack(side=tk.LEFT)

qb = tk.Button(w, text="Quit", command=w.destroy)
qb.pack(side=tk.RIGHT)

w.mainloop()