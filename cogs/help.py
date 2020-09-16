import discord
from discord.ext import commands


class HelpCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        # Comando de ajuda (será atualizado no futuro)

        show_help = '''
**:small_blue_diamond: Comandos I**
`.teste` Será que o bot está a funcionar?
`.twitter` Link do nosso Twitter
`.instagram` Link do nosso Instagram
`.facebook` Link do nosso Facebook
`.tiktok` Link do nosso TikTok
`.website` Link do nosso Website

**:small_blue_diamond: Torneio Fortnite**
`.torneio` Informa-te como participar no torneio
`.participar` Participa no torneio!

**:small_blue_diamond: Sobre o BOT**
`.info` Descobre mais sobre mim
                '''

        await ctx.message.add_reaction("❔")
        embed=discord.Embed(title="Lista de comandos", description=show_help, color=0x0080c0)
        embed.set_footer(text="Desenvolvido por supr3me", icon_url=self.bot.user.avatar_url)
        await ctx.author.send(embed=embed)

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(HelpCog(bot))