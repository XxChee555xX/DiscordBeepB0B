import discord
from discord.ext import commands
from discord.ext.commands import Bot
import urllib
import urllib.request
import bs4 as bs
import re
import random
import praw
import time
import datetime

Client = discord.Client()
bot = commands.Bot(command_prefix = "<@450205388726468609> ",case_insensitive=True)

redditbot =praw.Reddit(username ="-YourLife-",
                          client_id = "OGy9_rBA-xcjpQ",
                          client_secret = "oNqE6JgytOLmrUPlCQReKoRPTMs",
                          user_agent = "TestBot By YourLife")

#Variables
Clukk = time.asctime(time.localtime())
thetime = datetime.datetime.strptime(Clukk, "%c")



@bot.event
async def on_ready():
    print("B0B has awakened")
    await bot.change_presence(game=discord.Game(
        name='w̶̡͌i̷͉̚t̷̘̎h̶̙̀ ̸̙͊ḧ̶̯́i̴̳̾ṡ̷͚ ̷̾͜f̷͈͛r̸̬̾i̴̢̎e̷̠͒ñ̶̥d̵͜͝s̸̮̆'))

@bot.event
async def on_message(message):
    if message.content.startswith("<@450205388726468609>"):
        if message.content[22:].lower() in ["hai","hey","hello","ni hao","yo","hi"] :
            greetings = ["Greetings ","Beep. Boop. ","Hello There ","01101000 01100101 01101100 01101100 01101111 "]
            userID = message.author.id
            await bot.send_message(message.channel,random.choice(greetings)+"<@%s>"%(userID))
        if message.content[22:].lower() == "ping":
            await bot.send_message(message.channel,'pong.')
    message.content = message.content.lower()
    await bot.process_commands(message)

@bot.command(pass_context = True)
async def clear(ctx, number):
    try:
        mgs = []
        number = int(number)
        async for x in bot.logs_from(ctx.message.channel, limit=number):
            mgs.append(x)
        await bot.delete_messages(mgs)
    except:
        pass

@bot.command(pass_context = True)
async def meme(ctx):
    try:
        submissionlist = []
        for submission in redditbot.subreddit('memes').hot(limit=100):
            submissionlist.append(submission)
        await bot.send_message(ctx.message.channel,random.choice(submissionlist).title + '\n' + random.choice(submissionlist).url)
    except:
        pass

@bot.command(pass_context = True)
async def getsubred(ctx,subred,num,NSFW=False):
    try:
        submissionlist = []
        try:
            if type(int(num)) == int :
                if int(num) <= 100:
                    for submission in redditbot.subreddit(subred).hot(limit=int(num)):
                        submission.over_18 = not submission.over_18
                        if submission.over_18 or NSFW != False:
                            print("appended")
                            submissionlist.append(submission)
                    for submission in submissionlist:
                        await bot.send_message(ctx.message.channel, submission.title +'\n'+ submission.url)
        except Exception as e:
            if "invalid literal for int() with base 10: 'r'" in str(e):
                if num == "r":
                    for submission in redditbot.subreddit(subred).hot(limit=int(100)):
                        submission.over_18 = not submission.over_18
                        if submission.over_18 or NSFW != False:
                            print("appended")
                            submissionlist.append(submission)
                            subchoice = random.choice(submissionlist)
                    await bot.send_message(ctx.message.channel, subchoice.title + '\n' + subchoice.url)
            else:
                await bot.send_message(ctx.message.channel,"Error;Please use the command in the following format 'getsubred [subreddit] [numbers/'r'].'")
    except Exception as e:
        if str(e) == "Cannot choose from an empty sequence":
            await bot.send_message(ctx.message.channel, "Either no submission found or submissions are NSFW.'")
            await bot.send_message(ctx.message.channel,"Error;Please use the command in the following format 'getsubred [subreddit] [numbers/'r'].'")

@bot.command(pass_context = True)
async def telltime(ctx):
    await bot.send_message(ctx.message.channel,"It is now " + thetime.strftime("%I:%M %p"))

@bot.command(pass_context = True)
async def telldate(ctx):
    await bot.send_message(ctx.message.channel,"Today is " + thetime.strftime("%A")+','+thetime.strftime("%d")+' of ' + thetime.strftime("%B %Y"))

@bot.command(pass_context = True)
async def tolong(ctx):
    await bot.send_message(ctx.message.channel,"""Help has arrived.
    Current Available Functions: 'CLEAR','getsubred','MeMe'.functions are case-sensitive.Beep.Boop.""")




# addyoutube
# addgoogle
# get a random image from Imgur.
# cat
# wiki
# urbandict
# timer
bot.run("NDUwMjA1Mzg4NzI2NDY4NjA5.De6Sow.4K5McCa8J2WXCxLTuBf6TeC5FBg")