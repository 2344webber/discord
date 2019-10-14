import discord
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(Message(bot))