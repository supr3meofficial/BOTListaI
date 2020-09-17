from math import ceil as math_ceil
from datetime import timedelta
from discord import Spotify, Embed
from discord.ext import commands

class Geral(commands.Cog):
    # Inicialização da class
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def teste(self, ctx):
        await ctx.send('Parece estar a funcionar.')
    
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 43200, commands.BucketType.member)
    async def partilharmusica(self, ctx):
        member = ctx.author
        spotify = None
        # Encontra a atividade do Spotify
        for activity in member.activities:
            if type(activity) == Spotify:
                spotify = activity
        # Enviar mensagem de erro se não for descoberta
        if not spotify:
            return await ctx.send("Precisas de estar a ouvir uma música no Spotify ou não deves ter o Discord e o Spotify conectados",delete_after=5)

        share_author = f"{member.name} partilhou a seguinte música:"
        duration = str(spotify.duration).split(".")[0]
        artists = str(spotify.artist).replace(";",",")
        SPOTIFY_ICON = 'https://images-eu.ssl-images-amazon.com/images/I/51rttY7a%2B9L.png'

        embed = Embed(title="", description="", colour=spotify.colour)
        embed.set_author(icon_url=SPOTIFY_ICON, name=share_author)
        embed.set_thumbnail(url=spotify.album_cover_url)
        embed.add_field(name="Título:", value=spotify.title, inline=False)
        embed.add_field(name="Artistas:", value=artists, inline=False)
        embed.add_field(name="Álbum:", value=spotify.album, inline=False)
        embed.add_field(name="Duração:", value=duration, inline=False)
        embed.add_field(name="Link da Faixa:", value=f'https://open.spotify.com/track/{spotify.track_id}', inline=False)
        # Enviar para o canal de partilhas
        share_channel = ctx.guild.get_channel(756188228448420041)
        await share_channel.send(embed=embed)
        await ctx.send(f"Acabaste de partilhar **{spotify.title}**! -> <#756188228448420041>")

    @partilharmusica.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg="Só podes voltar a partilhar uma música em {}.".format(timedelta(seconds=(math_ceil(error.retry_after))))
            embed = Embed(title="Uh oh!",
            description=msg,
            colour=0xbf0000)
            embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
            return await ctx.send(embed=embed)
                
def setup(bot):
    # Adicionar cog ao bot
	bot.add_cog(Geral(bot))