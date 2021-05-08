from tkinter import*

window=Tk(); window.geometry("500x600"); window.title("Python GUI programming")
label1=Label(window,text="Python Gui Programming!",font=("sda",30),fg="red",background="green",width=5,height=3)
label1.pack(side=TOP,fill=BOTH)

button=Button(window,text="Close",background="white",width=15,height=2)
button.pack(side=BOTTOM,padx=100,pady=100,ipadx=10,ipady=5)
checkbutton=Checkbutton(window,text="Turn on/off",background="red")
checkbutton.pack(padx=50,pady=50,ipadx=500,ipady=5)
radiobutton=Radiobutton(window,text="Python",background="blue")
radiobutton.pack(padx=20,pady=30,ipadx=60,ipady=600)
window.mainloop()