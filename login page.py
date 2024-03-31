# we find the login page:

from tkinter import*
root=Tk()
#root.title(,Login and Registered Page)
root.geometry("450x400")
def login():
    f2=Frame()
    f2.place(x=0,y=0,width="400",height="300")
    u3=Label(f2,text="Login Page",font=("Times",20))
    u3.place(x=150,y=10)
    
    u1=Label(f2,text="Enter the name",font=("Times",20))
    u1.place(x=0,y=100)
    e1=Entry(f2,font=("",20))
    e1.place(x=180,y=100,width=180,height=35)

    u2=Label(f2,text="Enter Password",font=("Times",20))
    u2.place(x=0,y=200)
    e2=Entry(f2,font=("",20))
    e2.place(x=180,y=200,width=180,height=35)
    #e2=Entry(f2)
    #e2.place(x=100,y=100)
    b2=Button(f2,text="<<-",command=home,font=("Times",15),width=5,height=0)
    b2.place(x=0,y=0)
def regis():
    f3=Frame()
    f3.place(x=0,y=0,width="400",height="300")
    u3=Label(f3,text="Registration Page",font=("Times",20))
    u3.place(x=150,y=10)
    
    u1=Label(f3,text="Enter the name",font=("Times",20))
    u1.place(x=0,y=100)
    e1=Entry(f3,font=("",20))
    e1.place(x=180,y=100,width=180,height=35)

    u2=Label(f3,text="Enter Password",font=("Times",20))
    u2.place(x=0,y=200)
    e2=Entry(f3,font=("",20))
    e2.place(x=180,y=200,width=180,height=35)
    u3=Label(f3,text="Enter C.Password",font=("Times",20))
    u3.place(x=0,y=300,)
    e3=Entry(f3,font=("",20))
    e3.place(x=180,y=300,width=180,height=35)
    #e2=Entry(f2)
    #e2.place(x=100,y=100)
    b2=Button(f3,text="<<-",command=home,font=("Times",15),width=5,height=0)
    b2.place(x=0,y=0)
    b3=Button(f3,text="<<-",command=home,font=("Times",15),width=5,height=0)
    b3.place(x=220,y=350)
def home ():
    
    f1=Frame()
    f1.place(x=0,y=0,width="400",height="300")
    b1=Button(f1,text="click!!!",font=("Times",20),command=login)
    b1.place(x=80,y=80,width=80,height=40)
    
    b2=Button(f1,text="Riges",font=("Times",20),command=regis)
    b2.place(x=200,y=80,width=80,height=40)
home()

root.mainloop()
