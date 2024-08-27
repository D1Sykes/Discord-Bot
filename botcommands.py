import random
import discord
from discord.ext import commands

# Badwords which the bot will continously look for, and respond to.
badwords = ['cs', 'cs2', 'counter strike'] 
badwords_responses = ['Nei.', 'Hvilken del av nei forstår du ikke?', 'Ikke faen', 'Uaktuelt.', 'Legg deg.']

async def on_ready():
    print(f'Sekretæren er klar for flørting!')

# A function which looks for, and responds to "badwords"
async def on_message(message):
    if message.author == message.guild.me:  # Prevents the bot from responding to itself
        return
    for word in badwords:
        if word in message.content.lower():
            response = random.choice(badwords_responses)
            await message.channel.send(response)
            break  # Exit loop after the first bad word is found and responded to

    # Process commands after checking for bad words
    bot_instance = message.guild.me._state._get_client()  # Get the bot instance from message
    await bot_instance.process_commands(message)

# Simple currency-converter between CSGO Empire Coins and Norwegian Kroner
async def ecCalc(ctx, num: float = None):
    if num is None:
        await ctx.send("Du må bruke et tall og da dumbass, typ: !ec 10")
    else:
        result = num * 6.3
        await ctx.send(f"{num} Empire Coins er ish {result} norske kroner ;-)")


# Simple random seed generator,
async def seedGen(ctx):
    randSeed = random.randint(10000000000000000000000000000000, 99999999999999999999999999999999)
    await ctx.send(randSeed)

# Function to register all the commands and events with the bot
def botSetup(bot):
    bot.event(on_ready)
    bot.event(on_message)
    bot.command(name="ec")(ecCalc)
    bot.command(name="seed")(seedGen)