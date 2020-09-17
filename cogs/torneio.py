from discord import Embed
from discord.ext import commands
import asyncio

class Torneio(commands.Cog):
    # Inicialização da class
    def __init__(self, bot):
        self.bot = bot

    # pylint: disable=no-self-argument
    # pylint: disable=no-member
    def check_channel_id(ctx):
        return ctx.message.channel.id == 751866032133636188

    async def account_request(self, ctx):
        # Enviar DM ao utilizador
        dm_channel = await asyncio.wait_for(ctx.author.create_dm(), timeout=3)
        bot_dm = await dm_channel.send('Envia-me o teu @ do Instagram, para te podermos registar :)')
        # Aguardar pela reposta
        try:
            reply = await self.bot.wait_for('message', timeout=30, check=lambda reply: reply.author == ctx.author and reply.channel == dm_channel)
            # Aguardar pela confirmação
            bot_confirmation_message = await dm_channel.send(f"Confirma se está correto: `{reply.content}`")
            await bot_confirmation_message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            await bot_confirmation_message.add_reaction('\N{CROSS MARK}')
            # Check para as reações
            def check(reaction, user):
                return user == ctx.author and reaction.message.author.id == self.bot.user.id
            # Aguardar pelas reações
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30, check=check)
                if reaction.emoji == '\N{WHITE HEAVY CHECK MARK}':
                    await dm_channel.send('Obrigado por te registares. Um moderador irá agora rever o teu registo.')
                    return reply.content
                else:
                    await self.account_request(ctx)
            except asyncio.TimeoutError:
                await bot_confirmation_message.add_reaction('\N{TIMER CLOCK}')
                return None
        except asyncio.TimeoutError:
            await bot_dm.add_reaction('\N{TIMER CLOCK}')

    @commands.command()
    @commands.check(check_channel_id)
    async def participar(self, ctx):
        # Reagir à mensagem
        await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
        # Processo de registo da conta
        account_name = await self.account_request(ctx)
        if account_name != None:
            # Remover potenciais @ no nome
            account_name = str(account_name).replace('@','')
            # Reportar para o canal admin
            admin_channel = ctx.guild.get_channel(751865819834613902)
            await admin_channel.send(f'**Novo registo:** `{ctx.author}` **->** `{account_name}`')
            # Adicionar role
            await ctx.author.add_roles(ctx.guild.get_role(751863492495147176))
            # Editar nickname
            await ctx.author.edit(nick=account_name)

    @commands.command()
    async def torneio(self, ctx):

        desc = '''
:small_blue_diamond: Envia `.participar` para o canal <#751866032133636188> e segue as instruções para te poderes registar.

:eye_in_speech_bubble: Lembra-te que estes canais são destinados exclusivamente aos __participantes__ do torneio. Os participantes devem-se registar com informação verdadeira, nomes de registo indevidos irão ser punidos por um moderador.
                '''

        embed = Embed(title="Como participar no Torneio de Fornite", url="https://listaieseg.wixsite.com/", description=desc, color=0x933db8)
        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(Torneio(bot))