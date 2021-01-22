import datetime
import asyncio
import discord
import json
from discord.ext import commands
from core.classes import Cog_classes

class task(Cog_classes):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(#channel's ID)
            self.report=self.bot.get_channel(#channel's ID)
            while not self.bot.is_closed():
                now=datetime.datetime.now()
                now_time=datetime.datetime.now().strftime('%H%M%S')
                with open('setting.json','r',encoding='utf8')as jfile:
                    jdata=json.load(jfile)
                if now_time==jdata['time']:
                    await asyncio.sleep(1)
                    await self.channel.purge(limit=10)
                    await self.channel.send('已清除!')
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task=self.bot.loop.create_task(time_task())

    @commands.command()
    async def select_time(self,ctx,time):
        with open('setting.json','r',encoding='utf8')as jfile:
            jdata=json.load(jfile)
        jdata['time']=time
        with open('setting.json','w',encoding='utf8')as jfile:
            json.dump(jdata,jfile,indent=4)
    
    @commands.command()
    async def select_channel(self,ctx,ch:int):
        self.channel=self.bot.get_channel(ch)
        await ctx.send(f'已設置到頻道:{self.channel.mention}')   
    
    @commands.command()
    async def select_report_channel(self,ctx,ch:int):
        self.report=self.bot.get_channel(ch)
        await ctx.send(f'已重新設置日誌頻道:{self.channel.mention}')   
    
    @commands.command()
    async def reset_task(self,ctx):
        with open('setting.json','r',encoding='utf8')as jfile:
            jdata=json.load(jfile)
        jdata['time']=''
        with open('setting.json','w',encoding='utf8')as jfile:
            json.dump(jdata,jfile,indent=4)
        await ctx.send('清理時間已重設')

def setup(bot):
    bot.add_cog(task(bot))
