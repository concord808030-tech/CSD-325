#Miguel Fernandez Brazon
#3/08/26
import tkinter as tk
from tkinter import Menu, END


#Main Window

root = tk.Tk()
root.title("MIGUEL-LIST!")

root.geometry("350x500")
root.config(bg="white")


#Functions

def add_task():
    task = entry.get()
    if task.strip():
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task(event):
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        pass

def exit_program():
    root.quit()


#Menu Bar

menubar = Menu(root, bg="#1e3d58", fg="black")
filemenu = Menu(menubar, tearoff=0, bg="black", fg="#1e3d58")

filemenu.add_command(label="Exit", command=exit_program)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

#Widgets
label = tk.Label(
    root,
    text="Your TO-DO Right-click to delete",
    bg="WHITE",
    fg="#1e3d59",
    font=("Helvetica", 15)
)
label.pack(pady=15)

entry = tk.Entry(root, width=26, font=("Helvetica", 16))
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Note", command=add_task, bg="#1e3d59", fg="white")
add_button.pack(pady=5)

# Listbox
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(
    frame,
    width=30,
    height=12,
    yscrollcommand=scrollbar.set,
    font=("Helvetica", 11)
)
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

# Bind right-click
listbox.bind("<Button-3>", delete_task)


#  Run Program

root.mainloop()