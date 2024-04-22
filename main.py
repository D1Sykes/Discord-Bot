# Import needed libraries

import settings
import discord

from discord.ext import commands

badwords = ['cs', 'cs2'] # Custom variable used in later function(s)

def run(): # Main program

    # Bot settings and intents
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)


    # Prints a message to console if launched succesfully
    @bot.event 
    async def on_ready():
        print(f'{bot.user} er live')


    # Simple event which listens for the aformentioned "badwords" and prints a response if detected
    @bot.event
    async def on_message(message):
        if message.author == bot.user: # This prevents the bot from going in a loop looking for the word, I don't really know why.
            return
        for i in badwords:
            if i in message.content.lower():
                await message.channel.send('Nei.')
        await bot.process_commands(message)  # This line allows the bot to do other things while the event is going, again keeping it from being stuck in a loop. Also, I don't know why.


    # Simple multiplication calc for CSGOEmpire coins to Norwegian Kroner conversion
    @bot.command(name="ec")
    async def ecCalc(ctx, num : float):
        result = num * 6.3
        await ctx.send(f"{num} Empire Coins er ish {result} norske kroner ;-)")

    bot.run(settings.token)

if __name__ == "__main__":
    run()