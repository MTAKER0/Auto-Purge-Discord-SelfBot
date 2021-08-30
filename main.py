import discord
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
	await asyncio.sleep(300000)
	await message.delete()

@client.event
async def on_ready():
    print('ready')


client.run(TOKEN, bot = False)
