from tkinter import*
parent =Tk()
###pack method###

'''redbutton=Button(parent,text="Red",fg="red")
redbutton.pack(side=LEFT)
bluebutton=Button(parent,text='Blue',fg="blue")
bluebutton.pack(side=RIGHT)
greebutton=Button(parent,text='Green',fg="green")
greebutton.pack(side=BOTTOM)
yellowbutton=Button(parent,text="yellow",fg="yellow")
yellowbutton.pack(side=TOP)'''
###grid Method###
'''name=Label(parent,text="Name").grid(row=0,column=0)
e1=Entry(parent).grid(row=0,column=1)
password=Label(parent,text="password").grid(row=1,column=0)
e2=Entry(parent).grid(row=1,column=1)
submit=Button(parent,text="Submit").grid(row=4,column=1)'''\
parent.geometry("400x250")
name=Label(parent,text="Name").place(x=30,y=50)
email=Label(parent,text="Email").place(x=30,y=130)
password=Label(parent,text="Password").place(x=30,y=130)
e1.Entry(parent).place(x=80,y=50)
e2.Entry(parent).place(x=80,y=90)
e3.Entry(parent).place(x=95,y=130)
parent.mainloop()