import discord
from discord.ext import commands

from secret_settings import *

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


# Client (our bot)
#client = discord.Client()
client = commands.Bot(command_prefix="!",intents=intents)

@client.command(name="connect")
async def _connect(context):
    voice_channel = client.get_channel(672895581953327107)
    await voice_channel.connect()

@client.command(name="disconnect")
async def _disconnect(context):
    voice_channel = client.get_channel(672895581953327107)
    await voice_channel.disconnect()

@client.command(name="version")
async def version(context):
    
    myEmbed = discord.Embed(title="Current Version", description="Version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Model Size:", value="355M", inline=False)
    myEmbed.add_field(name="Retrained:", value="False", inline=True)
    myEmbed.add_field(name="Date Released:", value="January 8th, 2021", inline=False)
    myEmbed.set_footer(text="by xerluc")
    #myEmbed.set_author(name="xerluc")
    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():

    bot_channel = client.get_channel(797231173281644615)
    myEmbed = discord.Embed(title="GPT2-bot", description="GPT2-bot is now online!", color=0x87ceeb)
    await bot_channel.send(embed=myEmbed)

    myEmbed = discord.Embed(title="Examples", description=" ", color=0x87ceeb)
    myEmbed.add_field(name="\u200b", value="```!gpt2```", inline=False)
    myEmbed.add_field(name="\u200b", value="```!gpt2 \"There was a poll that asked me\"```", inline=False)
    myEmbed.add_field(name="\u200b", value="```!gpt2 There was a poll that asked me```", inline=False)
    myEmbed.add_field(name="\u200b", value="```There was a poll that asked me```", inline=False)
    await bot_channel.send(embed=myEmbed)

    # myEmbed = discord.Embed(title="\u200b", description="\u200b", color=0x87ceeb)
    # myEmbed.add_field(name="\u200b", value="https://openai.com/blog/better-language-models/", inline=False)
    # myEmbed.add_field(name="\u200b", value="> GPT-2 is a large transformer-based language model with 1.5 billion parameters, trained on a dataset of 8 million web pages. GPT-2 is trained with a simple objective: predict the next word, given all of the previous words within some text. The diversity of the dataset causes this simple goal to contain naturally occurring demonstrations of many tasks across diverse domains. GPT-2 is a direct scale-up of GPT, with more than 10X the parameters and trained on more than 10X the amount of data.", inline=False)
    # myEmbed.add_field(name="\u200b", value="https://en.wikipedia.org/wiki/GPT-2", inline=False)
    # await bot_channel.send(embed=myEmbed)
    #await bot_channel.send(">> https://openai.com/blog/better-language-models/")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    if message.content == "!dm test":
        await message.author.send("sup my dude")

    await client.process_commands(message)

# Run the client on the server
client.run(discord_token)