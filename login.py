# create a login in python
from email import message
import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showinfo("Login", "Invalid username or password")

root = tk.Tk()
root.title("Login")