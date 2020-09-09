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
        # Reagir à mensagem
        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
        # Enviar DM ao utilizador
        dm_channel = await ctx.author.create_dm()
        await dm_channel.send('Envia-me o teu @ do Instagram, para te podermos registar :)')

def setup(bot):
	bot.add_cog(Torneio(bot))