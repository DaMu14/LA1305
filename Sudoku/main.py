import tkinter as tk

root = tk.Tk()

# Textausgabe erzeugen
label1 = tk.Label(root, text="Hallo Welt")
label1.pack(side="top")

schaltf1 = tk.Button(root, text="einfach", command=root.destroy)
schaltf1.pack(side="left")
 
schaltf2 = tk.Button(root, text="Mittel")
schaltf2.pack(side="bottom")
schaltf3 = tk.Button(root, text="Schwierig")
schaltf3.pack(side="right")

root.mainloop()