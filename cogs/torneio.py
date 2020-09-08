import discord
from discord.ext import commands

class Torneio(commands.Cog):
    # Inicialização da class
    def __init__(self, bot):
        self.bot = bot

    def check_channel_id(ctx):
        return ctx.message.channel.id == 751866032133636188

    @commands.command()
    @commands.check(check_channel_id)
    async def participar(self, ctx):
        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

def setup(bot):
	bot.add_cog(Torneio(bot))