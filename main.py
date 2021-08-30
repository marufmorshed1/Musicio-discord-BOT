
import discord
from discord.ext import commands
import music
from webserver import keep_alive
import os


cogs = [music]

client = commands.Bot(command_prefix = "?", intents = discord.Intents.all())


for i in range(len(cogs)):
  cogs[i].setup(client)


keep_alive()

# TOKEN = os.environ.get("DISCORD_BOT_SECRET")

my_secret = os.environ['DISCORD_BOT_SECRET']


client.run(my_secret)