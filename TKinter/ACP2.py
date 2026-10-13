from tkinter import *

window = Tk()
window.title("Personal Bio Form")
window.geometry("500x450")
window.configure(bg="white")

title = Label(
    window,
    text="Personal Bio Form",
    fg="white",
    bg="purple",
    font=("Arial", 18, "bold"),
    width=35
)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=15)

name_label = Label(
    window,
    text="Name:",
    fg="black",
    bg="white",
    font=("Arial", 12)
)
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

name_entry = Entry(
    window,
    fg="blue",
    bg="lightyellow",
    width=30
)
name_entry.grid(row=1, column=1, padx=10, pady=10)


hobby_label = Label(
    window,
    text="Hobby:",
    fg="black",
    bg="white",
    font=("Arial", 12)
)
hobby_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

hobby_entry = Entry(
    window,
    fg="blue",
    bg="lightyellow",
    width=30
)
hobby_entry.grid(row=2, column=1, padx=10, pady=10)

about_frame = Frame(
    window,
    relief=RAISED,
    borderwidth=3,
    bg="white"
)
about_frame.grid(
    row=3,
    column=0,
    columnspan=2,
    padx=10,
    pady=15
)

about_label = Label(
    about_frame,
    text="About Me:",
    fg="black",
    bg="white",
    font=("Arial", 12, "bold")
)
about_label.pack(pady=5)

about_text = Text(
    about_frame,
    fg="green",
    bg="lightyellow",
    width=40,
    height=6
)
about_text.pack(padx=10, pady=5)

def show_card_details():

    name = name_entry.get()

    hobby = hobby_entry.get()

    user_about_me_input = about_text.get("1.0", END).strip()

    about_text.delete("1.0", END)

    completed_bio = "--- My Personal Bio ---\n"
    completed_bio += f"Name: {name}\n"
    completed_bio += f"Hobby: {hobby}\n"

    if user_about_me_input:
        completed_bio += f"About Me: {user_about_me_input}\n"

    about_text.insert(END, completed_bio)

submit = Button(
    window,
    text="Show My Card",
    bg="purple",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    command=show_card_details
)
submit.grid(
    row=4,
    column=0,
    columnspan=2,
    padx=10,
    pady=15
)

window.mainloop()