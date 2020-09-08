import discord
from discord.ext import commands

class Geral(commands.Cog):
    # Inicialização da class
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def teste(self, ctx):
        await ctx.send('Parece estar a funcionar.')

def setup(bot):
	bot.add_cog(Geral(bot))