from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("HTML IDE")
root.minsize(650, 650)
root.maxsize(650, 650)
root.configure(bg="gray87")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
close_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

file_name_label = Label(root, text="File name")
file_name_label.place(relx=0.28, rely=0.03, anchor=CENTER)

file_name_entry = Entry(root)
file_name_entry.place(relx=0.46, rely=0.03, anchor=CENTER)

text_box = Text(root, height=35, width=80, background="#1F1F1F" ,foreground="#3AAD98")
text_box.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()