from tkinter import*
window = Tk()
window.title("GUI Calculator")
window.geometry("500x600")

label1 = Label(window,text="First Number",font=("Calibri",12))
label1.pack()
text1 = Text(window,height=1,width=20,font=("Calibri",20))
text1.pack()
label2 = Label(window,text="Second Number",font=("Calibri",12))
label2.pack()
text2 = Text(window,height=1,width=20,font=("Calibri",20))
text2.pack()

def add():
    n1 = int(text1.get("1.0","end-1c"))
    n2 = int(text2.get("1.0","end-1c"))
    print(n1+n2)
button1 = Button(window,command=add,text="Add",height=1,width=15,font=("Arial",20))
button1.pack()
def sub():
    n1 = int(text1.get("1.0","end-1c"))
    n2 = int(text2.get("1.0","end-1c"))
    print(n1-n2)
button2 = Button(window,command=sub,text="Substract",height=1,width=15,font=("Arial",20))
button2.pack()
def multi():
    n1 = int(text1.get("1.0","end-1c"))
    n2 = int(text2.get("1.0","end-1c"))
    print(n1*n2)
button3 = Button(window,command=multi,text="Multiply",height=1,width=15,font=("Arial",20))
button3.pack()
def div():
    n1 = int(text1.get("1.0","end-1c"))
    n2 = int(text2.get("1.0","end-1c"))
    print(n1/n2)
button4 = Button(window,command=div,text="Divide",height=1,width=15,font=("Arial",20))
button4.pack()

window.mainloop()
