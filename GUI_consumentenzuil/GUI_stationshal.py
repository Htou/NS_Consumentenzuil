from tkinter import *
from Twitter_API.Request_Response_Tweets import fetch_tweets  # pakt de resultaat van fetch_tweets list.

root = Tk()

stock = []
for i in range(len(fetch_tweets())):  # loopt door lijst van list obejects van fetch_tweets.
    label = Label(master=root,  # Maakt label aan van welke list index
                  text=fetch_tweets()[i],  # pakt strings uit list en gebruikt ze als text
                  background='#BCA136',
                  foreground='white',
                  font=('Helvetica', 16, 'bold'))
    label.grid(row=i, column=0, pady=5)  # layout van labels
    stock.append(label)  # slaat alle labels op in stock list
root.mainloop()
