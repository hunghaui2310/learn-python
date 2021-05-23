from tkinter import *

window = Tk()       # instantiate an instanceof a window
window.geometry("420x420")
window.title("First Program in GUI")

# icon = PhotoImage(file='path_to _file') # set icon logo
# window.iconphoto(True, icon)
# window.config(background="")

# label = an area widget that holds text and/or an image
label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20)
label.place(x=0, y=0)

window.mainloop()   # place window on computer screen, listen for event