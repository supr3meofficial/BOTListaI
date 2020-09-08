from discord.ext import commands
import os

bot = commands.Bot(command_prefix='.')

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

bot.load_extension('cogs.geral')

bot.run(os.environ["BOT_TOKEN"])
