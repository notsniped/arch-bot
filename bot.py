### Modules ###
import os
import sys
import time
import praw
import math
import random
import pickle
import string
import os.path
import discord
import json
import asyncio
import datetime
import requests
import threading
import traceback
import itertools
import youtube_dl
from time import sleep
import multiprocessing
from random import randint
from functools import partial
from discord.utils import get
from discord.ext import tasks
from discord import TextChannel
from discord.ext import commands
from youtube_dl import YoutubeDL
from async_timeout import timeout
from discord.ext.commands import *
from discord import FFmpegPCMAudio
from discord.voice_client import VoiceClient
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
### Modules end ###

### Startup/variables ###
console = False
log = True
intents = discord.Intents.all()
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
client = commands.Bot(command_prefix=".", intents=intents)
slash = SlashCommand(client, sync_commands=False)
global startTime
startTime = time.time()
client.remove_command('help')
cwd = os.getcwd()
global owner_id
owner_id = #paste your discord id here

def foo():
    v = 1
    while True:
        print(f"hit {v}")
        v += 1
        time.sleep(300)

b = threading.Thread(target=foo)
b.daemon = True
b.start()

## Events ###
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds | .help"))
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            else:
                client.load_extension(f'cogs.{filename[:-3]}')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('Bot is online')
    print('==================')
    print('Bot config:')
    print('------------------')
    print(f'Ping: {round(client.latency * 1000)}')
    print('------------------')
    boot = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    print(f'Startup time: {boot}')
    print('------------------')
    print(f'Server count: {str(len(client.guilds))}')
    print('------------------')

@client.event
async def on_message_edit(message_before, message_after):
        global author
        author = message_before.author
        guild = message_before.guild.id
        channel = message_before.channel
        global before
        before = message_before.content
        global after
        after = message_after.content

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
    if message.content.startswith(".say"):
        return
    else:
        pass
    if not message.author.bot:
        pass
    else:
        return
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    guild = client.guilds[0]
    channel = message.channel
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content

@client.event
async def on_guild_join(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds | .help"))

@client.event
async def on_guild_remove(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(client.guilds))} guilds | .help"))
### Events end ###

@client.command()
async def snipe(ctx):
    bad = [
    "fuck",
    "dick",
    "nigga",
    "nigger",
    "cock",
    "asshole",
    "bitch"
    ]
    channel = ctx.channel
    try:
        if any(x in snipe_message_content[channel.id].lower() for x in bad):
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description =f"||{snipe_message_content[channel.id]}||")
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}\nWarning: this message contains banned words")
            await ctx.send(embed = em)
        else:
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")


@client.command()
async def load(ctx, *, arg1):
    if ctx.message.author.id == owner_id:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    client.load_extension(f'cogs.{arg1}')
    await ctx.send("Loaded Cog")

@client.command()
async def unload(ctx, *, arg1):
    if ctx.message.author.id == owner_id:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    client.unload_extension(f'cogs.{arg1}')
    await ctx.send("Unloaded Cog")


@client.command()
async def reload(ctx, *, arg1):
    if ctx.message.author.id == owner_id:
        pass
    else:
        await ctx.reply(f"You can\'t use this command")
        return
    client.unload_extension(f'cogs.{arg1}')
    client.load_extension(f'cogs.{arg1}')
    await ctx.send("Reloaded Cog")

client.run("") #paste your token inside the quotes
