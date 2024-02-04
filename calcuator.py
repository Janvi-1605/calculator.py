import tkinter
from tkinter import *

def click(event):
    global scvalue
    Text=event.widget.cget("text")
    print(Text)
    if Text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif Text =="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+Text)
        screen.update()

root=Tk()
root.title("Calculator")
root.geometry("450x650")
root.config(bg="#000000")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=10, pady=10, padx=10 )

       # ************ 9/8/7 ***********
f=Frame(root, bg="black")
b=Button(f, text="9",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="8",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="7",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="*",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)
f.pack()
        # *************6/5/4 *********************
f=Frame(root, bg="black")
b=Button(f, text="6",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="5",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="4",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="+",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)
f.pack()
         # *******************3/2/1 *******************
f=Frame(root, bg="black")
b=Button(f, text="3",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="2",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="1",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="-",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)
f.pack()
   #**********0-=-/*************
f=Frame(root, bg="black")
b=Button(f, text="0",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text=".",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="%",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="/",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)
f.pack()
        #************** c&= *********************
f=Frame(root, bg="black")
b=Button(f, text="C",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f, text="=",padx=20, pady=20, font= "lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()