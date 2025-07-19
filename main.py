from tkinter import Tk, Label, Button, StringVar, Frame, Entry, messagebox

class App():
    def __init__(self,master):
        self.master = master
        self.master.title("Bill Manager")
        self.master.geometry("1000x500")
        self.master.resizable(False, False)
        self.label = Label(master, text="Bill Manager",bg="black",fg="white", font=("calibri", 33),width=300,height=2)
        self.label.pack()
        #Menu
        self.f = Frame(master,bg = "lightblue",highlightbackground="black",highlightthickness=1,width = 300,height = 370)
        self.f.place(x = 10,y = 118)
        self.label1 = Label(self.f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightblue").place(x = 80,y = 0)
        self.label2 = Label(self.f,font=("Lucida Calligraphy",15,'bold'),fg="black",bg="lightblue",text="Paneer....Rs.50/plate").place(x = 8,y = 80)
        self.label3 = Label(self.f,font=("Lucida Calligraphy",15,'bold'),fg="black",bg="lightblue",text="Chips....Rs.10/plate").place(x = 8,y = 110)
        self.label4 = Label(self.f,font=("Lucida Calligraphy",15,'bold'),fg="black",bg="lightblue",text="Snacks....Rs.20/plate").place(x = 8,y = 140)
        self.label5 = Label(self.f,font=("Lucida Calligraphy",15,'bold'),fg="black",bg="lightblue",text="Tea....Rs.15/plate").place(x = 8,y = 170)
        self.label6 = Label(self.f,font=("Lucida Calligraphy",15,'bold'),fg="black",bg="lightblue",text="Coffee....Rs.20/plate").place(x = 8,y = 200)

        #Entry Box
        self.f2 = Frame(master,bd = 5,width = 300,height = 370,relief="raised")
        self.f2.pack(pady=10,padx=10)
        self.paneer = StringVar()
        self.chips = StringVar()
        self.snacks = StringVar()
        self.tea = StringVar()
        self.coffee = StringVar()
        self.TotalBill = StringVar()
        #paneer
        self.lbl_paneer = Label(self.f2,font=("aria",20,'bold'),text="Paneer",fg="blue4")
        self.lbl_paneer.grid(row = 1,column=0)
        self.paneer_entry = Entry(self.f2,font=("aria",20,'bold'),textvariable=self.paneer,bd = 6,width=8,bg="lightgreen")
        self.paneer_entry.grid(row = 1,column=1)
        #chips
        self.lbl_chips = Label(self.f2,font=("aria",20,'bold'),text="Chips",fg="blue4")
        self.lbl_chips.grid(row = 3,column=0)
        self.chips_entry = Entry(self.f2,font=("aria",20,'bold'),textvariable=self.chips,bd = 6,width=8,bg="lightgreen")
        self.chips_entry.grid(row = 3,column=1)
        #snacks
        self.lbl_snacks = Label(self.f2,font=("aria",20,'bold'),text="Snacks",fg="blue4")
        self.lbl_snacks.grid(row = 5,column=0)
        self.snacks_entry = Entry(self.f2,font=("aria",20,'bold'),textvariable=self.snacks,bd = 6,width=8,bg="lightgreen")
        self.snacks_entry.grid(row = 5,column=1)
        #tea
        self.lbl_tea = Label(self.f2,font=("aria",20,'bold'),text="Tea",fg="blue4")
        self.lbl_tea.grid(row = 7,column=0)
        self.tea_entry = Entry(self.f2,font=("aria",20,'bold'),textvariable=self.tea,bd = 6,width=8,bg="lightgreen")
        self.tea_entry.grid(row = 7,column=1)
        #coffee
        self.lbl_coffee = Label(self.f2,font=("aria",20,'bold'),text="Coffee",fg="blue4")
        self.lbl_coffee.grid(row = 9,column=0)
        self.coffee_entry = Entry(self.f2,font=("aria",20,'bold'),textvariable=self.coffee,bd = 6,width=8,bg="lightgreen")
        self.coffee_entry.grid(row = 9,column=1)

        #divider
        self.divider = Label(self.f2,text="----------------------------------",font=("aria",20,'bold'),fg="pink4")
        self.divider.grid(row=11,column=0,columnspan=2)

        #Buttons
        self.btn_reset = Button(self.f2,text="Reset",font=("aria",16,'bold'),bd=5,fg="white",bg="red",width=10,command=lambda:self.Reset())
        self.btn_reset.grid(row=12,column=0)
        self.btn_total = Button(self.f2,text="Total",font=("aria",16,'bold'),bd=5,fg="white",bg="green",width=10,command=lambda:self.Total())
        self.btn_total.grid(row=12,column=1)

        #Bill
        self.f3 = Frame(master,bg="lightyellow",highlightbackground="black",highlightthickness=1,width = 300,height = 370)
        self.f3.place(x = 690,y = 118)
        self.bill = Label(self.f3,text="Bill",font=("calibri",20),bg="lightyellow",fg="black")
        self.bill.place(x = 120,y = 10)

    def Total(self):
        try:a1 = int(self.paneer.get())
        except: a1 =0
        try:a2 = int(self.chips.get())
        except: a2 =0
        try:a3 = int(self.snacks.get())
        except: a3 =0
        try:a4 = int(self.tea.get())
        except: a4 =0
        try:a5 = int(self.coffee.get())
        except: a5 =0

        c1 = a1 * 50
        c2 = a2 * 10
        c3 = a3 * 20
        c4 = a4 * 15
        c5 = a5 * 20

        self.lbl_total = Label(self.f3,font=("aria",20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
        self.lbl_total.place(x = 10,y = 50)


    def Reset(self):
        self.paneer.set("")
        self.chips.set("")
        self.snacks.set("")
        self.tea.set("")
        self.coffee.set("")
        self.TotalBill.set("")
        messagebox.showinfo("Reset", "All fields have been reset.")



root = Tk()
app = App(root)
root.mainloop()
