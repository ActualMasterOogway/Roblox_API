import discord
from discord.ext import commands,tasks

prefix = 'rb?'

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix=prefix, intents=intents)

