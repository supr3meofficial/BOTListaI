from discord.ext import commands
import os
import config

bot = commands.Bot(command_prefix='.')

# Quando o bot se conecta ao discord
@bot.event
async def on_ready():
    print(f'BOT conectado como {bot.user}')

# Reage a entradas de membros no servidor
@bot.event
async def on_member_join(member):
    # Canal das boas-vindas definido como o canal de sistema
    channel = member.guild.system_channel
    print("Something at least happened")
    if channel is not None:
        await channel.send(f'Bem-vindo/a à família, {member.mention}. :purple_heart:')

extensions = ['cogs.geral',
              'cogs.torneio']

for ext in extensions:
    bot.load_extension(ext)


bot.run(config.BOT_TOKEN)
# bot.run(os.environ["BOT_TOKEN"])
