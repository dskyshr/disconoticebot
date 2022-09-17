# discoChannels.py

import mylib.config as config
import discord

client = discord.Client(intents=discord.Intents.all())

# 起動時処理
@client.event
async def on_ready():
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")

token = config.BOT_TOKEN
client.run(token)

