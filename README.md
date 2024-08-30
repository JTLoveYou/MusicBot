# 🎵 Discord Music Bot

A Discord bot that allows you to play music from YouTube directly in your voice channel using slash commands.

## Features

- **Join Voice Channel:** The bot joins the voice channel you're in.
- **Play Music:** Play a song from YouTube by providing a name or a direct URL.
- **Pause/Resume Music:** Pause or resume the currently playing song.
- **Stop Music:** Stop the music and disconnect the bot from the voice channel.
- **Slash Commands:** All commands are available as Discord slash commands for easy access.

## Commands

Here are the commands you can use with this bot:

- `/join` - Joins the voice channel you are in.
- `/play <song name or URL>` - Plays a song from YouTube. You can provide a song name to search for or a direct URL.
- `/pause` - Pauses the current song.
- `/resume` - Resumes the paused song.
- `/stop` - Stops the song and leaves the voice channel.
- `/help` - Displays this help information.

## Installation

### Prerequisites

- Python 3.8 or higher
- `discord-py-interactions`, `youtube_dl`, `PyNaCl`

### Clone the Repository

```bash
git clone https://github.com/yourusername/discord-music-bot.git
cd discord-music-bot
