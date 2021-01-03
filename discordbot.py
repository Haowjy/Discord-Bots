import discord

import apscheduler

import json
import time
import feedparser

from secret_settings import *

# Client (our bot)
client = discord.Client()

def get_rss_feeds():
    """Get the xml for all feeds for all users"""
    rss_feed_list = []
    #todo loop through the saved json
    return rss_feed_list

def parse_rss_feeds():
    """parse all given rss feeds"""

@client.event
async def on_ready():
    # DO STUFF
    general_channel = client.get_channel(797231173281644615)

    await general_channel.send("Hello World!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Run the client on the server
client.run(discord_token)