import discord
from redbot.core import commands, Config

from datetime import datetime, timedelta
from redbot.core.utils.chat_formatting import humanize_timedelta
from .taskhelper import TaskHelper

class GiveAway(TaskHelper, commands.Cog):
    """Simple Giveaway Cog by Mucski"""
    def __init__(self):
        TaskHelper.__init__(self)
        self.conf = Config.get_conf(self, 975667633)
        defaults = { "channel": 0, "msg": 0, "stamp": 0, "running": False }
        self.conf.register_guild(**defaults)
        self.load_check = self.bot.loop.create_task(self._worker())
        
        @commands.group()
        async def gw(self, ctx):
            pass
        
        @gw.command()
        async def start(self, ctx, time: int, channel: discord.TextChannel = None, *, text = None):
            if not channel:
                channel = ctx.channel
            if not text:
                text = "Daily VIP Supreme giveaway. React bellow to enter."
            now = datetime.utcnow()
            timer = timedelta(minutes=time)
            future = timer + now
            future = future.timestamp()
            temp_stamp = datetime.fromtimestamp(future)
            remaining = temp_stamp - now
            remaining = remaining.total_seconds()
            #Embed Builder
            embed = discord.Embed()
            embed.set_author(name=f"{self.bot.user.name}'s giveaway.", icon_url=self.bot.avatar_url)
            embed.description(text)
            embed.set_footer(text=f"{humanize_timedelta(timedelta=remaining.total_seconds())}")
            msg = await channel.send(embed=embed)
            msg.addreaction("💎")
            channel = channel.id
            msg = msg.id
            await self.conf.guild(ctx.guild).channel.set(channel)
            await self.conf.guild(ctx.guild).msg.set(msg)
            await self.conf.guild(ctx.guild).stamp.set(future)
            await self.conf.guild(ctx.guild).running.set(True)
            await self.schedule_task(self._timer(remaining))
            
        @gw.command()
        async def end(self, ctx):
            msg = await self.conf.guild(ctx.guild).msg()
            channel = await self.conf.guild(ctx.guild).channel()
            await self._teardown(channel, msg, ctx.guild)
            await self.end_task()
            await self.conf.guild(ctx.guild).running.set(False)
            
        async def _timer(self, remaining):
            guilds = await self.conf.all_guilds()
            for guild in guilds.items():
                guild = self.bot.get_guild(guild)
            if await self.conf.guild(guild).running() is False:
                return
            msg = await self.conf.guild(guild).msg()
            channel = await self.conf.guild(guild).channel()
            await asyncio.sleep(remaining)
            await self._teardown(channel, msg, guild)
            
        async def _teardown(self, channel, msg, guild):
            channel = self.bot.get_channel(channel)
            msg = await channel.fetch_message(msg)
            users = []
            async for user in msg.reactions[0].users():
                if user == self.bot.user:
                    continue
                users.append(user)
            winner = random.choice(users)
            await self.conf.guild(guild).msg.clear()
            await self.conf.guild(guild).channel.clear()
            await self.conf.guild(guild).stamp.clear()
            await self.conf.guild(guild).running.set(False)
            #Embed Builder
            embed = discord.Embed()
            embed.set_author(name=f"{self.bot.user.name}'s giveaway.", icon_url=self.bot.avatar_url)
            embed.description("Giveaway finished. See bellow for winners:")
            embed.set_footer(text=f"Giveaway finished.")
            msg.edit(embed=embed)
            await channel.send(f"The winner is {winner.mention}, congratulations! 🎉🎊")
            
        async def _worker(self):
            await self.bot.wait.until_ready()
            guilds = await self.conf.all_guilds()
            for guild in guilds.items():
                guild = self.bot.get_guild(guild)
            now = datetime.utcnow()
            stamp = await self.conf.guild(guuld).stamp()
            stamp = datetime.fromtimestamp()
            remaining = stamp - now
            remaining = remaining.total_seconds()
            msg = await self.conf.guild(guild).msg()
            channel = await self.conf.guild(guild).channel()
            if stamp < now:
                await self._teardown(channel, msg, guild)
            else:
                await self.schedule_task(self._timer(remaining))
            
        def cog_unload(self):
            self.load_check.cancel()