import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Login sebagai {bot.user}")

@bot.tree.command(name="join", description="Bot masuk ke voice channel kamu")
async def join(interaction: discord.Interaction):

    if interaction.user.voice:
        channel = interaction.user.voice.channel

        if interaction.guild.voice_client is None:
            await channel.connect()
        else:
            await interaction.guild.voice_client.move_to(channel)

        await interaction.response.send_message(f"Masuk ke voice channel {channel.name}")
    else:
        await interaction.response.send_message(
            "Kamu harus berada di voice channel dulu!",
            ephemeral=True
        )

bot.run(TOKEN)
