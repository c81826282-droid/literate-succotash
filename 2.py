from tkinter import *


window = Tk()
window.title("EVENT HANDLER")
window.geometry("100x100")
def virus(event):
    print("thankfully tanav clicked the button!!!!")
button = Button(text="Click Me!")
button.pack()
button.bind("<Button-1>", virus)
window.mainloop()