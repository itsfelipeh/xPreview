import discord
from discord.ext import commands

TOKEN = 'TU_TOKEN_DE_DISCORD'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    # No procesar mensajes del propio bot
    if message.author == bot.user:
        return

    # Detectar si el mensaje contiene un enlace de Twitter
    if "https://twitter.com/" in message.content:
        # Reemplazar 'https://twitter.com/' con 'https://vxtwitter.com/'
        new_url = message.content.replace('https://twitter.com/', 'https://vxtwitter.com/')
        await message.channel.send(f"URL modificada: {new_url}")

    await bot.process_commands(message)

bot.run(TOKEN)
