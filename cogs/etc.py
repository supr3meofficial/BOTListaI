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

def setup(bot):
    bot.add_cog(AboutCog(bot))