import discord
import datetime
from discord import app_commands
from discord.ext import commands

intents = discord.Intents().all()
client = discord.Client
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} connected")
bot.run("MTE0ODIzODI4ODk5ODYzNzY3MQ.GEIKyj.NbxuWGsI9F4hfrbpzAOgl6phnsB6Jc2g5-UZGs")

