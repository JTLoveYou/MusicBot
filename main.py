import discord
from discord.ext import commands
from discord import app_commands
import youtube_dl
import asyncio

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # Bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f'Successfully synced {len(synced)} commands.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')
    print(f'{bot.user} has connected to Discord!')

@bot.tree.command(name="join", description="Joins the voice channel you are in")
async def join(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message("You are not in a voice channel!", ephemeral=True)
        return
    channel = interaction.user.voice.channel
    await channel.connect()
    await interaction.response.send_message(f"Joined {channel.name}")

@bot.tree.command(name="play", description="Plays a song from YouTube")
@app_commands.describe(search="The song name or URL to play")
async def play(interaction: discord.Interaction, search: str):
    if interaction.guild.voice_client is None:
        await join(interaction)

    async with interaction.channel.typing():
        player = await YTDLSource.from_url(search, loop=bot.loop, stream=True)
        interaction.guild.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

    await interaction.response.send_message(f'Now playing: {player.title}')

@bot.tree.command(name="pause", description="Pauses the current song")
async def pause(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await interaction.response.send_message("Music paused")
    else:
        await interaction.response.send_message("No music is currently playing")

@bot.tree.command(name="resume", description="Resumes the paused song")
async def resume(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await interaction.response.send_message("Music resumed")
    else:
        await interaction.response.send_message("Music is not paused")

@bot.tree.command(name="stop", description="Stops the song and leaves the voice channel")
async def stop(interaction: discord.Interaction):
    if interaction.guild.voice_client is not None:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("Stopped the music and left the voice channel")
    else:
        await interaction.response.send_message("The bot is not in a voice channel")

@bot.tree.command(name="help", description="Displays the help information")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title="Help", description="List of commands for the bot", color=discord.Color.blue())
    embed.add_field(name="/join", value="Join your current voice channel", inline=False)
    embed.add_field(name="/play <song name or URL>", value="Play a song from YouTube", inline=False)
    embed.add_field(name="/pause", value="Pause the current song", inline=False)
    embed.add_field(name="/resume", value="Resume the paused song", inline=False)
    embed.add_field(name="/stop", value="Stop the song and leave the voice channel", inline=False)
    await interaction.response.send_message(embed=embed)

bot.run(BOT_TOKEN)
