from tkinter import *
from Twitter_API.Request_Response_Tweets import fetch_tweets

fetch_tweets()

root = Tk()

label = Label(master=root,
              text=fetch_tweets(),
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'))
label.pack()

root.mainloop()
