import discord
from config import settings
from rcon.source import Client

bot = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == CHANNELID:
        nick = message.content
        member = message.author
        role = discord.utils.get(message.guild.roles, name = "ROLE")
        await member.add_roles(role)
        await message.channel.send(f'Игрок {nick} был добавлен в Whitelist Haku Mods!')

        with Client('127.0.0.1', 25575, passwd='123qwe') as mineserv:
            response = mineserv.run('easywl', 'add', nick)

        print(response)


bot.run(settings['token'])
