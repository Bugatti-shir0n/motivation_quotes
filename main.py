import tkinter as tk
import requests
import time

while True:
   response = requests.get("https://zenquotes.io/api/random").json()
   quote = response[0]['q']

   window = tk.Tk()
   window.title("Pytivator")
   window.config(padx=30, pady=30)

   quote_lbl = tk.Label(text=quote, font=(25))
   quote_lbl.pack()

   window.after(1000, window.destroy)
   window.mainloop()
  
   time.sleep(5)