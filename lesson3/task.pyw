from tkinter import *
root=Tk()
def summa(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t3['text']=str(x1+x2)
def delet(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t4['text']=str(x1/x2)
def subtraction(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t5['text']=str(x1-x2)
def multiplication(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t6['text']=str(x1*x2)
def clear(event):
    e1.delete(0,END)
    e2.delete(0,END)
t1=Label(root,text='ввeдите первое число')
t1.pack()
e1=Entry(root)
e1.pack(pady=5)
t2=Label(root,text='введите второе число')
t2.pack(pady=5)
e2=Entry(root)
e2.pack(pady=5)
btn=Button(root,text='сложить',width=10,font="Arial 14")
btn.pack(pady=5)
btn.bind("<Button-1>",summa)
t3=Label(root,font='Arial 20')
t3.pack()
btn2=Button(root,text='делить',width=10,font='Arial 14')
btn2.pack(pady=5)
btn2.bind("<Button-1>",delet)
t4=Label(root,font='Arial 20')
t4.pack()
btn3=Button(root,text='вычитание',width=10,font='Arial 14')
btn3.pack(pady=5)
btn3.bind("<Button-1>",subtraction)
t5=Label(root,font='Arial 20')
t5.pack()
btn4=Button(root,text='умножение',width=10,font='Arial 14')
btn4.pack(pady=5)
btn4.bind("<Button-1>",multiplication)
t6=Label(root,font='Arial 20')
t6.pack()
btn5=Button(root,text='очистить',width=10,font='Arial 14')
btn5.pack(pady=5)
btn5.bind("<Button-1>",clear)
root.mainloop()
