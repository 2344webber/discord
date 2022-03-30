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
        
    @commands.command()#可以使用(沒被伺服端禁止)
    async def car(self,ctx,*,msg):
        url="https://nhentai.net/"
        website=requests.get(url+"g/"+msg+"/")
        sp=bs(website.text,'lxml')
        Comic_name = sp.select('div h1')
        Comic_image=sp.select('#container a')
        for titles in Comic_name:
          await ctx.send(titles.text)
          print(titles.text)
        for images in Comic_image:
          await ctx.send(url+images['href'])
          print(url+images['href'])

def setup(bot):
    bot.add_cog(meme(bot))
