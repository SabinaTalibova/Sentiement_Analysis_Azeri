from tkinter import *
top = Tk()
RTitle=top.title("Sentiment analyzer")
RWidth=top.winfo_screenwidth()/2
RHeight=top.winfo_screenheight()/2
top.geometry("%dx%d+0+0" % (RWidth, RHeight))






L1 = Label(top, text="Enter the sentnce you want to check")
L1.place(x=250, y=10)
E1 = Entry(top, bd =2)
E1.place(x=200, y=40,width=300)
B1=Button(top,text="Check")
B1.place(x=300, y=70,width=100)

top.mainloop()




