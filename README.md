🎵 Discord Music Bot
A Discord bot that allows you to play music from YouTube directly in your voice channel using slash commands.

Features
Join Voice Channel: The bot joins the voice channel you're in.
Play Music: Play a song from YouTube by providing a name or a direct URL.
Pause/Resume Music: Pause or resume the currently playing song.
Stop Music: Stop the music and disconnect the bot from the voice channel.
Slash Commands: All commands are available as Discord slash commands for easy access.
Commands
Here are the commands you can use with this bot:

/join - Joins the voice channel you are in.
/play <song name or URL> - Plays a song from YouTube. You can provide a song name to search for or a direct URL.
/pause - Pauses the current song.
/resume - Resumes the paused song.
/stop - Stops the song and leaves the voice channel.
/help - Displays this help information.
Installation
Prerequisites
Python 3.8 or higher
discord-py-interactions, youtube_dl, PyNaCl
Clone the Repository
bash
Copier le code
git clone https://github.com/yourusername/discord-music-bot.git
cd discord-music-bot
Install Dependencies
Install the necessary Python packages using pip:

bash
Copier le code
pip install discord-py-interactions youtube_dl PyNaCl
Setup Your Bot
Go to the Discord Developer Portal and create a new application.
Under the "Bot" tab, create a bot and copy the token.
Replace YOUR_BOT_TOKEN_HERE in the main.py file with your actual bot token.
Run the Bot
bash
Copier le code
python main.py
The bot should now be online and responding to commands in your Discord server.

Troubleshooting
Ensure the bot has the necessary permissions to connect to voice channels and manage messages.
If the bot isn't responding to slash commands, check that the bot has the applications.commands permission and try re-syncing the commands by restarting the bot.
Contributing
Feel free to open issues or pull requests if you find any bugs or want to add new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

