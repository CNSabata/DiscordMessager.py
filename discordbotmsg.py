# Thanks to the chap at https://gist.github.com/ianklatzco/769d9e3a991dc2f443a2e105b0157117
# He inspired me to upgrade his code just a little bit

# Post messages through the Discord API via an application's bot account
# The bot must be added on the server and have write permissions to the channel
# You may need to connect with a websocket the first time you run the bot
# Use a library like discord.py to do so

import requests
import json
import os
import sys
import datetime

# User libs
import yesno
import keymod

# Additional testing libs
# import pygame
# from pygame.locals import*
# import keyboard
# from pynput import keyboard


# Settings
logfile = "discordlogs.txt" # Name for the log file
unitelogs = True            # Choose whether or not you want to unite all logs as one or not


# Var init
i = 0
now = datetime.datetime.now()

# Input for channelID and botToken > Improvement in progress for a favorites system
channelID = input("Channel > ") # enable dev mode on discord, right-click on the channel, copy ID
botToken = input("Token > ")    # get from the bot page. must be a bot, not a discord app

# Defining keyboard listener
# def on_press(key):
#     try:
#         pass
#     except AttributeError:
#         pass

# def on_release(key):
#     if key == keyboard.Key.esc:
#         sys.exit("Error message")

# Manual settings - Placeholder for a future favorite system
# channelID = "Uncomment and set channelID here"
if not channelID:
	channelID = "XXXXXXXXXXXXXXXXXX"
	print("Using default channel ID.")

# botToken = "Uncomment and set botToken here"
if not botToken:
	botToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	print("Using default bot token.")


# Building the URL for the JSON delivery
baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken),
            "User-Agent":"DiscordBotMsg (http://falkensmaze.net, v0.1)",
            "Content-Type":"application/json", }


# Showing the user we're connected
# since at this point if we have no error
# it probably means we are
print("Connected.")
logs = yesno.query_yes_no("Save logs to a file? (Default is N)", "no") # Asking the user for a logfile in file or term
print("Starting message loop. Press ESC to quit before message is sent.")                     # Informing the user the loop has started


# Checking whether or not user wants logs
if logs == False:
    print("Okay, no logs.")

else:
    print("Showing logs in file : ")
    print(os.getcwd()+logfile)


# Main loopy jam
while 1:

    getch = keymod._Getch()
    key = getch()
    if (key == '\x1b'):
       print("quit")
       sys.exit()
    else:
       message = input("> ") # Raw message input
       if (message == "^["):
           sys.exit()

    try:
        if(message != "^["):
            POSTedJSON = json.dumps ( {"content":message} )
            r = requests.post(baseURL, headers = headers, data = POSTedJSON)
    except NameError:
        sys.exit()

    if logs == False:
        if unitelogs:
            try:
                with open(logfile, 'a') as log:
                    log.write(now.strftime("%Y-%m-%d %H:%M"))
                    log.write("=================================================")
                    log.write("> "+message)
            except IOError:
                with open(logfile, 'w+') as log:
                    log.write("File created on "+now)
                    log.write("=================================================")
                    log.write("> "+message)
        else:
            try:
                with open(logfile + now.year + now.month + now.day + now.hour + "h" + now.minute, 'a') as log:
                    log.write(now.strftime("%Y-%m-%d %H:%M"))
                    log.write("=================================================")
                    log.write("> "+message)
            except IOError:
                with open(logfile + now.year + now.month + now.day + now.hour + "h" + now.minute, 'w+') as log:
                    log.write("File created on "+now)
                    log.write("=================================================")
                    log.write("> "+message)

    elif logs == True: # If the user selected no to the log menu
        pass



# Different keyboard capture methods i've tried.
# Pretty interesting when you look into it.
# while True:
#     DISPLAYSURF = pygame.display.set_mode((50,10))
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#
#     if keyboard.is_pressed('esc'):
#         break
#         print("quitting")
#
#     if i<2:
#         interrupt = input("Starting message loop. Press ESC to quit.")
#     else:
#         interrupt = input("Press ESC to quit.")
#
#     if interrupt is "Q" or interrupt is "q" or interrupt is "^]":
#         print("Quitting")
#         sys.exit()
#     else:
#
#     with Listener(on_release=on_release) as listener:
#         listener.join()

print("EOF (This message shouldn't even appear, how did you even got there?)")
