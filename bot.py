import discord
import asyncio
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '$')
bot.remove_command('help')

@bot.event
async def on_ready():
    print ("Бот подключился!")

@bot.command(aliases = ['b'])
@commands.has_permissions(ban_members = True)
async def ban (ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'{member.mention} был забанен администратором {ctx.author.mention} по причине: *{reason}*')

@bot.command()
async def say(ctx, channel: discord.TextChannel = None, *, arg):
  await ctx.message.delete()
  await channel.send(arg)

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))