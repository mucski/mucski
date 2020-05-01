import discord
from redbot.core import commands, checks

class AdminUtils(commands.Cog):
    
    def shuffle(self, word):
        word = list(word)
        random.shuffle(word)
        return ''.join(word)
     
    @commands.command()
    @checks.is_owner()
    async def add_cookie(self, ctx, amt: int, member: discord.Member=None):
        if member is None:
            member = ctx.author
        cookie = await self.conf.user(member).cookies()
        amt = amt + cookie
        await self.conf.user(member).cookies.set(amt)
        await ctx.send("Added {} to {}".format(amt, member.name))
    
    async def del_cookie(self, ctx, member: discord.Member=None):
        pass
    
    async def reset_db(self, ctx):
        pass
    
    async def reset_cd(self, ctx, member: discord.Member=None):
        pass
        
    
