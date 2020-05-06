# Import stuff
import discord
from discord.ext import commands
import random
import datetime as dt

pickCounter = 0
cap1 = None
cap2 = None
team1 = []
team2 = []

def getPickCt():
    return pickCounter

def addToPickCt():
    pickCounter += 1
    return

def setCap1(cap):
    cap1 = cap

def setCap2(cap):
    cap2 = cap

def flipCoin(playerA, playerB):
    if(random.randint(0, 100) > 49):
        print("A")
        return playerA
    print("B")
    return playerB

# Discord Token
TOKEN = "NjE1Njg2MzY4MjM1ODgwNjE4.XrJUuQ.y9Ji2vL2nbj1pdqXIeButX8rn8w"
bot = commands.Bot(command_prefix='!')

# Bot Login
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Command to start scrim
@bot.command()
async def scrim(ctx, cap1, cap2):
    if(len(ctx.message.mentions) != 2):
        print("Invalid captains")
    else:
        if(flipCoin(ctx.message.mentions[0], ctx.message.mentions[1]) == ctx.message.mentions[0]):
            Captain1 = ctx.message.mentions[0]
            Captain2 = ctx.message.mentions[1]
        else:
            Captain1 = ctx.message.mentions[1]
            Captain2 = ctx.message.mentions[0]
        print(Captain1, Captain2)
        cap1 = Captain1
        cap2 = Captain2
        team1.append(Captain1)
        team2.append(Captain1)

# Command to pick teammates
@bot.command()
async def pick(ctx, pick):
    print(getPickCt())
    print(ctx.message.author)
    print(cap1)
    #Check who's picking; if even, cap1, if odd cap2
    # if(getPickCt() % 2 == 0 and ctx.message.author == cap1):
    if(True):
        # ADD CHECK TO MAKE SURE ITS A VALID PICK
        if(ctx.message.mentions[0] in team1 or ctx.message.mentions[0] in team2):
            print("Invalid pick")
            return
        team1.append(ctx.message.mentions[0])
        # addToPickCt()
        print(team1)
        print(team2)
    elif(ctx.message.author == cap2):
        # ADD CHECK TO MAKE SURE ITS A VALID PICK
        if(ctx.message.mentions[0] in team1 or ctx.message.mentions[0] in team2):
            print("Invalid pick")
            return
        team2.append(ctx.message.mentions[0])
        addToPickCt()
        print(team1)
        print(team2)
    else:
        print("Invalid captain")
        return
#Shutdown command---------------------------------------------------------------
@bot.command()
@commands.is_owner()
async def stop(ctx):
    print("Bot is shutting down")
    await ctx.bot.logout()

bot.run(TOKEN)

# Class requirements
# "Game" Class that holds data for scrim
# Keeps track of who the two captains are, whos picking, whos available, what the teams are

# def start(captain1, captain2):#captain 1 will get first pick
#     print(captain1+ " will get first pick: ")
#     counter=0
#     c1list=[captain1]
#     c2list=[captain2]
#     while counter<10:
#         if counter%2 == 0:
#             print(captain1+ ", make your pick with !(discordname)")
#             #now get users input
#             c1list.add(input)
#         else:
#             print(captain2+ ", make your pick with !(discordname)")
#             #now get users input
#             c2list.add(input)
#         counter+=1
#     movePlayers(c1list, c2list)
#
# def movePlayers(c1list, c2list):
#     for player in c1list:
#         TODO
#         #move player into discord labeled "Team 1"
#     for player in c2list:
#         TODO
#         #move player into discord labeled "Team 2"
#
