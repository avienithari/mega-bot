import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from source import mega_list, set_mega

load_dotenv(".env")
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

mega_types = mega_list.get_mega_list()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="setmega")
@commands.has_permissions(administrator=True)
async def setmega(ctx, *args):
    await ctx.channel.send(set_mega.set_mega(mega_types, *args))

@bot.command(name="mega")
async def mega(ctx):
    await ctx.channel.send(set_mega.send_mega())

bot.run(str(token))
