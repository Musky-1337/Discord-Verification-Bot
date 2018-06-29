All the settings for the bot go in config.json

The bot token is the token for your Discord Application.

A tutorial on creating a Discord application and getting the token is here https://github.com/SinisterRectus/Discordia/wiki/Setting-up-a-Discord-application but ignore anything about OAuth as we don't require it for this app.

You can get the ID for your server (guide on getting that here https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)

The role name is the name of the role authorized users will be given (must be spelt exactly with correct capitalisation), you need to create the role first and setup the desired permissions.

You can authorize users with anything (emails, license keys etc.) just enter each one on a separate line in verification.txt

To run the discord bot, just run bot.py (a server is a good idea)