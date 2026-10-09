
from tkinter import *

# Create window
window = Tk()
window.title("Event Handler")
window.geometry("300x200")

# Function to change background
def handle_click(event):
    window.config(bg="lightblue")
    print("The button was clicked!")

# Create button
button = Button(text="Click me!")
button.pack()

# Bind click event
button.bind("<Button-1>", handle_click)

# Start GUI
window.mainloop()