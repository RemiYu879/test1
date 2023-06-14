import tkinter as tk

root=tk.Tk()
root.geometry("500x300")

canvas=tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_oval(50,50,100,100)
canvas.create_line(75,100,75,130)
canvas.create_line(75,130,100,155)
canvas.create_line(75,130,50,155)
canvas.create_line(75,110,100,100)
canvas.create_line(75,110,50,100)


root.mainloop()