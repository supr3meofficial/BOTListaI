import discord
from discord.ext import commands
import random
import aiohttp
import asyncio

class AboutCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def twitter(self, ctx):

        embed=discord.Embed(title="<:twitter:755846108986736662> Twitter", url="https://twitter.com/listai_eseg", description="O nosso Twitter :purple_heart:", color=0x933db8)
        await ctx.send(embed=embed)

    @commands.command()
    async def instagram(self, ctx):

        embed=discord.Embed(title="<:instagram:755846110261542912> Instagram", url="https://instagram.com/listai_eseg", description="O nosso Instagram :purple_heart:", color=0x933db8)
        await ctx.send(embed=embed)

    @commands.command()
    async def facebook(self, ctx):

        embed=discord.Embed(title="<:facebook:755846109150052523> Facebook", url="https://www.facebook.com/Lista-I-116320443519601/", description="O nosso Facebook :purple_heart:", color=0x933db8)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def tiktok(self, ctx):

        embed=discord.Embed(title="<:tiktok:755846109267755008> TikTok", url="https://www.tiktok.com/@listai_eseg", description="O nosso TikTok :purple_heart:", color=0x933db8)
        await ctx.send(embed=embed)

    @commands.command()
    async def website(self, ctx):

        embed=discord.Embed(title="<:lista_i:755849189317017632> Website", url="https://listaieseg.wixsite.com/", description="O nosso website :purple_heart:", color=0x933db8)
        await ctx.send(embed=embed) 

    @commands.command()
    async def info(self, ctx):

        embed=discord.Embed(title="<:GitHub:449612764751593472> GitHub", url="https://github.com/supr3meofficial/BOTListaI", description="Dá uma espreitadela pelo meu interior", color=0x933db8)
        await ctx.send(embed=embed)
        embed=discord.Embed(title="<:PayPal:437213765923241986> Paypal Link", url="https://www.paypal.me/supr3medonate", description="Se quiseres ajudar o meu programador, aqui está o link <3", color=0x933db8)
        await ctx.send(embed=embed)
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def regras(self, ctx):
        rules = """

**1 ❱ ‎ Não sejas rude com ninguém.**
Não há necessidade nenhuma em insultar alguém.

**2 ❱ ‎ Não sejas um distúrbio**
Ninguém gosta de ter a sua conversa perturbada.

**3 ❱ ‎ Não publiques conteúdo NSFW — coisas sangrentas or pornografia.**
Mantém um chat amigável para todos.

**4 ❱ ‎ Não publicites nada sem aprovação de um moderador.**
Não sejas **esse** tipo.

**5 ❱ ‎ Não spames o chat.**
Vais ser mutado.

**6 ❱ ‎ ‎Utiliza sempre os canais apropriados.**
Estão lá por algum motivo.

**7 ❱ ‎ ‎Segue os Termos e Condições do Discord.**
Estão anexados em baixo.

> Os moderadores deste discord reservam o direito de agir conforme acharem correto sem aviso prévio.
> Para apelar um ban contacta o <@203299786382639104>
"""
        await ctx.message.delete()
        embed = discord.Embed(title='', description=rules, colour=0x933db8)
        embed.set_author(icon_url=ctx.guild.icon_url, name='Regras do Servidor')
        await ctx.send(embed=embed)
        embed=discord.Embed(title='<:discord:434011189656158219> Termos de Serviço', url='https://discord.com/terms', description='', color=0x933db8)
        await ctx.send(embed=embed)
        embed=discord.Embed(title='<:discord:434011189656158219> Diretrizes', url='https://discord.com/guidelines', description='', color=0x933db8)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AboutCog(bot))