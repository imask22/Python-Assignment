import tkinter
window=tkinter.Tk()
window.title("pic gui")
a="C:\\Users\\Student\\Desktop\\a.png"
icon=tkinter.PhotoImage(file = a)
label=tkinter.Label(window,image=icon)
label.pack()
label1=tkinter.Label(window,image=icon)
label.pack()

label2=tkinter.Label(window,image=icon)
label2.pack()
window.mainloop()

