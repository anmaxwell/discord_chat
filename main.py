import os
import discord
from discord.ext import commands

# Get bot token from environment variable
TOKEN = os.environ.get('DISCORD_TOKEN')

if TOKEN is None:
    print("Error: Discord token not found. Please set the DISCORD_TOKEN environment variable.")
    exit(1)

# Define intents
intents = discord.Intents.default()
intents.messages = True
# Bot setup
bot = commands.Bot(command_prefix='!', intents=intents)

# Event to print messages from a specific channel
@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def download_messages(ctx, channel_id):
    try:
        # Fetch the channel
        channel = bot.get_channel(int(channel_id))
        if channel is None:
            await ctx.send("Channel not found.")
            return

        # Fetch recent messages
        messages = []
        async for message in channel.history(limit=10):
            messages.append(message)

        # Save messages to a file
        filename = f"messages_{channel_id}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            for message in messages:
                file.write(f"{message.author.name}: {message.content}\n")

        await ctx.send(f"Messages downloaded and saved to {filename}.")
    except Exception as e:
        await ctx.send(f"Error occurred: {str(e)}")

@bot.command()
async def shutdown(ctx):
    try:
        await ctx.send("Shutting down...")
        await bot.close()  # Gracefully close the bot
    except Exception as e:
        print(f"Error occurred during shutdown: {str(e)}")
        await ctx.send(f"Error occurred during shutdown: {str(e)}")

# Run the bot
bot.run(TOKEN)