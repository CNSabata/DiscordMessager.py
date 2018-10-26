# post a message to discord api via a bot
# bot must be added to the server and have write access to the channel
# you may need to connect with a websocket the first time you run the bot
#   use a library like discord.py to do so
import requests
import json

channelID = input("Channel > ") # enable dev mode on discord, right-click on the channel, copy ID
botToken = input("Token > ")    # get from the bot page. must be a bot, not a discord app

# Manual settings
# channelID = "Uncomment and set channelID here"
if not channelID:
	channelID = "420993114325516288"
	print("Using default channel ID.")
# botToken = "Uncomment and set botToken here"
if not botToken:
	botToken = "NDE4OTIwNDM1MzU1NDg0MTcx.Dnz-xQ.r5vgdXUSP6GqR01RwjkZkJt321Q"
	print("Using default bot token.")

baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken),
            "User-Agent":"DiscordBotMsg (http://falkensmaze.net, v0.1)",
            "Content-Type":"application/json", }

print("Connected.")
message = input("> ")

POSTedJSON =  json.dumps ( {"content":message} )

r = requests.post(baseURL, headers = headers, data = POSTedJSON)
print("Sent message : "+message)
