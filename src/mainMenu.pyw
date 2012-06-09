'''
    Ball Game - Python implementation of a simple ball-through-the-hole game.
    Copyright (C) 2012  Gordon Reid

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    The author can be contacted via email:
    gordon.reid1992@hotmail.co.uk
    OR
    1002536r@student.gla.ac.uk
'''
from highScores import highScores
from mainGame import play


try:
    # Python 3.x
    from tkinter import *
    from tkinter.messagebox import showerror, showinfo
except ImportError:
    # Python 2.x
    from Tkinter import *
    from tkMessageBox import showerror, showinfo


from string import punctuation
from sys import exit


class createWindow:
    # Root window class.
    def checkDetails():  # @NoSelf
        # Obtain user name from entry box and check to see if it's valid
        # (user name cannot contain punctuation)
        userName = entryUserName.get()
        for char in userName:
            if char in punctuation:
                showerror("Error - Invalid User name", \
                "Your user name is invalid. It can not contain these " \
                + "characters:\n" + str(punctuation))
                userName = ""
                return

        # Obtain radio button selection and take appropriate element from
        # list as the computer's difficulty level.
        if (v.get() == 1 or v.get() == 2 or v.get() == 3 or v.get() == 4 \
        or v.get() == 5) and userName != "":
            levels = ["alone", "easy", "medium", "difficult", "uber"]
            if v.get() == 1:
                computerPlay = False
            else:
                computerPlay = True
            computerLevel = levels[v.get() - 1]
            play(userName, computerPlay, computerLevel)
        else:
            showerror("Error - Missing Information", \
            "Please fill in your name and check one of the radio buttons.")

    def showAbout():  # @NoSelf
        # Show information about myself and the project.
        showinfo("About", "Currently in development\n\nOriginally for Free " \
        + "Programming Project for CS1P University of Glasgow\n\nAuthor:\n" \
        + "Gordon Reid\n\nContact:\ngordon.reid1992@hotmail.co.uk\n" \
        + "1002536r@student.gla.ac.uk")

    # Define details for the window (size and menu options).
    root = Tk()
    root.title('Ball Game - Main Menu')
    root.minsize(800, 500)
    root.maxsize(800, 500)
    root.geometry = root.minsize
    root.resizable(0, 0)

    # Define the fonts to use
    titleFont = "Calibri", 16
    menuFont = "Calibri", 12
    otherFont = "Calibri", 14

    # Create a top level menu
    menubar = Menu(root)
    menubar.add_command(label="Play", command=checkDetails, font=menuFont)
    menubar.add_command(label="Show High Scores", command=highScores, \
                    font=menuFont)
    menubar.add_command(label="Quit", command=exit, font=menuFont)
    menubar.add_command(label="About", command=showAbout, font=menuFont)
    root.config(menu=menubar)

    # Add title and instructions
    Label(text='Ball Game', font=titleFont).pack(pady=15)
    instructions = "Instructions: \n Please use the left and right arrow " \
    + "keys to move the ball towards the gap in the platform. The down " \
    + "arrow key stops the ball. \n You are the red ball, Computer is the " \
    + "blue ball. \n Before you begin please fill in the information " \
    + "below. \n Good luck! \n"
    Label(text=instructions, wraplength=700, font=otherFont) .pack()

    # User name entry label
    textFrame = Frame(root)
    entryUserNameLabel = Label(textFrame)
    entryUserNameLabel["text"] = "Please enter your name:"
    entryUserNameLabel["font"] = otherFont
    entryUserNameLabel.pack(side=LEFT)
    textFrame.pack()

    global entryUserName, v

    # User name entry box
    entryUserName = Entry(textFrame)
    entryUserName['width'] = 50
    entryUserName.pack(side=RIGHT)

    # Computer difficulty radio buttons label
    anotherTextFrame = Frame(root)
    radioButtonsLabel = Label(anotherTextFrame)
    radioButtonsLabel["text"] = "\nPlease select one of the options below:"
    radioButtonsLabel["font"] = otherFont
    radioButtonsLabel.pack(side=BOTTOM)
    anotherTextFrame.pack()

    # Computer difficulty radio buttons
    v = IntVar()
    Radiobutton(root, text="Alone", variable=v, value=1, \
            font=otherFont).pack()
    Radiobutton(root, text="Easy Computer", variable=v, value=2, \
            font=otherFont).pack()
    Radiobutton(root, text="Medium Computer", variable=v, value=3, \
            font=otherFont).pack()
    Radiobutton(root, text="Difficult Computer", variable=v, value=4, \
            font=otherFont).pack()
    Radiobutton(root, text="Uber Computer", variable=v, value=5, \
            font=otherFont).pack()
    root.mainloop()
