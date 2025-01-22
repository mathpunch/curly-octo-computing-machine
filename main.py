import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

token = os.environ['MTMzMTQxNDk5MjExNjkwODA5NQ.GLHwt0.eo3ePqqYD_s_0jCFNfI1FvzUtGFSLa4aQNjsqM'] 
bot.run(token) 
