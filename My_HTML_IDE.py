from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()

root.title("HTML IDE")
root.minsize(650, 650)
root.maxsize(650, 650)
root.configure(bg="gray87")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
close_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

def openFile():
    file_name_entry.delete(0, END)
    text_box.delete(0.1, END)
    
    html_file = filedialog.askopenfilename(title="Open file", filetypes=(("Open HTML file", "*.html"), ))
    print(html_file)
    
    name = os.path.basename(html_file)
    formated_name = name.split(".")[0]
    root.title(formated_name)
    file_name_entry.insert(END, formated_name)
    
    html_file = open(html_file, "r")
    code = html_file.read()
    
    text_box.insert(END, code)
    
file_name_label = Label(root, text="File name")
file_name_label.place(relx=0.28, rely=0.03, anchor=CENTER)

file_name_entry = Entry(root)
file_name_entry.place(relx=0.46, rely=0.03, anchor=CENTER)

text_box = Text(root, height=35, width=80, background="#1F1F1F", foreground="#3AAD98")
text_box.place(relx=0.5, rely=0.55, anchor=CENTER)

open_file_button = Button(root, image=open_img, text="Open file", command=openFile)
open_file_button.place(relx=0.07, rely=0.03, anchor=CENTER)


root.mainloop()