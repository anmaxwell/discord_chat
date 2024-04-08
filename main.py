import os
import discord
from discord.ext import commands

# Get bot token from environment variable
TOKEN = os.environ.get('DISCORD_TOKEN')

if TOKEN is None:
    print("Error: Discord token not found. Please set the DISCORD_TOKEN environment variable.")
    exit(1)

# Bot setup
bot = commands.Bot(command_prefix='!')

