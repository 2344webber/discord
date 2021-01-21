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

    
    @commands.command()##無法使用(被伺服端禁止)
    async def car(self,ctx,*,msg):
        html=(f'https://nhentai.net/g/{msg}')
        sp=BeautifulSoup(urlopen(html))
        try:  
            title=sp.find("meta", itemprop="image")
            img=title.get("content")
            await ctx.send(img)
        except:
            await ctx.send('查無此車')
        finally:
            return()
        

def setup(bot):
    bot.add_cog(meme(bot))
