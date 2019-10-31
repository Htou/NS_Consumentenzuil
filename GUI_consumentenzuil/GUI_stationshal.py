from t
from tkinter import *

root = Tk()

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

root.overrideredirect(1)
root.geometry('%dx%d+0+0' % (screenWidth, screenHeight))
root.configure(background='#000000')  # black


canvas = Canvas(
    background='#000000',  # black
    borderwidth=-5,
    height=500,
    relief='flat',
    width=500)

canvas.pack(expand=1, fill=BOTH)

root.mainloop()
