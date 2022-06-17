import discord
from discord.ext import commands

token = "" ###Your Token
bot = commands.Bot(command_prefix="!")
del_chanel_id = 987158343707676674 ###Your Category ID

@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def close(ctx):
  ensar = discord.utils.get(ctx.guild.categories, id = del_chanel_id)

  for channel in ensar.voice_channels:
    await channel.delete()

  for channel in ensar.text_channels:
    await channel.delete()
  
  ensar.delete()


bot.run(token, bot=True)