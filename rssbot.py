import discord
from discord.ext import commands

import apscheduler

import json
import time
import feedparser

from secret_settings import *

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False


# Client (our bot)
#client = discord.Client()
client = commands.Bot(command_prefix="!",intents=intents)

@client.command(name="version")
async def version(context):
    
    myEmbed = discord.Embed(title="Current Version", description="Version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="January 8th, 2021", inline=False)
    myEmbed.set_footer(text="by xerluc")
    #myEmbed.set_author(name="xerluc")
    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():

    bot_channel = client.get_channel(797231173281644615)
    for member in client.get_all_members():
        bot = False
        for role in member.roles:
            if role.id == 797287725766017074:
                bot = True
                break
        if not bot:
            await bot_channel.send("Wassup "+member.name+"!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    if message.content == "!dm test":
        await message.author.send("sup my dude")

    await client.process_commands(message)

@client.event
async def on_member_join(member):
    user = {"discord_id": member.id,"feeds":[]}
    print(json.dumps(user, indent=2))


def get_rss_feeds():
    """Get the xml for all feeds for all users"""
    rss_feed_list = []
    #todo loop through the saved jsons
    return rss_feed_list

def parse_rss_feeds():
    """parse all given rss feeds"""
    return

# Run the client on the server
client.run(discord_token)