import discord
from discord.ext import commands

class Torneio(commands.Cog):
    # Inicialização da class
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def participar(self, ctx):
        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

def setup(bot):
	bot.add_cog(Torneio(bot))