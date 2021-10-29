
import os
import time
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from async_timeout import timeout
from keep_alive import keep_alive

client = discord.Client()

client = commands.Bot(command_prefix = '`')



from discord.ext import commands

@client.command()
async def hello(ctx):
   await ctx.send("im hiding...")
   time.sleep(2)
   await ctx.send("im screwed, aren't I?")

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
    await ctx.send(file=discord.File('files/dimduly.png'))
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
    await ctx.send(file=discord.File('files/SUNP0011.JPG'))
    await ctx.send("devil go 'it cold'")

@client.command()
async def sussysus(ctx):
    await ctx.send(file=discord.File('files/sus.mp4'))

@client.command()
async def warzone(ctx):
    await ctx.send(file=discord.File('files/gulag moment with the bois.mp4'))
    await ctx.send("me when i lose the gulag and my teammates kill me irl")

@client.command()
async def funnycar(ctx):
    await ctx.send(file=discord.File('files/th.png'))
    await ctx.send("me when funny")

@client.command()
async def canoe(ctx):
    await ctx.send(file=discord.File('files/his reward is the canoe.png'))
    await ctx.send("a criminal in a canoe.")

@client.command()
async def win7(ctx):
    await ctx.send(file=discord.File('files/win7.png'))
    await ctx.send("what 2007-2009 kids endured.")

@client.command()
async def kpopstan(ctx):
   await ctx.send(file=discord.File('files/videoplayback.mp4'))
   await ctx.send("when you say kpop sucks on twitter")

@client.command()
async def wheatley(ctx):
   await ctx.send(file=discord.File('files/dockingstation.jpg'))
   await ctx.send("GOOD NEWS, THAT IS NOT A DOCKING STATION")

@client.command()
async def bueno(ctx):
   await ctx.send(file=discord.File('files/bueno.jpeg'))
   await ctx.send("bueno")

@client.command()
async def fh4(ctx):
   await ctx.send(file=discord.File('files/mosler.jpg'))
   await ctx.send("Patryk: Mosler is glitched car.")
   await ctx.send("Karol:")
   await ctx.send(file=discord.File('files/blank face emoji.jpg'))

@client.command()
async def slapschickonk(ctx):
   await ctx.send("i don wanna cook a chickeenn")
   await ctx.send(file=discord.File('files/slaps.png'))

@client.command()
async def smiledog(ctx):
   await ctx.send("smile :)")
   await ctx.send(file=discord.File('files/smile.jpg'))
   await ctx.send(file=discord.File('files/smiledog.jpg'))

@client.command()
async def analogfear(ctx):
   await ctx.send("run they are coming")
   await ctx.send(file=discord.File('files/analog1.jpg'))
   await ctx.send(file=discord.File('files/analog2.png'))

@client.command()
async def whybillgates(ctx):
    await ctx.send(file=discord.File('files/bruh.png'))
    await ctx.send("so i spent Â£50+ on... nothing?") 

@client.command()
async def oikmosfeetpics(ctx):
    await ctx.send(file=discord.File('files/sdjflsdkfj;.mp4'))
    await ctx.send("okay...? u have fetish for my feet?") 

@client.command()
async def yoga(ctx):
    await ctx.send(file=discord.File('files/yoga!.png'))
    await ctx.send(file=discord.File('files/nono.mp3'))
    await ctx.send("She's at yoga!") 

@client.command()
async def comedy(ctx):
    await ctx.send(file=discord.File('files/image0.jpg'))
    await ctx.send(file=discord.File('files/image0 (1).jpg'))
    await ctx.send("comedy from Escoulshaire aka monke boy 27") 


@client.command()
async def whobetter(ctx):
    await ctx.send("licnenkol") 

@client.command()
async def tacos(ctx):
    await ctx.send(file=discord.File('files/soft tacos.mp4'))
    await ctx.send("you're my friend now.") 

@client.command()
async def jeb_boat(ctx):
    await ctx.send(file=discord.File('files/jeb_boat.jpg'))
    await ctx.send("you dare oppose him mortal?") 

@client.command()
async def korn(ctx):
    await ctx.send(file=discord.File('files/KORN.mp4'))
    await ctx.send("WHEN ITS KORN")

@client.command()
async def lilshitz(ctx):
    await ctx.send(file=discord.File('files/lilshitz.png'))
    await ctx.send("Lil Shitz the mischievous turd")

@client.command()
async def ifeelya(ctx):
    await ctx.send(file=discord.File('files/sad.jpg'))
    await ctx.send("I feel this man.")

keep_alive()
client.run(os.getenv("TOKEN"))

