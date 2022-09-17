# DiscordNoticeBot.py

import mylib.config as config
import discord
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:

        botRoom = client.get_channel(config.NOTIFY_CHANNEL_ID)
        monitorChannelIds = config.MONITOR_CHANNEL_IDS

        # 退室通知
        if before.channel is not None and before.channel.id in monitorChannelIds:
            await botRoom.send(
               before.channel.name + " から **" + member.name + "** が退出しました。" + 
               before.channel.name + "は現在 **" + str(len(before.channel.members)) + "** 名が利用中です。"
            )
        # 入室通知
        if after.channel is not None and after.channel.id in monitorChannelIds:
            await botRoom.send(
               after.channel.name + " に **" + member.name + "** が入室しました。" +
               after.channel.name + " は現在 **" + str(len(after.channel.members)) + " **名が利用中です。"
            )

token = config.BOT_TOKEN
client.run(token)

