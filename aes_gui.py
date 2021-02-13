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

def shenoFjalen1(event):
    entry_3.insert(0, encrypt_aes(entry_1.get(), entry_2.get()))

def shenoFjalen2(event):
    entry_3.insert(0, "Encrypted Text with 192-bit key")


style = ttk.Style(window)
style.configure("leftab.TNotebook", tabposition='wn')

tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

#TAB1
tab1 = ttk.Frame(tab_control)

#TAB2
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text=f'{"CFB 192-bit encryption":^20s}')
tab_control.add(tab2, text=f'{"CFB 128-bit encryption":^20s}')
tab_control.add(tab3, text=f'{"CFB 256-bit encryption":^20s}')

tab_control.pack(expand=1, fill="both")



label1 = Label(tab2, text="CFB Mode Aes Encryption", padx=15, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab1, text="EBC Mode Aes Encryption", padx=5, pady=5)
label2.grid(column=0, row=0)
                
#CFB MODE
l1 = Label(tab2, text="Text to be encrypted: ", padx=15, pady=5)
l1.grid(column=0, row=1)

# fname_raw_entry = StringVar()
entry_text1 = Entry(tab2, width=50)
entry_text1.grid(row=1, column=1)

l2 = Label(tab2, text="Type the secret key: ", padx=5, pady=5)
l2.grid(column=0, row=2)
fname_raw_entry = StringVar()
entry_text2 = Entry(tab2, width=50)
entry_text2.grid(row=2, column=1)

button1 = Button(tab2, text="128-bit Encryption", width=12, bg="#03A9F4", fg = "#fff")
button1.grid(row=3, column=0, padx=5, pady=30)
button1.bind("<Button-1>", shenoFjalen1)
button1.configure(height=1, width=15)

button2 = Button(tab2, text="Clear", width=12, bg="#03A9F4", fg = "#fff")
button2.grid(row=3, column=1, padx=5, pady=30)

#Encrypted Text

lDisplay = Label(tab2, text="Encrypted Text: ", padx=5, pady=5)
lDisplay.grid(column=0, row=4)

entry_text3 = Entry(tab2, width=50)
entry_text3.grid(row=4, column=1)


window.mainloop()
