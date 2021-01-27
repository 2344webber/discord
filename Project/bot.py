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
    await bot.change_presence(activity=discord.Game(name='meme|HI!helps'))
    print(">>Bot is online!<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['Lobby_channel']))
    await channel.send(f'{member}已經腦殘了!!!')
     
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['Lobby_channel']))
    await channel.send(f'{member}被逐出聯盟了!!!')

@bot.event
async def on_raw_reaction_add(data):
    if str(data.emoji)==':bow_and_arrow:':
        guild=bot.get_guild(data.guild_id)
        channel=bot.get_channel(data.channel_id)
        role=guild.get_role(702476834771697704)
        data.member.add_roles(role)
        await channel.send(f'{data.member.mention}已加入了{role}身分組!')
    
"""""
@bot.event
async def on_reaction_add(data):
    yes=no=0
    channel=bot.get_channel(int(jdata['vote_channel']))
    while(yes>no or no>yes):
        if data.emoji=='<:pepe:765552259798663199>':
            yes+=1
        else:
            no+=1
    if yes>no:
        await channel.send('yes')
    else:
        await channel.send('no')
"""""

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.errors.CommandNotFound):
        await ctx.send('查無此指令!\n請用`HI!helps`查詢可用指令')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])