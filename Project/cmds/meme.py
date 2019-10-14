import discord
from discord.ext import commands
import random
import json

with open('setting.json',mode='r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class meme(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def warmeme(self,ctx):
        random_pic=random.choice(jdata['url-pic'])
        await ctx.send(random_pic)
    
    @commands.command()
    async def deaf(self,ctx):
        random_pic=random.choice(jdata['deaf'])
        await ctx.send(random_pic)


def setup(bot):
    bot.add_cog(meme(bot))
