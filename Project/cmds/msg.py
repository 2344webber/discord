import discord
import json
import os
import datetime
from discord.ext import commands
from core.classes import Cog_classes
import gspread
from oauth2client.service_account import ServiceAccountCredentials

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class message(Cog_classes):
    
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def helps(self,ctx):
        embed=discord.Embed(title="目前可用指令", color=0x51a6c6)
        embed.add_field(name="`HI!warmeme`", value="會隨機跑出戰爭迷因(有彩蛋)", inline=False)
        embed.add_field(name="`HI!deaf`", value="會隨機跑出嗆人圖片", inline=False)
        embed.add_field(name="`HI!report`", value="在指令後方打上檢舉詳細內容，管理員就會收到", inline=False)
        embed.add_field(name="其他指令",value="```製作中~~```",inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def report(self,ctx,*,msg):
        channel=self.bot.get_channel(int(jdata['report_channel']))
        when=datetime.datetime.now()
        name=ctx.message.author
        await channel.send(f'<@&593233066340646916>\n{name}:{msg}\n時間:{when}')

def setup(bot):
    bot.add_cog(message(bot))