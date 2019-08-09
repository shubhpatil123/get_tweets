import tkinter as tk
import os

master = tk.Tk()
tk.Label(master, 
         text="Username").grid(row=0)
tk.Label(master, 
         text="TweetCount").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)




tk.Button(master, 
          text='Submit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
master.mainloop()

os.system('python my_edit.py')

