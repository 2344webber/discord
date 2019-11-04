import discord
from discord.ext import commands
import random
import json

with open('setting.json',mode='r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class embed(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def commands(self,ctx):
        embed=discord.Embed(title="梗圖指令", color=0x51a6c6)
        embed.add_field(name="`HI!warmeme`", value="會隨機跑出戰爭迷因(有彩蛋)", inline=False)
        embed.add_field(name="`HI!deaf`", value="會隨機跑出嗆人圖片", inline=True)
        embed.add_field(name="其他指令",vaule="```製作中~~```")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(embed(bot))
