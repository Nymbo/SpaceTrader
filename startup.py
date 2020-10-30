from Tkinter import *
import pygame

from main import main

# Initialize window:
window = Tk()
window.title("Year 2666 startup window")

# Create controls:


# Options frame:
options_frame = Frame(window)
options_frame.pack(side="top")

# Window size dropdown label:
win_size_label = Label(options_frame, text= "Window size:")
win_size_label.grid(column=0, row=0)

# Read available fullscreen modes:
pygame.init()
pygame_modes = pygame.display.list_modes()
modes_list = []
mode_idx = 0
for mode in pygame_modes:
    modes_list.append(str(mode[0]) + " x " + str(mode[1]))

# Populate the modes dropdown:
modes_var = StringVar(window)
modes_var.set(modes_list[0])
modes_dropdown = OptionMenu(options_frame, modes_var, *modes_list)
modes_dropdown.grid(column=1, row=0)


# Define a function for game start:
def startGame():
    mode_string = modes_var.get()
    mode = (int(mode_string.split(" x ")[0]), int(mode_string.split(" x ")[1]))
    main(mode)

# Create start button:
start_button = Button(window, text="Start!", command=startGame)
start_button.pack()



window.mainloop()




