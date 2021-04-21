import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix = "$")
TOKEN = "Add Your Bot Token here"

@client.event
async def on_ready():
    print("Bot is Ready....")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Watching my Owner...."))

def load(extension):
    client.load_extension(f"cogs.{extension}")


def unload(extension):
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
    