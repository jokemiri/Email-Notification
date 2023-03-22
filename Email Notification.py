import imaplib
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def check_email():
    email_address = email_entry.get()
    password = password_entry.get()

    # set up the IMAP connection
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_address, password)
    mail.select('inbox')

    # check for new email every 30 seconds
    while True:
        mail.select('inbox')
        status, response = mail.search(None, 'UNSEEN')
        unread = response[0].split()

        if len(unread) > 0:
            messagebox.showinfo('New Email', 'You have new email(s)!')
        root.after(30000) # 30 seconds

# set up the GUI
root = tk.Tk()
root.title('Email Checker')


style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-light")

# create labels and entry fields
email_label = tk.Label(root, text='Email Address:')
email_entry = tk.Entry(root)
email_entry.insert(0, 'Email')
email_entry.bind("<FocusIn>", lambda clear_name: email_entry.delete('0', 'end'))

password_label = tk.Label(root, text='Password:')
password_entry = tk.Entry(root, show='*')
# password_entry.insert(0, 'Password')

email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry.grid(row=0, column=1, padx=10, pady=10)

password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# create a button to start checking email
check_button = tk.Button(root, text='Check Email', command=check_email)
check_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def toggle_LD():
    if toggle_switch.instate(['selected']):
        style.theme_use('forest-light')
    else:
        style.theme_use('forest-dark')


toggle_switch = ttk.Checkbutton(root, text='Toggle Light/Dark', style='Switch', command=toggle_LD)
toggle_switch.grid(row=6, column=0, sticky='nsew', padx=5, pady=10)

root.mainloop()
