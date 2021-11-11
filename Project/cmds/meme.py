import discord
from discord.ext import commands
import random
import json
from core.classes import Cog_classes
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

class meme(Cog_classes):    
    
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
