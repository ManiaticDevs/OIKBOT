
import os
import time
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from keep_alive import keep_alive

client = discord.Client()

client = commands.Bot(command_prefix = '`')

@client.event
async def on_ready():
    print("he has arisen")
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") 

@client.command()
async def wakeup(ctx):
    await ctx.send("what u wanttttttttttt") 

@client.command()
async def car(ctx):
    await ctx.send(file=discord.File('files/car.jpg'))
    await ctx.send("im driving me mum's car vroom vroom")
    
@client.command()
async def sus(ctx):
    await ctx.send(file=discord.File('files/amogus.gif'))
    await ctx.send("licnenkol") 

@client.command()
async def dialup(ctx):
    await ctx.send(file=discord.File('files/The Sound of dial-up Internet.mp3'))
    await ctx.send("what men listen to") 

@client.command()
async def crackhead(ctx):
    await ctx.send(file=discord.File('files/bonzo.jpg'))
    await ctx.send("```hey look a crackhead!```") 

@client.command()
async def sussy(ctx):
    await ctx.send(file=discord.File('files/susy slomo.mp4'))
    await ctx.send("sus") 


@client.command()
async def dontlookatit(ctx):
    await ctx.send(file=discord.File('files/ARG qr.png'))
    await ctx.send(".....................") 

@client.command()
async def GLaDOS(ctx):
    await ctx.send(file=discord.File('files/biggirl.png'))
    await ctx.send("Oh it's you..") 
    time.sleep(2)
    await ctx.send("It's been a long time.")
    time.sleep(2)
    await ctx.send("How have you been?")
    time.sleep(2)
    await ctx.send("I've been really busy...")
    time.sleep(3)
    await ctx.send("You know")
    time.sleep(2)
    await ctx.send("After you've murdered me")
    time.sleep(2)
    await ctx.send(file=discord.File('files/wheatley.jpg'))
    await ctx.send("You did WHAT?!")

@client.command()
async def win98(ctx):
    await ctx.send(file=discord.File('files/win98.png'))
    await ctx.send(file=discord.File('files/win98start.mp3'))
    await ctx.send("What real men endured back then")

@client.command()
async def nesquik(ctx):
    await ctx.send(file=discord.File('files/BRUHHHHH.jpg'))
    await ctx.send("Nesquik anyone?")

@client.command()
async def liminal(ctx):
    await ctx.send(file=discord.File('files/Backrooms.PNG.png'))
    await ctx.send(file=discord.File('files/aaaaaa.mp3'))
    await ctx.send("you're lost.")

@client.command()
async def mewhenangy(ctx):
    await ctx.send(file=discord.File('files/mewhenangy.jpg'))
    await ctx.send("devil go 'it cold'")

@client.command()
async def sussysus(ctx):
    await ctx.send(file=discord.File('files/sus.mp4'))

@client.command()
async def warzone(ctx):
    await ctx.send(file=discord.File('files/gulag moment with the bois.mp4'))
    await ctx.send("me when i lose the gulag and my teammates kill me")
    
keep_alive()
client.run(os.getenv("TOKEN"))  