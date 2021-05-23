from tkinter import *

window = Tk()

def submit():
    username = entry.get()
    print("Hello = ", username)

def delete():
    entry.delete(0, END)

entry = Entry(window,
              font=("Arial", 50, ),
              fg="#00FF00",
              show="*")
entry.pack()
submit_btn = Button(window,
                    text="submit",
                    command=submit)
submit_btn.pack(side=RIGHT)

delete_btn = Button(window,
                    text="delete",
                    command=delete)
delete_btn.pack(side=RIGHT)

window.mainloop()