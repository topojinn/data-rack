import customtkinter as ctk
from tkinter import messagebox
import json

class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

logPath = "C:\\placeholder\\placeholder.json"

root = ctk.CTk()
root.title("NAME UR COMIC")
root.geometry("800x400")
root.iconbitmap()

label_title = ctk.CTkLabel(root, text="insert stuff:")
label_title.pack(pady=10)

AuthorEntry = ctk.CTkEntry(root, placeholder_text="author", width=170)
AuthorEntry.pack(pady=10)

TitleEntry = ctk.CTkEntry(root, placeholder_text="title", width=170)
TitleEntry.pack(pady=10)

PagesEntry = ctk.CTkEntry(root, placeholder_text="pages", width=170)
PagesEntry.pack(pady=10)

label_input = ctk.CTkLabel(root, text="")

def enter():
    author = AuthorEntry.get()
    print(f"author: {author}")
    
    title = TitleEntry.get()
    print(f"title: {title}")
    
    pages = PagesEntry.get()
    print(f"pages: {pages}")

    switcher = ctk.CTkLabel(root, text="")
    switcher.pack()

    label_input.configure(text = f"author: {author}\ntitle: {title}\npages: {pages}")
    label_input.pack()
    
    book_data = Book(author, title, pages)

    with open(logPath, "w") as file:
        json.dump(book_data.__dict__, file, indent=4)
    
    messagebox.showinfo("ADVICE", "done!")

placehold = ctk.CTkLabel(root, text="")
placehold.pack()

btn = ctk.CTkButton(root, text="enter data", command=enter)
btn.pack()

root.mainloop()
