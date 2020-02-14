import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

client = commands.Bot(command_prefix = '!')
Client = discord.client
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' 총 서버 갯수   '+str(len(client.servers))+'개  확인 | 총 서버 유저 수  '+str(len(set(client.get_all_members())))+' 명 확인')
    print("copyright 2019 WHY all rights reserved")

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def 유저정보(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}님의 정보".format(user.name), description="정보확인 성공", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="이름", value=user.name, inline=True)
    embed.add_field(name="아이디", value=user.id, inline=True)
    embed.add_field(name="상태", value=user.status, inline=True)
    embed.add_field(name="권한", value=user.top_role)
    embed.add_field(name="회원가입 날짜", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
@commands.has_permissions(administrator=True)

@client.command(pass_context = True)
async def 전송(ctx, *, content: str):
        for member in ctx.message.server.members:
            try:
                await client.send_message(member, content)
                await client.say("**전송 성공 : {}** :o:".format(member))
            except:
                print("FAIL SEND")
                await client.say("**전송 실패 : {}** :x:".format(member))
		
client.run("NjUzOTI3NjQ1MDQ1NzE5MDUx.Xe-0nQ.q-FKF7JYnwXNpkp3TQ4Mj-MV_Ds")
