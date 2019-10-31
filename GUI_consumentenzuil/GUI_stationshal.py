from tkinter import *
from Twitter_API.Request_Response_Tweets import fetch_tweets

root = Tk()

label = Label(master=root,
              text=fetch_tweets()[0],
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'))

label2 = Label(master=root,
              text=fetch_tweets()[1],
              background='blue',
              foreground='yellow',
              font=('Helvetica', 16, 'bold italic'))

label3 = Label(master=root,
              text=fetch_tweets()[2],
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'))

label4 = Label(master=root,
              text=fetch_tweets()[3],
              background='blue',
              foreground='yellow',
              font=('Helvetica', 16, 'bold italic'))

label5 = Label(master=root,
              text=fetch_tweets()[4],
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'))

label6 = Label(master=root,
              text=fetch_tweets()[5],
              background='blue',
              foreground='yellow',
              font=('Helvetica', 16, 'bold italic'))


label.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()


root.mainloop()