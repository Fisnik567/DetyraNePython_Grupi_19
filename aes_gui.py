from Cryptodome.Cipher import AES
import base64
from tkinter import ttk
from tkinter import *

window = Tk()
window.title('Aes Encryption')
window.geometry("750x450")

BLOCK_SIZE = 16
PADDING = '\0'
pad_it = lambda s: s+(16 - len(s)%16)*PADDING
iv = b'1234567890123456'

#Enkriptimi me CFB Mode(128-bit key length)
def encrypt_aesCFB128(sourceStr, key):
    if len(key) == 16:
        b = bytes(key, 'utf-8')
        generator = AES.new(b, AES.MODE_CFB, iv)
        crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
        cryptedStr = base64.b64encode(crypt)
        return cryptedStr
    else:
        gabim = "Key length should be 16!"
        return gabim

#Enkriptimi ne EBC MODE(128-bit key length)
def encrypt_aesECB128(sourceStr, key):
    if len(key) == 16:
        b = bytes(key, 'utf-8')
        generator = AES.new(b, AES.MODE_ECB)
        crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
        cryptedStr = base64.b64encode(crypt)
        return cryptedStr
    else:
        gabim = 'Key length should be 16!'
        return gabim

#Enkriptimi ne CFB MODE(192-bit key length)
def encrypt_aesCFB192(sourceStr, key):
    if len(key) == 24:
        b = bytes(key, 'utf-8')
        generator = AES.new(b, AES.MODE_CFB, iv)
        crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
        cryptedStr = base64.b64encode(crypt)
        return cryptedStr
    else:
        gabim = "Key length should be 24!"
        return gabim

#Enkriptimi ne EBC MODE(192-bit key length)
def encrypt_aesECB192(sourceStr, key):
    if len(key) == 24:
        b = bytes(key, 'utf-8')
        generator = AES.new(b, AES.MODE_ECB)
        crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
        cryptedStr = base64.b64encode(crypt)
        return cryptedStr
    else:
        gabim = "Key length should be 24!"
        return gabim    

#Enkriptimi ne CFB MODE(256-bit key length)
def encrypt_aesCFB256(sourceStr, key):
    if len(key) == 32:
        b = bytes(key, 'utf-8')
        generator = AES.new(b, AES.MODE_CFB, iv)
        crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
        cryptedStr = base64.b64encode(crypt)
        return cryptedStr
    else:
        gabim = "Key length should be 32!"
        return gabim

#Enkriptimi ne EBC MODE(256-bit key length)
def encrypt_aesECB256(sourceStr, key):
    if len(key) == 32:
        b = bytes(key, 'utf-8')
        generator = AES.new(b, AES.MODE_ECB)
        crypt = generator.encrypt(pad_it(sourceStr).encode('utf-8'))
        cryptedStr = base64.b64encode(crypt)
        return cryptedStr
    else:
        gabim = "Key length should be 32!"
        return gabim
    

def shenoFjalen1(event):
    entry_textECB1.insert(0, encrypt_aesECB128(entry_text1.get(), entry_text2.get()))
    
def shenoFjalen2(event):
    entry_textCFB1.insert(0, encrypt_aesCFB128(entry_text1.get(), entry_text2.get()))
    
def shenoFjalen3(event):
    entry_textECB11.insert(0, encrypt_aesECB192(entry_text11.get(), entry_text22.get()))

def shenoFjalen4(event):
    entry_textCFB22.insert(0, encrypt_aesCFB192(entry_text11.get(), entry_text22.get()))

def shenoFjalen5(event):
    entry_textECB111.insert(0, encrypt_aesECB256(entry_text111.get(), entry_text222.get()))

def shenoFjalen6(event):
    entry_textCFB222.insert(0, encrypt_aesCFB256(entry_text111.get(), entry_text222.get()))

def delete1(event):
    entry_text1.delete(0, 'end')
    entry_text2.delete(0, 'end')
    entry_textECB1.delete(0, 'end')
    entry_textCFB1.delete(0, 'end')

def delete2(event):
    entry_text11.delete(0, 'end')
    entry_text22.delete(0, 'end')
    entry_textECB11.delete(0, 'end')
    entry_textCFB22.delete(0, 'end')

def delete3(event):
    entry_text111.delete(0, 'end')
    entry_text222.delete(0, 'end')
    entry_textECB111.delete(0, 'end')
    entry_textCFB222.delete(0, 'end')


style = ttk.Style(window)
style.configure("leftab.TNotebook", tabposition='wn')

tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

#TAB1
tab1 = ttk.Frame(tab_control)

#TAB2
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text=f'{"AES 192-bit encryption":^20s}')
tab_control.add(tab2, text=f'{"AES 128-bit encryption":^20s}')
tab_control.add(tab3, text=f'{"AES 256-bit encryption":^20s}')

tab_control.pack(expand=1, fill="both")



label1 = Label(tab1, text="AES Encryption(128-bit key length)", padx=15, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text="AES Encryption(192-bit key length)", padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text="AES Encryption(256-bit key length)", padx=15, pady=5)
label3.grid(column=0, row=0)
                
                
                
#Tab1 Content
l1 = Label(tab1, text="Text to be encrypted: ", padx=15, pady=5)
l1.grid(column=0, row=1)

entry_text1 = Entry(tab1, width=50)
entry_text1.grid(row=1, column=1)

l2 = Label(tab1, text="Type the secret key(length of 16): ", padx=5, pady=5)
l2.grid(column=0, row=2)

entry_text2 = Entry(tab1, width=50)
entry_text2.grid(row=2, column=1)

buttonECB1 = Button(tab1, text="ECB-128-bit Encryption", width=2, bg="#03A9F4", fg = "#fff")
buttonECB1.place(x=50,y=100)
buttonECB1.bind("<Button-1>", shenoFjalen1)
buttonECB1.configure(height=1, width=18)

buttonCFB1 = Button(tab1, text="CFB-128-bit Encryption", width=12, bg="#03A9F4", fg = "#fff")
buttonCFB1.place(x=50,y=135)
buttonCFB1.bind("<Button-1>", shenoFjalen2)
buttonCFB1.configure(height=1, width=18)

buttonCLEAR1 = Button(tab1, text="Clear", width=12, bg="#03A9F4", fg="#fff")
buttonCLEAR1.bind("<Button-1>", delete1)
buttonCLEAR1.place(x=500,y=200)

lDisplay = Label(tab1, text="Encrypted Text: ", padx=0, pady=0)
lDisplay.place(x=200, y=100)

entry_textECB1 = Entry(tab1, width=50)
entry_textECB1.place(x=300, y=100)

lDisplay = Label(tab1, text="Encrypted Text: ", padx=0, pady=0)
lDisplay.place(x=200, y=135)

entry_textCFB1 = Entry(tab1, width=50)
entry_textCFB1.place(x=300, y=135)
                
                
                
#Tab2 Content
l11 = Label(tab2, text="Text to be encrypted: ", padx=15, pady=5)
l11.grid(column=0, row=1)

entry_text11 = Entry(tab2, width=50)
entry_text11.grid(row=1, column=1)

l22 = Label(tab2, text="Type the secret key(length of 24): ", padx=5, pady=5)
l22.grid(column=0, row=2)

entry_text22 = Entry(tab2, width=50)
entry_text22.grid(row=2, column=1)

buttonECB11 = Button(tab2, text="ECB 192-bit Encryption", width=2, bg="#03A9F4", fg = "#fff")
buttonECB11.place(x=50,y=100)
buttonECB11.bind("<Button-1>", shenoFjalen3)
buttonECB11.configure(height=1, width=18)

buttonCFB11 = Button(tab2, text="CFB 192-bit Encryption", width=12, bg="#03A9F4", fg = "#fff")
buttonCFB11.place(x=50,y=135)
buttonCFB11.bind("<Button-1>", shenoFjalen4)
buttonCFB11.configure(height=1, width=18)

buttonCLEAR11 = Button(tab2, text="Clear", width=12, bg="#03A9F4", fg="#fff")
buttonCLEAR11.bind("<Button-1>", delete2)
buttonCLEAR11.place(x=500,y=200)

lDisplay11 = Label(tab2, text="Encrypted Text: ", padx=0, pady=0)
lDisplay11.place(x=200, y=100)

entry_textECB11 = Entry(tab2, width=50)
entry_textECB11.place(x=300, y=100)

lDisplay22 = Label(tab2, text="Encrypted Text: ", padx=0, pady=0)
lDisplay22.place(x=200, y=135)

entry_textCFB22 = Entry(tab2, width=50)
entry_textCFB22.place(x=300, y=135)

#Tab3 Content
l111 = Label(tab3, text="Text to be encrypted: ", padx=15, pady=5)
l111.grid(column=0, row=1)

entry_text111 = Entry(tab3, width=50)
entry_text111.grid(row=1, column=1)

l222 = Label(tab3, text="Type the secret key(length of 32): ", padx=5, pady=5)
l222.grid(column=0, row=2)

entry_text222 = Entry(tab3, width=50)
entry_text222.grid(row=2, column=1)

buttonECB111 = Button(tab3, text="ECB 192-bit Encryption", width=12, bg="#03A9F4", fg = "#fff")
buttonECB111.place(x=50,y=100)
buttonECB111.bind("<Button-1>", shenoFjalen5)
buttonECB111.configure(height=1, width=18)

buttonCFB111 = Button(tab3, text="CFB 192-bit Encryption", width=12, bg="#03A9F4", fg = "#fff")
buttonCFB111.place(x=50,y=135)
buttonCFB111.bind("<Button-1>", shenoFjalen6)
buttonCFB111.configure(height=1, width=18)

buttonCLEAR111 = Button(tab3, text="Clear", width=12, bg="#03A9F4", fg="#fff")
buttonCLEAR111.bind("<Button-1>", delete3)
buttonCLEAR111.place(x=500,y=200)

lDisplay111 = Label(tab3, text="Encrypted Text: ", padx=0, pady=0)
lDisplay111.place(x=200, y=100)

entry_textECB111 = Entry(tab3, width=50)
entry_textECB111.place(x=300, y=100)

lDisplay222 = Label(tab3, text="Encrypted Text: ", padx=0, pady=0)
lDisplay222.place(x=200, y=135)

entry_textCFB222 = Entry(tab3, width=50)
entry_textCFB222.place(x=300, y=135)
                

window.mainloop()
