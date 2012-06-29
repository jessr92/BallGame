'''
Project was conceptualised formally on the 3rd of November 2010
Last updated 12th of January 2011 by Gordon Reid
@title: Ball Game
@author: Gordon Reid - gordon.reid1992@hotmail.co.uk
This code is freely available for anybody to view and edit.
I request that if any code is used that credit is given in an appropriate
fashion (a.k.a my name mentioned in a section similar to this and visible
in the user interface).

Disclaimer:
I, me (and similar) all reference to Gordon Reid
(gordon.reid1992@hotmail.co.uk) unless explicitly stated.
I have not intentionally stolen code, this is all my own work and as a result
the property (programming projects) are solely owned by me.
I accept no responsibility for any damages which may occur from the code.
The code has been tested on my own computer systems running
Ubuntu 10.04 Netbook Edition and Ubuntu 10.10 Desktop Edition x64 without
causing any damage (to files or otherwise).
The code is run at the users own risk.
No support on the use on any of the the projects will be available.
'''


try:
	# Python 3.x
	from tkinter import * # @UnusedWildImport
	from tkinter.messagebox import showerror, showinfo
except ImportError:
	# Python 2.x
	from Tkinter import * # @UnusedWildImport
	from tkMessageBox import showerror, showinfo
from highScores import highScores
from mainGame import play
from string import punctuation
from sys import exit


class createWindow:
	# Root window class.
	def checkDetails(): # @NoSelf
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


	def showAbout(): # @NoSelf
		# Show information about myself and the project.
		showinfo("About", "Currently in development\n\nFree " \
		+ "Programming Project for CS1P University of Glasgow\n\nAuthor:\n" \
		+ "Gordon Reid\n\nContact:\ngordon.reid1992@hotmail.co.uk")


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
