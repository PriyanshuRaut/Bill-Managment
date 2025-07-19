from tkinter import Tk, Label, Button, StringVar

class App():
    def __init__(self,master):
        self.master = master
        self.master.title("Bill Manager")
        self.master.geometry("1000x500")
        self.master.resizable(False, False)
        self.label = Label(master, text="Bill Manager",bg="black",fg="white", font=("calibri", 33),width=300,height=2)
        self.label.pack()

root = Tk()
app = App(root)
root.mainloop()
