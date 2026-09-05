import customtkinter as ctk
from tkinter import messagebox

root = ctk.CTk()
root.title("NAME UR COMIC")
root.geometry("800x600")

label_entry = ctk.CTkLabel(root, text="insert stuff:")
label_entry.pack(pady=(20, 5))

label_input = ctk.CTkLabel(root, text="")
label_input.pack(pady=(20, 5))

AuthorEntry = ctk.CTkEntry(
    root, 
    placeholder_text="author", 
    width=250,
    height=35
)

TitleEntry = ctk.CTkEntry(
    root, 
    placeholder_text="title", 
    width=250,
    height=35
)

PagesEntry = ctk.CTkEntry(
    root, 
    placeholder_text="pages", 
    width=250,
    height=35
)

AuthorEntry.pack(pady=5)
TitleEntry.pack(pady=5)
PagesEntry.pack(pady=5)

def enter():
    global centerX

    # enter author
    author = AuthorEntry.get()
    print(f"author: {author}")

    # enter title
    title = TitleEntry.get()
    print(f"title: {title}")

    # enter title
    pages = PagesEntry.get()
    print(f"pages: {pages}")

    label_input.configure(text = f"author: {author}\ntitle: {title}\npages: {pages}")
    label_input.place(x=380, y=325)

    messagebox.showinfo("ADVICE", "done!")

def clear():
    global AuthorEntry
    global TitleEntry
    global PagesEntry

    AuthorEntry = ""
    TitleEntry = ""
    PagesEntry = ""
    
btn = ctk.CTkButton(root, text="enter data", command=enter)
btn.pack(pady=20)

btn = ctk.CTkButton(root, text="reset", command=clear)
btn.pack(pady=20)

root.mainloop()
