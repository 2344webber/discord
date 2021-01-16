import discord
from discord.ext import commands
import json
import random
import asyncio
import datetime
import os

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='HI!') 

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='meme|HI!commands'))
    print(">>Bot is online!<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['Lobby_channel']))
    await channel.send(f'{member}已經腦殘了!!!')
     
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['Lobby_channel']))
    await channel.send(f'{member}被逐出聯盟了!!!')

@bot.command()
async def report(ctx,*,msg):
    channel=bot.get_channel(int(jdata['report_channel']))
    await channel.send(f'<@&593233066340646916> :{msg}')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])