import discord
import os

from discord.ext import commands
from dotenv import load_dotenv
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Vi er live')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'cs' in message.content.lower():
        await message.channel.send('Nei.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'counterstrike' in message.content.lower():
        await message.channel.send('Nei.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'cs2' in message.content.lower():
        await message.channel.send('Nei.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'counter strike 2' in message.content.lower():
        await message.channel.send('Nei.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'counterstrike2' in message.content.lower():
        await message.channel.send('Nei.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'counter strike' in message.content.lower():
        await message.channel.send('Nei.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'homsesex' in message.content.lower():
        await message.channel.send('Homsesex er deilig ass')

@bot.command()
async def hei(ctx):
    await ctx.send('hade')

load_dotenv()
token=os.getenv('DISCORD_TOKEN')
bot.run(token)