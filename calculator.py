import tkinter as tk
from tkinter import messagebox


def calculator():
    label.config(text="Hello! This is a basic calculator")

root= tk.Tk()
root.title("Addition app")
root.geometry("300x500")

label=tk.Label(root,text="Add")

def find_sum():
    num1= entry1.get()
    num2=entry2.get()

    if num1.isdigit() and num2.isdigit():
        result= int(num1)+int(num2)
        messagebox.showinfo("Result", f"Sum: {result}")
    else:
        messagebox.showerror("Error","Enter valid numbers")

label1=tk.Label(root,text="Number 1")
entry1=tk.Entry(root)
label1.pack()
entry1.pack(pady=5)
label2=tk.Label(root,text="Number 2")
entry2=tk.Entry(root)
label2.pack()
entry2.pack(pady=5)

tk.Button(root,text="Find Sum", command=find_sum).pack(pady=10)

root.mainloop()