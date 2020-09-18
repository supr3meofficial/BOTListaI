from discord import Game, Forbidden
from discord.ext import commands
import os
# import config

bot = commands.Bot(command_prefix='.')

# Quando o bot se conecta ao discord
@bot.event
async def on_ready():
    await bot.change_presence(activity=Game("Família I <3"))
    print(f'BOT conectado como {bot.user}')

# Reage a entradas de membros no servidor
@bot.event
async def on_member_join(member):
    # Canal das boas-vindas definido como o canal de sistema
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'Bem-vindo/a à família, {member.mention}. :purple_heart:')

@bot.event
async def on_command_error(ctx, error):
    # Permitir handler de erros local
    if hasattr(ctx.command, 'on_error'):
        return

    # Exceção original
    error = getattr(error, 'original', error)

    # Executa quando o comando não é encontrado. (É ignorado)
    if isinstance(error, commands.CommandNotFound):
        return
    # Executa quando o comando não pode ser utilizado nas mensagens privadas
    if isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.author.send('Desculpa, mas este comando não pode ser utilizado nas DMs')
        except Forbidden:
            pass
        return

extensions = ['cogs.geral',
              'cogs.torneio',
              'cogs.help',
              'cogs.etc',
              'cogs.admin']

for ext in extensions:
    bot.load_extension(ext)


# bot.run(config.BOT_TOKEN)
bot.run(os.environ["BOT_TOKEN"])
