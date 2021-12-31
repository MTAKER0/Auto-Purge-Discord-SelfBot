import discord
import time

client = discord.Client()

@client.event
async def on_message(message):
	time.sleep(300)
	await message.delete()

@client.event
async def on_ready():
    print('ready')


client.run(TOKEN, bot = False)
