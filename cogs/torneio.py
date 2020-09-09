import discord
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
            reply = await self.bot.wait_for('message', timeout=30, check=lambda reply: reply.author == ctx.author)
            # Aguardar pela confirmação
            bot_confirmation_message = await dm_channel.send(f"Confirma se está correto: `{reply.content}`")
            await bot_confirmation_message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
            await bot_confirmation_message.add_reaction('\N{CROSS MARK}')
            # Check para as reações
            def check(reaction, user):
                return user == ctx.author
            # Aguardar pelas reações
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30, check=check)
                if reaction.emoji == '\N{WHITE HEAVY CHECK MARK}':
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
            # Editar nickname
            await ctx.author.edit(nick=account_name)
            # Reportar para o canal admin
            admin_channel = ctx.guild.get_channel(751865819834613902)
            await admin_channel.send(f'{ctx.author} -> {account_name}')
            
def setup(bot):
	bot.add_cog(Torneio(bot))