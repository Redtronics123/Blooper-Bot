import nextcord
from nextcord.ext import commands, tasks
import asyncio


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @tasks.loop(seconds=30)
    async def status(self):
        await self.bot.change_presence(
            activity=nextcord.Game("Spielt mit der Waschmaschine."),
            status=nextcord.Status.do_not_disturb
        )
        await asyncio.sleep(15)
        await self.bot.change_presence(
            activity=nextcord.Game("In der Entwicklung"),
            status=nextcord.Status.do_not_disturb
        )

    @commands.Cog.listener()
    async def on_ready(self):
        self.status.start()
        print("Status started")


def setup(bot):
    bot.add_cog(Status(bot))
