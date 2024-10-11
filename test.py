#simple 25/5 min time manager 4 study By Mohamed Aziz Heni
#Feel Free how to use it :)
#azizheni24@gmail.com

import tkinter as tk
from tkinter import messagebox
import time

#(min * 60 * 1000 milliseconds)


b=0
def show_reminder():
    messagebox.showinfo("Reminder", "Take a 5 min rest")
    root.after(300000, go_back)

def go_back():
    global b
    b=b+1
    text_widget.insert(tk.END, f"You are on round {b}\n")
    text_widget.see(tk.END) 
    if b == 8 :
        messagebox.showinfo("Reminder", "You reached 4h , Now take a 30 min rest")
        root.after(1500000, go_back)
        
        b=0
    else :
        messagebox.showinfo("Reminder", "Go back !!")
        root.after(1500000, show_reminder)


root = tk.Tk()
 

text_widget = tk.Text(root, height=15, width=40)
text_widget.pack(pady=20)


text_widget.insert(tk.END, f"You are on round {b}\n")
text_widget.see(tk.END)


root.after(1500000, show_reminder)





root.title("Wa9ti - Time manger")
root.geometry("300x500")







root.iconphoto(False, tk.PhotoImage(file="icon.ico"))

root.mainloop()
