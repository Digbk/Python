import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("All Message Boxes")
window.geometry("300x400")


def show_info():
    messagebox.showinfo("Info", "This is an information message.")


def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")


def show_error():
    messagebox.showerror("Error", "Something went wrong!")


def ask_yesno():
    messagebox.askyesno("Question", "Do you want to continue?")


def ask_okcancel():
    messagebox.askokcancel("Question", "Do you want to continue?")


def ask_retrycancel():
    messagebox.askretrycancel("Error", "Do you want to try again?")


def ask_yesnocancel():
    messagebox.askyesnocancel("Question", "Do you want to save?")


def ask_question():
    messagebox.askquestion("Question", "Are you sure?")


tk.Button(window, text="Show Info", command=show_info).pack(pady=5)
tk.Button(window, text="Show Warning", command=show_warning).pack(pady=5)
tk.Button(window, text="Show Error", command=show_error).pack(pady=5)
tk.Button(window, text="Ask Yes / No", command=ask_yesno).pack(pady=5)
tk.Button(window, text="Ask OK / Cancel", command=ask_okcancel).pack(pady=5)
tk.Button(window, text="Ask Retry / Cancel", command=ask_retrycancel).pack(pady=5)
tk.Button(window, text="Ask Yes / No / Cancel", command=ask_yesnocancel).pack(pady=5)
tk.Button(window, text="Ask Question", command=ask_question).pack(pady=5)

window.mainloop()