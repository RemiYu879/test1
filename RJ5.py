import tkinter as tk

root=tk.Tk()
root.geometry("500x300")

canvas=tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_oval(50,50,100,100,tag="hito")
canvas.create_line(75,100,75,130,tag="hito")
canvas.create_line(75,130,100,155,tag="hito")
canvas.create_line(75,130,50,155,tag="hito")
canvas.create_line(75,110,100,100,tag="hito")
canvas.create_line(75,110,50,100,tag="hito")

def move():
    canvas.move("hito", 5, 0)
    canvas.after(100, move)

def clk():
    move()

button = tk.Button(root, text="GO", command=clk)
button.pack()


root.mainloop()