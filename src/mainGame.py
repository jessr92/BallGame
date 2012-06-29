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
from os import listdir
from random import randrange
from traceback import print_exc


bonusTrigger = False
count = 0
xMin = 10
yMin = 0
xMax = 790
yMax = 370


class ball():
    # Ball object class
    def __init__(self):
        self.diameter = 20
        self.hitTop = False
        self.isHuman = True
        self.isPlaying = False
        self.powerup = None
        self.powerupTime = 0
        self.score = 0
        self.speed = 8
        self.oldSpeed = 8
        self.userName = ""
        self.xPos = 20
        self.yPos = 20
        self.moveLeft = False
        self.moveRight = False

def ballGame(computerPlaying, computerLevel, userName, canvas, mainGameWindow):
    # Set starting variables and decide which picture to show as
    # the game background (bonusTrigger and count here just in case
    # user quit game midway last time).
    global bonusTrigger, count
    bonusTrigger = False
    success = True
    count = 0
    level = 0

    try:
        dirList = listdir("backgrounds/")
    except Exception:
        success = False
        print_exc(file=open("errlog.txt", "a"))
        showerror("Wrong directory", "You appear to have forgotten to cd to " \
        + "the correct directory. A traceback has been written to " \
        + "errlog.txt in the program's directory.")

    if success:
        photos = []
        # Find *.gif files in background directory
        for element in dirList:
            if str(element)[-4:] == ".gif":
                photos += [element]
                randomNumber = randrange(0, len(photos))
                whichPicture = "backgrounds/" + str(photos[randomNumber])

        try:
            photo1 = PhotoImage(file=whichPicture)
            canvas.create_image((xMin + xMax) / 2, \
                            (yMin + yMax) / 2, image=photo1)
        except Exception:
            print_exc(file=open("errlog.txt", "a"))
            showerror("Error - Failed to load image", "I could not load the " \
            + "background images for the game environment. The game will " \
            + "still load, just with a blank background. A traceback has " \
            + "been written to errlog.txt in the program's directory.")

    # Define specific values for each ball and make the ball objects global 
    # (for call back only, otherwise pass variables in).
    global playerOne, playerTwo
    playerOne = ball()
    playerOne.isPlaying = True
    playerOne.userName = userName
    playerTwo = ball()

    if computerPlaying == True:
        playerTwo.isHuman = False
        playerTwo.isPlaying = True
        if computerLevel == "easy":
            playerTwo.speed = 2
            playerTwo.oldSpeed = 2
        elif computerLevel == "medium":
            playerTwo.speed = 4
            playerTwo.oldSpeed = 4
        elif computerLevel == "difficult":
            playerTwo.speed = 6
            playerTwo.oldSpeed = 6
        elif computerLevel == "uber":
            playerTwo.speed = 8
            playerTwo.oldSpeed = 8

    # Define specific values for each ball if the user name is "TechDemo".
    if playerOne.userName == "TechDemo":
        playerOne.speed = 15
        playerOne.oldSpeed = 15
        playerOne.isHuman = False
        if computerLevel == "alone":
            playerTwo.isPlaying = False
        else:
            playerTwo.isHuman = False
            playerTwo.isPlaying = True

    # Display initial score and level.
    playerOneText = ("Score " + str(playerOne.score) \
                    + " and on level " + str(level))
    theFont = "Calibri", 12
    playerOneInformation = canvas.create_text(400, 385, \
                            text=playerOneText, font=theFont)
    powerupText = "You currently have no powerups."
    powerupInformation = canvas.create_text(400, 405, \
                            text=powerupText, font=theFont)
    # Display count down from 3 prior to starting the game.
    massiveFont = "Calibri", 200
    for number in range(3):
        counter = canvas.create_text(390, 185, text=str(3 - number), \
                    font=massiveFont, fill="white")
        canvas.update()
        canvas.after(1000)
        canvas.delete(counter)

    canvas.delete(playerOneInformation)
    canvas.delete(powerupInformation)
    # Keep playing the game until one of the balls in 
    # play hits the top of the game area.
    while playerOne.hitTop == False and playerTwo.hitTop == False:
        playerOne, playerTwo, level = drawLine(playerOne, \
                                        playerTwo, canvas, level)

    gameOver(computerLevel, playerOne, playerTwo, computerPlaying, \
             canvas, level, mainGameWindow)


def gameOver(computerLevel, playerOne, playerTwo, computerPlaying, \
             canvas, level, mainGameWindow):
    theFont = "Calibri", 12

    # If player one lost against player two:
    if playerOne.hitTop == True and playerTwo.hitTop == False \
    and playerTwo.isPlaying == True:
        if computerLevel == "easy" or computerLevel == "uber":
            canvas.create_text(400, 385, text=("Game over, you lost. " \
            + "Your final score is " + str(playerOne.score) \
            + ". You reached level " + str(level) + " against an " \
            + str(computerLevel) + " computer."), width=780, font=theFont)
        elif computerLevel == "medium" or computerLevel == "difficult":
            canvas.create_text(400, 385, text=("Game over, you lost. " \
            + "Your final score is " + str(playerOne.score) \
            + ". You reached level " + str(level) + " against a " \
            + str(computerLevel) + " computer."), width=780, font=theFont)

    # If only player one was playing:
    if playerOne.hitTop == True and computerLevel == "alone":
        canvas.create_text(400, 385, text=("Game over. Your final score is " \
        + str(playerOne.score) + ". You reached a level of " \
        + str(level) + "."), width=780, font=theFont)

    # If player two lost
    if playerTwo.hitTop == True:
        playerOne.score += 20000
        canvas.create_text(400, 385, text=("Game over, you won! " \
        + "Your final score is " + str(playerOne.score) \
        + ". You reached level " + str(level) + "."), width=780, font=theFont)

    # Show the newly created text for five seconds then 
    # destroy the window and save the score.
    canvas.update()
    canvas.after(5000)
    canvas.destroy()
    writeScore(playerOne, computerLevel, computerPlaying, mainGameWindow)


def writeScore(playerOne, computerLevel, computerPlaying, mainGameWindow):
    filename = "resources/scores.txt"

    # Work out what to save to the text file
    if computerPlaying == False:
        nameAndScore = str(playerOne.userName) + \
        "@" + str(playerOne.score) + "@alone"
    elif computerPlaying == True and (computerLevel == "easy" or \
                                        computerLevel == "uber"):
        nameAndScore = str(playerOne.userName) + \
        "@" + str(playerOne.score) + "@" + str(computerLevel)
    else:
        nameAndScore = str(playerOne.userName) + \
        "@" + str(playerOne.score) + "@" + str(computerLevel)

    # Convert the variable to be saved to string, remove punctuation,
    # add a new line character then try and save it to the specified file.
    nameAndScore = str(nameAndScore)
    nameAndScore += "\n"

    try:
        file = open(filename, "a")
        file.writelines(nameAndScore)
        file.writelines("")
        file.close()
    except Exception:
        print_exc(file=open("errlog.txt", "a"))
        showerror("Error - Failed to write score", "I could not your score " \
        + "to the scores file. A traceback has been written to errlog.txt "\
        + "in the program's directory.")

    mainGameWindow.destroy()


def drawLine(playerOne, playerTwo, canvas, level):
    # Set values for count, starting yPos for line and 
    # xPos for the gap in the line.
    global count
    count = count + 1
    yLine = yMax
    gapX = randrange(xMin, xMax - (3 * playerOne.diameter), playerOne.diameter)
    interval = int(1000 / 120)
    # Power up on new level if computer is playing.
    if count > 0 and count % 5 == 0 and playerOne.powerupTime == 0:
        playerOne = findPowerup(playerOne, playerTwo)
    elif count > 0 and count % 5 == 0 and playerOne.powerupTime != 0:
        playerOne.powerupTime += 1000

    # Until the line goes off the top of the screen:
    while yLine > yMin:
        level = int(count / 5) + 1

        # Call appropriate function based on whether or not 
        # the player is human or computer.
        if playerOne.isPlaying == True and playerOne.isHuman == True:
            playerOne = humanMove(playerOne, yLine, gapX)

        if playerOne.isPlaying == True and playerOne.isHuman == False:
            playerOne = computerMove(playerOne, yLine, gapX)

        if playerTwo.isPlaying == True and playerTwo.isHuman == True:
            playerTwo = humanMove(playerTwo, yLine, gapX)

        if playerTwo.isPlaying == True and playerTwo.isHuman == False:
            playerTwo = computerMove(playerTwo, yLine, gapX)

        # If both balls are at the bottom of the game area and are fully 
        # overlapping, move player one by half a diameter to the right.
        if playerOne.xPos == playerTwo.xPos \
        and playerOne.yPos + playerOne.diameter == yMax \
        and playerTwo.yPos + playerTwo.diameter == yMax:
            playerOne.xPos += int(playerOne.diameter / 2)

        # Limit the speed the line moves up at to 15px per cycle.
        if level > 15:
            level = 15

        # Reduce time left for powerup.
        if playerOne.powerupTime >= 0:
            playerOne.powerupTime -= interval

        # When powerup has finished, go back to old speeds.
        if playerOne.powerupTime < 0:
            playerOne.powerupTime = 0
            playerOne.powerup = None
            playerOne.speed = playerOne.oldSpeed
            playerTwo.speed = playerTwo.oldSpeed

        # Create image of the player(s) ball(s) if they are playing.
        if playerOne.isPlaying == True:
            ball = canvas.create_oval(playerOne.xPos, playerOne.yPos, \
                playerOne.xPos + playerOne.diameter, \
                playerOne.yPos + playerOne.diameter, fill="red")

        if playerTwo.isPlaying == True:
            ball2 = canvas.create_oval(playerTwo.xPos, playerTwo.yPos, \
                playerTwo.xPos + playerTwo.diameter, \
                 playerTwo.yPos + playerTwo.diameter, fill="blue")

        # Player one receives a score bonus if there ball is lower 
        # down the game area than player two.
        if playerOne.isPlaying == True and playerTwo.isPlaying == True \
        and playerOne.yPos > playerTwo.yPos:
            playerOne.score += level

        # Create both sections of the line.
        line = canvas.create_line(xMin, yLine, gapX, yLine, fill="white", \
                width=6, stipple='questhead')
        line2 = canvas.create_line(gapX + 3 * playerOne.diameter, yLine, \
                xMax, yLine, fill="white", width=6, stipple='questhead')

        # Display player one's score and how fast the line is moving.
        theFont = "Calibri", 12
        playerOneText = ("Score " + str(playerOne.score) \
                         + " and on level " + str(level))
        playerOneInformation = canvas.create_text(400, 385, \
                                text=playerOneText, font=theFont)

        # Tell player if they have a powerup
        if playerOne.powerupTime != 0:
            time = int(playerOne.powerupTime / 1000) + 1
        else:
            time = 0

        if playerOne.powerup != None and time != 1:
            powerupText = ("You currently have the powerup: " \
            + str(playerOne.powerup) + " for " + str(time) + " seconds.")
            powerupInformation = canvas.create_text(400, 405, \
                        text=powerupText, font=theFont)
        elif time == 1:
            powerupText = ("You currently have the powerup: " \
            + str(playerOne.powerup) + " for " + str(time) + " second.")
            powerupInformation = canvas.create_text(400, 405, \
                        text=powerupText, font=theFont)
        else:
            powerupText = "You currently have no powerups."
            powerupInformation = canvas.create_text(400, 405, \
                        text=powerupText, font=theFont)

        canvas.update()
        canvas.after(interval)
        playerOne.score += level
        yLine -= int(level / 2) + 1

        # Delete all objects created in this iteration of the loop.
        canvas.delete(line)
        canvas.delete(line2)
        canvas.delete(playerOneInformation)
        canvas.delete(powerupInformation)
        if playerOne.isPlaying == True:
            canvas.delete(ball)
        if playerTwo.isPlaying == True:
            canvas.delete(ball2)

        # If either the line or one of the balls has gone off the 
        # top of the game area, quit the loop.
        if yLine <= yMin or playerOne.hitTop == True or \
        playerTwo.hitTop == True:
            return playerOne, playerTwo, level


def findPowerup(playerOne, playerTwo):
    filename = "resources/powerups.txt"
    powerupsAvailable = []

    try:
        file = open(filename, "r")
    except Exception:
        file = ""
        print_exc(file=open("errlog.txt", "a"))
        showerror("Error - Failed to load powerups", "I could not load the " \
        + "powerups because powerups.txt could not be found. A traceback has "\
        + "been written to errlog.txt in the program's directory.")

    # Add floating point numbers to powerupsAvailable list
    for line in file:
        powerupsAvailable += [float(str(line[:-1]))]

    # Obtain a random powerup
    number = randrange(0, len(powerupsAvailable))
    playerOne.powerup = powerupsAvailable[number]

    # If the value would result in a speed increase, give it to the user.
    if playerOne.powerup > 1:
        playerOne.speed = int(playerOne.speed * playerOne.powerup)
        playerOne.powerupTime = 5000 * (playerOne.powerup - 1)
        playerOne.powerup = "speed you up to " \
        + str(powerupsAvailable[number]) + "x speed"
    # If the value would result in a speed decrease, give it to the computer.
    elif playerOne.powerup < 1 and playerTwo.isPlaying == True:
        playerTwo.speed = int(playerTwo.speed * playerOne.powerup)
        playerOne.powerupTime = 5000 * playerOne.powerup
        playerOne.powerup = "slow computer down to "\
        + str(powerupsAvailable[number]) + "x speed"
    # If the value wouldn't result in a speed change, add 1000 to user's score.
    elif playerOne.powerup == 1:
        playerOne.score += 1000
        playerOne.powerupTime = 0
        playerOne.powerup = "score bonus of 1000"

    return playerOne


def humanMove(ball, yLine, gapX):
    # Let the ball fall down by 10px per cycle.
    ball.yPos += 10

    # If ball is off the left side of the game area then move it back inside.
    if ball.xPos < xMin:
        ball.xPos = xMin
        ball.moveLeft = False


    if ball.moveLeft and ball.isHuman and ball.isPlaying:
        ball.xPos -= ball.speed

    if ball.moveRight and ball.isHuman and ball.isPlaying:
        ball.xPos += ball.speed


    # If ball is off the right side of the game area then move it back inside.
    if ball.xPos + ball.diameter > xMax:
        ball.xPos = xMax - ball.diameter
        ball.moveRight = False

    # If ball is off the top side of the game area then game is over.
    if ball.yPos <= yMin:
        ball.hitTop = True

    # If ball is not over the gap then make it sit on the line 
    # (unless below the line by more than 15px).
    if ball.yPos + ball.diameter >= yLine - 3 \
    and ball.yPos + ball.diameter <= yLine + 15 \
    and (ball.xPos < gapX \
    or ball.xPos + ball.diameter > (gapX + (3 * ball.diameter))):
        ball.yPos = yLine - ball.diameter - 3

    # If ball is off the bottom of the game area then move it back inside.
    if ball.yPos + ball.diameter >= yMax:
        ball.yPos = yMax - ball.diameter
    return ball


def computerMove(ball, yLine, gapX):
    # Detection of whether or not the ball is out of the game area 
    # is the same for computer and human balls.
    ball = humanMove(ball, yLine, gapX)

    # If ball is left of gap, move it closer to the gap.
    if ball.xPos <= gapX:
        ball.xPos += ball.speed

    # If ball is right of the gap, move it closer to the gap.
    if ball.xPos + ball.diameter >= (gapX + 3 * ball.diameter):
        ball.xPos -= ball.speed
    return ball


def callback(event):
    # Move appropriate ball based on which key was pressed.
    if event.keysym == "Left" and playerOne.isHuman == True:
        playerOne.moveLeft = True
        playerOne.moveRight = False

    if event.keysym == "Right" and playerOne.isHuman == True:
        playerOne.moveLeft = False
        playerOne.moveRight = True

    if event.keysym == "Down" and playerOne.isHuman == True:
        playerOne.moveLeft = False
        playerOne.moveRight = False


def play(userName, computerPlaying, computerLevel):
    # Define details for the window (size and menu options).
    global mainGameWindow
    menuFont = "Calibri", 12
    mainGameWindow = Toplevel(takefocus=True)
    mainGameWindow.title('Ball Game - Main Game')
    mainGameWindow.minsize(800, 500)
    mainGameWindow.maxsize(800, 500)
    mainGameWindow.geometry = mainGameWindow.minsize
    mainGameWindow.resizable(0, 0)
    menubar = Menu(mainGameWindow)
    menubar.add_command(label="Quit", command=mainGameWindow.destroy, \
                        font=menuFont)
    mainGameWindow.config(menu=menubar)

    # Define details for the canvas widget which sits inside the 
    # window (size and which function to call on key press).
    canvas = Canvas(mainGameWindow, width=800, height=500,)
    canvas.bind_all('<Key>', callback)
    canvas.pack()
    ballGame(computerPlaying, computerLevel, userName, canvas, mainGameWindow)
