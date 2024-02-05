import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(".env")
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.run(str(token))
