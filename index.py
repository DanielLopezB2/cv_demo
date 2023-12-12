from tkinter import *

app = Tk()
app.title("Hello World")
app.geometry("500x300")
app.resizable(width=0, height=0)

label = Label(app, text="Hello, world!")
label.pack()

app.mainloop()