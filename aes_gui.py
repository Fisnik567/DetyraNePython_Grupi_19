from Cryptodome.Cipher import AES
import base64
from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="AES Encryption", width=20, font=("bold", 20))
label_0.place(x=90, y=53)


label_1 = Label(root, text="Enter text to be Encrypted: ", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, width=30)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Write secret key: ", width=20, font=("bold", 10))
label_2.place(x=80, y=180)

entry_2 = Entry(root, width=30)
entry_2.place(x=240, y=180)


root.mainloop()
