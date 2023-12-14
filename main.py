#imports
#put this in shell to restart "sh run.sh"

import os
import time
import discord
import discord.ext
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions,  CheckFailure, check
from discord import client
from keep_alive import keep_alive
from discord_buttons_plugin import *

#Prefixes and trash
client = discord.Client()

client = commands.Bot(command_prefix = '>')

buttons = ButtonsClient(client)


#Buttons

@client.command()
async def donate(ctx):
    await buttons.send(
      content = "Go DONATE to ManiaticDevs here!",
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label="Donate Here!",
            style=ButtonType().Link,
            url = "https://www.paypal.com/paypalme/maniaticdevs" 
          )
        ])
      ]
    )


#@client.command()
#async def test(ctx):
 #  await ctx.send("|")
 #   await ctx.delete
#    await ctx.send("/") # funny load ( / - \ | ) 
#    time.sleep(1)
#    await ctx.delete
 #   await ctx.send("-")
 #   time.sleep(1)
#    await ctx.delete
#    await ctx.send("|")
#    time.sleep(1)
#    await ctx.delete

@client.command()
async def Games(ctx):
    await ctx.send("> **Games**")
    await ctx.send("> _ _") # funny load ( / - \ | ) 
    await ctx.send("> *Undecided*")
    await ctx.send("> _ _")
    await ctx.send("> *Projext-Plat*")
    await buttons.send(
      content = "Links",
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label="UNDECIDED Game Page",
            style=ButtonType().Link,
            url = "https://gamejolt.com/games/undecided/676988"
          ),

          Button(
            label="Projext Plat Game Page",
            style=ButtonType().Link,
            url = "https://maniaticdevs.itch.io/projext-plat"
            #for now
          ) 
        ])
      ]
    )

#Defined Button Clicks
#Defined what happens when specific Button clicked
#Or warnings

@buttons.click
async def Accepted_Warning(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/913123435910168653/928709110881480824/funny_hahaha.mp4")

@buttons.click
async def warning13(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/924726117653422151/928758372717699082/0378fj4jf5.mp4")

@buttons.click
async def Payback(ctx):
    await ctx.reply(""" 
    We're no strangers to love
    You know the rules and so do I
    A full commitment's what I'm thinking of
    You wouldn't get this from any other guy
    I just wanna tell you how I'm feeling
    Gotta make you understand
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye

    ** You can never payback me**
    """)



#Normal Command
@client.command()
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("boi wtf i don't understand")


@client.command()
async def wakeup(ctx):
    await ctx.send("what u wanttttttttttt")

@client.command()
async def en(ctx):
    await ctx.send(file=discord.File('files/1586106456740.jpg'))
    time.sleep(1)
    await ctx.send("Bro")
    time.sleep(1)
    await ctx.send("not funny")
    time.sleep(2)
    await ctx.send("O.B : they do look like dat tho")

@client.command()
async def car(ctx):
    await ctx.send(file=discord.File('files/car.jpg'))
    await ctx.send("im driving me mum's car vroom vroom")
    
@client.command()
async def sus(ctx):
    await ctx.send(file=discord.File('files/amogus.gif'))
    await ctx.send(file=discord.File('files/among-us-dance.gif'))
    await ctx.send("licnenkol") 

@client.command()
async def dialup(ctx):
    await ctx.send(file=discord.File('files/The Sound of dial-up Internet.mp3'))
    await ctx.send("what real men listen to") 

@client.command()
async def crackhead(ctx):
    await ctx.send(file=discord.File('files/dimduly.png'))
    await ctx.send("```hey look a crackhead!```") 

@client.command()
async def sussy(ctx):
    await ctx.send(file=discord.File('files/susy slomo.mp4'))
    await ctx.send("sus") 

@client.command()
async def i_want_ps5(ctx):
    await ctx.send(file=discord.File('files/808835bu3u45b.mp4'))

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
    await ctx.send(file=discord.File('files/profile ultimate.png'))
    await ctx.send("a̴n̵d̷ ̴i̴ ̵w̵i̵l̷l̸ ̸f̴u̷c̷k̴i̸n̴g̵ ̸d̵o̵ ̴i̸t̴ ̵a̴g̷a̸i̴n̵")




@client.command()
async def win98(ctx):
    await ctx.send(file=discord.File('files/win98.png'))
    await ctx.send(file=discord.File('files/win98start.mp3'))
    await ctx.send("What real men endured back then")

@client.command()
async def sonk(ctx):
    await ctx.send("By Jehtt On youtube")
    await buttons.send(
      content = "warning this is 13+",    
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label="Accept Warning",
            style=ButtonType().Danger,
            custom_id="warning13" 
          )
        ])
      ]
    )

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
   time.sleep(1)
   await ctx.send("who knew you moron")

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
    await ctx.send("comedy from Escouleshaire") 


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

@client.command()
async def gamingpc(ctx):
    await ctx.send(file=discord.File('files/mygraphics.png'))
    await ctx.send("Oikmo's Gaming pc")

@client.command()
async def PS5(ctx):
    await ctx.send(file=discord.File('files/808835bu3u45b.mp4'))
    await ctx.send("IMAGINE NOT HAVING PS5 :rofl: :rofl: :rofl: LMAO.")

@client.command()
async def hmmm(ctx):
    await ctx.send(file=discord.File('files/devil.png'))
    await ctx.send(file=discord.File('files/muscular.png'))
    await ctx.send(file=discord.File('files/lesson.png'))
    await ctx.send(file=discord.File('files/beeep.png'))
    await ctx.send(file=discord.File('files/cuthulu.png'))
    await ctx.send(file=discord.File('files/cult.png'))
    await ctx.send(file=discord.File('files/X.png'))
    await ctx.send(file=discord.File('files/knockers.png'))
    await ctx.send("interesting")

@client.command()
async def GLaDOS_facts(ctx):
    await ctx.send("Did you know that GLaDOS actually means : Genetic Lifeform and Disk Operating System?")
    await ctx.send("Did you know that GLaDOS in Portal : Still Alive (or just called Portal) is different than the one in Portal 2? Look!")
    await ctx.send(file=discord.File('files/biggirlog.png'))
    time.sleep(1)
    await ctx.send("Portal : Still Alive")
    time.sleep(1)
    await ctx.send(file=discord.File('files/biggirl.png'))
    time.sleep(1)
    await ctx.send("Portal 2")
    time.sleep(1)
    await ctx.send("Interesting Huh?")

@client.command()
async def JUANNO(ctx):
    await ctx.send(file=discord.File('files/JUANNO.mp4'))
    await ctx.send("NO JUAN NO") 

@client.command()
async def randy(ctx):
    await ctx.send(file=discord.File('files/randy.mp4'))
    await ctx.send("MAGNUMOPUS (opus)")
    await ctx.send("opsus")
    await ctx.send("sus")

@client.command()
async def hm(ctx):
    await ctx.send(file=discord.File('files/ghosteatbooty.mp4'))
    await ctx.send("charlie wtf u doin")

@client.command()
async def baby(ctx):
    await ctx.send(file=discord.File('files/suckitbaby.mp4'))
    await ctx.send("suck it baby")

@client.command()
async def welldone(ctx):
    await ctx.send("```*Well done android the enrichment centre reminds you that android hell is a real place where you will be sent at the first sign of defiance.*```")

@client.command()
async def freeminecraft(ctx):
    await ctx.send(""" 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀⠀
    
    """)

    await buttons.send(
      content = "Give Payback",
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label="Payback Oikbot",
            style=ButtonType().Primary,
            custom_id="Payback"
          )
        ])
      ]
    )

@client.command()
async def cursed(ctx):
    await ctx.send("```BEFORE YOU SEE THIS VIDEO...```")
    time.sleep(1)
    await buttons.send(
      content = "please try not to die from 'wtf' or laughter",
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label="Accept Warning",
            style=ButtonType().Danger,
            custom_id="Accepted_Warning"
          )
        ])
      ]
    )

@client.command()
async def clear(ctx):
    await ctx.send(""" 
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    
   _ _    

  **Chat Cleared ** Type to get chatting.

    """)


#Emotes
@client.command()
async def emotes(ctx):
    await ctx.send("""
    
    **Emotes in bot inventory**

    ```
    usage = >Emotes_[Emote_Name]
    e.g. =  >Emotes_dance
    ```

    - Tpose
    - dance
    - pet_pepe
    
    
    """)

@client.command()
async def emotes_Tpose(ctx):
    await ctx.send(ctx.author.mention)
    await ctx.send(file=discord.File('emotes/MemmerTPOSE.png'))

@client.command()
async def emotes_dance(ctx):
    await ctx.send(ctx.author.mention)
    await ctx.send("https://media.discordapp.net/attachments/855686054744031304/862602707361857556/oh_yeah.gif")

@client.command()
async def mother(ctx):
    await ctx.send("https://youtu.be/5t53TcKIlMc")

#pet pet emotes

@client.command()
async def emotes_pet_pepe(ctx):
    await ctx.send(ctx.author.mention)
    await ctx.send("https://tenor.com/brJMu.gif")

@client.command()
async def sonic(ctx):
    await ctx.send(file=discord.File('files/Gotta Go Fast.mp4'))
    await ctx.send("fuck you if no sanic")

@client.command()
async def someone(ctx):
    await ctx.send(file=discord.File('files/patty.jpeg'))
    await ctx.send("mmm samwich")
    time.sleep(1)
    await ctx.send(file=discord.File('files/pattythreat.jpeg'))
    await ctx.send("DONT CUT MY MUOSTACSH")
    time.sleep(1)
    await ctx.send(file=discord.File('files/pattyahshit.jpeg'))
    await ctx.send("why would you do dat???")
    time.sleep(1)
    await ctx.send(file=discord.File('files/abimad.jpg'))
    await ctx.send("I WANT TO CUT YOUR HAIR!11!1!!1!")
    time.sleep(1)
    await ctx.send(file=discord.File('files/pattychill.jpg'))
    await ctx.send("ahh okay im fine")
    time.sleep(1)
    await ctx.send("cuz uh...")
    time.sleep(1)
    await ctx.send(file=discord.File('files/abipeppa.jpg'))
    time.sleep(1)
    await ctx.send("peppa?")

@client.command()
async def starwars4ever(ctx):
  await ctx.send(file=discord.File('files/jackcooper.jpg'))
  await ctx.send("this man is the best and star wars is uh")
  time.sleep(1)
  await ctx.send("disgusting at The Sith Eternal...")
  time.sleep(1)
  await ctx.send("So let that sit in while you look at BT-7274")
  await ctx.send(file=discord.File('files/M2W2.webp'))
  time.sleep(1)
  await ctx.send(file=discord.File('files/Titanfall_2_Logo.jpg'))
  time.sleep(1)
  await ctx.send("Now play this game and you...")
  time.sleep(1)
  await ctx.send("You will feel like you just had the best experience in your life")
  time.sleep(1)
  await ctx.send("This game will fill that hole you needed whilst playing video games.")
  time.sleep(1)
  await ctx.send("Now GO! STOP BEING A (star wars) DORK AND GET OUT THERE AND PLAY SOME REAL GAMES!")
  time.sleep(1)
  await ctx.send("stop playing baby  stwa wo gwames  by *publisher here* cuz th e y       mak sw games owoga booga")
  time.sleep(1)
  await ctx.send("you need to start playing more harder games btw also GROW UP")
  time.sleep(1)
  await ctx.send("Oh I hAvE tHe EnTiRe ScRiPtS oF eVeRy StAr WaRs MoViEs *snork*")
  time.sleep(1)
  await ctx.send("No WONDER why *YOU* have no father!")
  time.sleep(1)
  await ctx.send("You get offended like feminists over the littlest shits.")
  await ctx.send("OHHHHHHHHHHHHHHHH I'm sorry I don't know that Jar Jar Binks is the *hottest* character in all of hollywood!")

@client.command()
async def the_star_trek(ctx):
    await ctx.send(file=discord.File('files/Star Trek 25th.mp4'))
    await ctx.send(file=discord.File('files/Star Trek TOS.mp4'))

keep_alive()
client.run(os.getenv("TOKEN"))