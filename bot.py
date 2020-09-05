import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('BOT conectado como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.teste'):
        await message.channel.send('Parece estar a funcionar.')

client.run(os.environ["BOT_TOKEN"])