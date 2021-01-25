import datetime
import asyncio
import discord
import json
from discord.ext import commands
from core.classes import Cog_classes

class poll(Cog_classes):

    @commands.command()
    async def add_poll(self,ctx,msg,options:int):
        await ctx.message.delete()
        embed=discord.Embed(title='投票!!',description=f'投票內容:{msg}')
        msg=await ctx.send(embed=embed)
        if options<=1:
            await ctx.send('選項太少啦!!!至少需要兩個')
        elif options>10:
            await ctx.send('機器人的小腦袋記不住啦!!!')
        elif options==2:
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
        else:
            reaction=['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
            for i in range(options):
                sum=i
                await msg.add_reaction(reaction[sum])



def setup(bot):
    bot.add_cog(poll(bot))