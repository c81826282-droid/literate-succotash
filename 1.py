from tkinter import *


window = Tk()
window.title("EVENT HANDLER")
window.geometry("100x100")


def handle_keypress(event):
    """Print the characters the player typed"""
    print(event.char)

window.bind("<Key>", handle_keypress)





window.mainloop()