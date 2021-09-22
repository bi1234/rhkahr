import discord, asyncio, os
from discord.ext import commands
import time
import schedule
import datetime


game = discord. Game("파라토르몬")
bot = commands. Bot(command_prefix='[', status=discord.Status.online, activity=game)

frihanbo = ['보건', '한문']

def today():
  days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
  return days[datetime.datetime.today().weekday()]
client = discord.Client()

if today() == '토요일':
  frihanbo = frihanbo.reserve()

@bot.command()
async def 과목(ctx):
  if today() == '월요일':
     await ctx.send('한문 영어 과학 도덕 주제선택 주제선택')
  if today() == '화요일':
     await ctx.send('한문 수학 예술체육 예술체육 국어 미술')
  if today() == '수요일':
     await ctx.send('영어 수학 국어 사회 도덕 스포츠')
  if today() == '목요일':
     await ctx.send('영어 과학 사회 진로 수학 체육')
  if today() == '금요일':
     await ctx.send(f'사회 과학 국어 {frihanbo[0]} 음악 체육')
  if today() == '토요일':
     await ctx.send('없음')
  if today() == '일요일':
     await ctx.send('없음')

bot.run('ODg2NTc1MDc1MjE2NzI4MTI3.YT3lYQ.6LA3Zbd-t8FNF0DjL2LpRL_0Xxk')