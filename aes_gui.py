from Cryptodome.Cipher import AES
import base64
from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

BLOCK_SIZE = 16
PADDING = '\0'
pad_it = lambda s: s+(16 - len(s)%16)*PADDING


iv = b'1234567890123456'


def encrypt_aes(sourceStr, key):
    b = bytes(key, 'utf-8')
    generator = AES.new(b, AES.MODE_CFB, iv)
    crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
    cryptedStr = base64.b64encode(crypt)
    return cryptedStr

def shenoFjalen1(event):
    entry_3.insert(0, encrypt_aes(entry_1.get(), entry_2.get()))

def shenoFjalen2(event):
    entry_3.insert(0, "Encrypted Text with 192-bit key")


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

myButton1 = Button(root, text='128-bit key Encryption', width=20, bg='grey', fg='black')
myButton1.place(x=240, y=230)
myButton1.bind("<Button-1>", shenoFjalen1)

label_3 = Label(root, text="128-bit Encrypted Text: ", width=20, font=("bold", 10))
label_3.place(x=80, y=280)
entry_3 = Entry(root, width=30)
entry_3.place(x=240, y=280)


myButton2 = Button(root, text='192-bit key Encryption', width=20, bg='grey', fg='black')
myButton2.place(x=240, y=330)
myButton2.bind("<Button-1>", shenoFjalen2)



root.mainloop()
