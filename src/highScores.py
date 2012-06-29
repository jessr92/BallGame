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
    from tkinter.messagebox import showerror
except ImportError:
    # Python 2.x
    from Tkinter import * # @UnusedWildImport
    from tkMessageBox import showerror
from traceback import print_exc


def createScoreWindow(highScoreTop):
    # Define details for the canvas widget.
    highScoreCanvas = Canvas(highScoreTop, width=800, height=500)
    highScoreCanvas.pack()
    # Define details for the menu bar.
    menubar = Menu(highScoreTop)
    menuFont = "Calibri", 12
    menubar.add_command(label="Quit", command=highScoreTop.destroy, \
                         font=menuFont)
    highScoreTop.config(menu=menubar)
    return highScoreCanvas


def sortList(list):
    # Make the second element (score) of each inner list an integer.
    for number in range(len(list)):
        list[number][1] = int(list[number][1])


    # Return second element (score) of inner list.
    def sort_inner(inner):
        return inner[1]


    # Sort by second element (score) of inner list.
    list.sort(key=sort_inner)

    # Reverse list so it's ordered in descending order of score.
    orderedList = []
    for number in range(len(list)):
        orderedList += [list[len(list) - number - 1]]
    return orderedList


def highScores():
    # Define details for the window (size and title)
    titleFont = "Calibri", 14
    otherFont = "Calibri", 12
    filename = "resources/scores.txt"
    highScoreTop = Toplevel(takefocus=True)
    highScoreTop.title('Ball Game - High scores')
    highScoreTop.minsize(800, 500)
    highScoreTop.maxsize(800, 500)
    highScoreTop.geometry = highScoreTop.minsize
    highScoreTop.resizable(0, 0)
    highScoreCanvas = createScoreWindow(highScoreTop)

    # Attempt to open scores file for reading.
    try:
        file = open(filename, "r")
    except:
        file = ""
        print_exc(file=open("errlog.txt", "a"))
        showerror("Error - Failed to load scores", "I could not load the " \
        + "scores because scores.txt could not be found. " \
        + "A traceback has been written to errlog.txt in the program's " \
        + "directory.")

    easyScores = []
    mediumScores = []
    difficultScores = []
    uberScores = []
    aloneScores = []

    # Create headings for each score category.
    highScoreCanvas.create_text(250, 16, text=("Easy Scores:"), \
                    font=titleFont)
    highScoreCanvas.create_text(550, 16, text=("Medium Scores:"), \
                    font=titleFont)
    highScoreCanvas.create_text(250, 160, text=("Difficult Scores:"), \
                    font=titleFont)
    highScoreCanvas.create_text(550, 160, text=("Uber Scores:"), \
                    font=titleFont)
    highScoreCanvas.create_text(250, 294, text=("Alone Scores:"), \
                    font=titleFont)

    # If file was opened successfully:
    if file != "":
        for line in file:
            # Split line into list with new element after every @
            # (first element is user name, second element is score,
            # third element is computer level).
            line = line.split("@")

            # Add name and score to appropriate list.
            if str(line[2]) == "easy\n":
                easyScores += [line[0:2]]

            if str(line[2]) == "medium\n":
                mediumScores += [line[0:2]]

            if str(line[2]) == "difficult\n":
                difficultScores += [line[0:2]]

            if str(line[2]) == "uber\n":
                uberScores += [line[0:2]]

            if str(line[2]) == "alone\n":
                aloneScores += [line[0:2]]

        # Order each list by score in descending order.
        easyScores = sortList(easyScores)
        mediumScores = sortList(mediumScores)
        difficultScores = sortList(difficultScores)
        uberScores = sortList(uberScores)
        aloneScores = sortList(aloneScores)

        # Display the top five scores for each category (try/except is just
        # in case less than five games in a category have been played.
        for count in range(5):
            try:
                highScoreCanvas.create_text(250, (40 + (count * 20)), \
                text=(easyScores[count][0] + ": " + \
                str(easyScores[count][1])), font=otherFont)
            except Exception:
                pass

            try:
                highScoreCanvas.create_text(550, (40 + (count * 20)), \
                text=(mediumScores[count][0] + ": " + \
                str(mediumScores[count][1])), font=otherFont)
            except Exception:
                pass

            try:
                highScoreCanvas.create_text(250, (184 + (count * 20)), \
                text=(difficultScores[count][0] + ": " + \
                str(difficultScores[count][1])), font=otherFont)
            except Exception:
                pass

            try:
                highScoreCanvas.create_text(550, (184 + (count * 20)), \
                text=(uberScores[count][0] + ": " + \
                str(uberScores[count][1])), font=otherFont)
            except Exception:
                pass

            try:
                highScoreCanvas.create_text(250, (318 + (count * 20)), \
                text=(aloneScores[count][0] + ": " + \
                str(aloneScores[count][1])), font=otherFont)
            except Exception:
                pass
