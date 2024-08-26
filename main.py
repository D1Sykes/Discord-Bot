import settings
import discord
import random
from discord.ext import commands

badwords = ['cs', 'cs2', 'counter strike'] 
badwords_responses = ['Nei.', 'Hvilken del av nei forstår du ikke?', 'Ikke faen', 'Uaktuelt.', 'Legg deg.']

def run(): # Main program

    # Bot settings and intents
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Prints a message to console if launched successfully
    @bot.event 
    async def on_ready():
        print(f'{bot.user} er live')

    # Simple event which listens for the aforementioned "badwords" and prints a response if detected
    @bot.event
    async def on_message(message):
        if message.author == bot.user:  # Prevents the bot from responding to itself
            return
        for i in badwords:
            if i in message.content.lower():
                random_response = random.sample(badwords_responses, k=1)
                for response in random_response:
                    await message.channel.send(response)
                break  # Exit loop after the first bad word is found and responded to
        await bot.process_commands(message)  # Process  other commands after checking for bad words

    # Simple multiplication calc for CSGOEmpire coins to Norwegian Kroner conversion
    @bot.command(name="ec")
    async def ecCalc(ctx, num: float):
        result = num * 6.3
        await ctx.send(f"{num} Empire Coins er ish {result} norske kroner ;-)")

    bot.run(settings.token)

if __name__ == "__main__":
    run()