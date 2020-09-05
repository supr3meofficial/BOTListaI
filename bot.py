from discord.ext import commands
import os

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'BOT conectado como {bot.user}')

@bot.command()
async def teste(ctx):
    await ctx.send('Parece estar a funcionar.')

bot.run(os.environ["BOT_TOKEN"])