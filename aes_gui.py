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


window.mainloop()
