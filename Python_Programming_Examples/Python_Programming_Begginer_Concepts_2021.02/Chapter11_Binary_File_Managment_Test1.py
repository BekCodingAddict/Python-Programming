from tkinter import*
window=None
canvas=None

xSize,ySize=256,256
window=Tk()
canvas=Canvas(window,height=xSize,width=ySize)
paper=PhotoImage(width=xSize,height=ySize)
canvas.create_image((xSize/2,ySize/2),image=paper,state="normal")


canvas.pack()
window.mainloop()