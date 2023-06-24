from tkinter import *
from tkinter import messagebox
import random
import string

LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)
NUMBERS = list(string.digits)
SYMBOLS = ["!", "?", "@", "#", "$", "%", "^", "&", "*"]

# Creating a window
root = Tk()

root.geometry("450x250")
root.resizable(False, False)
root.iconbitmap("lock.ico")

root.title("Secure Password Generator | Basith Mohammed")

outputlabel = Label(root, text="Your secure password is: ",  font="Helvetica")
outputlabel.grid(row=0, column=0, columnspan=2, sticky=W, padx=(20, 0), pady=(20, 0))

lengthlabel = Label(root, text="Length: ", font="Helvetica")
lengthlabel.grid(row=1, column=0, sticky=W, padx=(40, 0), pady=(30, 10))

lengthentry = Entry(root, font="Helvetica", width=5)
lengthentry.grid(row=1, column=0, sticky=W, padx=(100, 0), pady=(30, 10))

uppercase = IntVar()
c1 = Checkbutton(root, text="Uppercase Letters (ABC)", font="Helvetica", variable=uppercase)
c1.grid(row=2, column=0, sticky=W, columnspan=2, padx=(35,0), pady=(0, 0))

lowercase = IntVar()
c2 = Checkbutton(root, text="Lowercase Letters (abc)", font="Helvetica", variable=lowercase)
c2.grid(row=3, column=0, sticky=W, columnspan=2, padx=(35,0), pady=(0, 0))

numbers = IntVar()
c3 = Checkbutton(root, text="Numberical Digits (123)", font="Helvetica", variable=numbers)
c3.grid(row=4, column=0, sticky=W, columnspan=2, padx=(35,0), pady=(0, 0))

symbols = IntVar()
c4 = Checkbutton(root, text="Special Symbols (&?$)", font="Helvetica", variable=symbols)
c4.grid(row=5, column=0, sticky=W, columnspan=2, padx=(35,0), pady=(0, 20))

passwordentry = Entry(root, font="Helvetica")
passwordentry.grid(row=0, column=1, padx=(90,20), pady=(20, 0))

def password():
    allowed = []
    if uppercase.get() == 1:
        allowed.extend(UPPERCASE)
    if lowercase.get() == 1:
        allowed.extend(LOWERCASE)
    if numbers.get() == 1:
        allowed.extend(NUMBERS)
    if symbols.get() == 1:
        allowed.extend(SYMBOLS)

    pword = ""
    try:
        length = int(lengthentry.get())
        if length > 1024:
            messagebox.showerror('Length Error', 'Error: Length must be smaller than 1024!')
        else:
            for _ in range(length):
                pword = pword + random.choice(allowed)
    except ValueError:
        messagebox.showerror('Length Error', 'Error: Length must be a numerical value!') 
    except IndexError:
        messagebox.showerror("Checkbox Error", "Error: You must select one of the checkboxes!")     
    
    passwordentry = Entry(root, font="Helvetica")
    passwordentry.insert(0, pword)
    passwordentry.grid(row=0, column=1, padx=(90,20), pady=(20, 0))

def enter_to_password(event):
    password()

generate = Button(root, text="Generate", font="Helvetica", command=password, width=15, height=5)
generate.grid(row=1, column=1, padx=(80, 0), rowspan=10)

root.bind('<Return>', enter_to_password)

# Creating the loop that continues to run the program
root.mainloop()