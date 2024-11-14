import tkinter as tk
from tkinter import messagebox
from Module import *  


db = Database('d:/mydb10.db')


win = tk.Tk()
win.geometry('700x500')
win.title('Login Form')
win.configure(bg='#f0fdec')


# FUNCTIONS ***********************************************

def sign_up():
    if ent_email.get() == '' or ent_pass.get() == '':
        messagebox.showerror('ERROR', 'Password OR Email is empty')
    else:
       
        db.insert(ent_fname.get(), ent_lname.get(), ent_email.get(), ent_pass.get())
        
       
        ent_email.delete(0, tk.END)
        ent_pass.delete(0, tk.END)
        ent_fname.delete(0, tk.END)
        ent_lname.delete(0, tk.END)
        ent_fname.focus_set()
        
        messagebox.showinfo('Success', 'Account created successfully!')


def sign_in():
    if not ent_email.get() or not ent_pass.get():
        messagebox.showerror('ERROR', 'Email and Password must be filled')
        return
    
   
    result = db.fetch(ent_email.get(), ent_pass.get())
    
    if result: 
        messagebox.showinfo('Success', 'Login Successful!')
        win.destroy()
        
        win1 = tk.Tk()
        win1.geometry('250x250')
        win1.title("Welcome")
        lbl_welcome = tk.Label(win1, text="Welcome to the system!", font='arial 15 bold')
        lbl_welcome.pack()
        win1.mainloop()
    else:
        messagebox.showerror('ERROR', 'Invalid Email or Password')

# WIDGETS ******************************************************************

lbl_fname = tk.Label(win, text='Fname:', font='arial 15 bold')
lbl_fname.place(x=140, y=50)

lbl_lname = tk.Label(win, text='Lname:', font='arial 15 bold')
lbl_lname.place(x=140, y=125)

lbl_email = tk.Label(win, text='Email:', font='arial 15 bold')
lbl_email.place(x=140, y=200)

lbl_pass = tk.Label(win, text='Password:', font='arial 15 bold')
lbl_pass.place(x=140, y=275)

lbl_important_email = tk.Label(win, text='*', font='arial 15 bold', fg='red')
lbl_important_email.place(x=130, y=200)

lbl_important_pass = tk.Label(win, text='*', font='arial 15 bold', fg='red')
lbl_important_pass.place(x=130, y=275)

ent_fname = tk.Entry(win, font='arial 15 bold')
ent_fname.place(x=290, y=50)

ent_lname = tk.Entry(win, font='arial 15 bold')
ent_lname.place(x=290, y=125)

ent_email = tk.Entry(win, font='arial 15 bold')
ent_email.place(x=290, y=200)

ent_pass = tk.Entry(win, font='arial 15 bold', show='*')
ent_pass.place(x=290, y=275)

btn_sign_up = tk.Button(win, text='Sign Up', font='arial 15 bold', width=15, bg='#9ffe87', command=sign_up)
btn_sign_up.place(x=140, y=350)

btn_sign_in = tk.Button(win, text='Sign In', font='arial 15 bold', width=15, bg='#9ffe87', command=sign_in)
btn_sign_in.place(x=365, y=350)


win.mainloop()

db.close()
