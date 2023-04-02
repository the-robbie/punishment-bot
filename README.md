# punishment-bot
Discord bot to punish deserving users.

## Editing the files
You will need to edit the .env and punishmentbot.py files first before you can run this bot.

### Edit the .env file
Within the .env file, replace `ENTER_TOKEN_HERE` with your Discord bot's token. ***The bot will not run without your bot's token.***

### Edit the punishmentbot.py file
**Adding your Guild (Server) ID for slash commands:**
Within the punishmentbot.py file on line 17, replace the 0's with your guild (server) ID. This will allow the slash commands to work in your specified server. You can add as many additional servers as you want (one example additional server is on line 18, which you will need to uncomment by removing the leading # and replace those 0's with another guild ID). If you add more servers, you will also need to edit lines 55 and 73 to include the additional servers. ***The bot will not run without at least one guild ID added.***

**Editing the responses:**
You can also edit the list of responses that the bot would randomly say to the punished user. The list of responses starts on line 119 of the punishmentbot.py file. You can add as many as you want, just make sure to separate the responses using commas.

**Making a custom role name:**
You will need to create a role called Punished and assign that role to the user being punished. If you want to change the name of the role, you will need to edit the word Punished on lines 116 and 117 of the punishmentbot.py file to your custom role name.


## Running the Bot

You can run this bot within terminal using python3 or you can run this bot using Docker.

### Running Within Terminal Using Python3
You will first need to install python3 and the dependencies if you haven't already. You will also need to add your bot to each server you want it running in before running it.

Google can help you to install python3 on your machine depending on your operating system. Then run the following commands to install the dependencies:
```
pip install --upgrade pip
pip install discord
pip install loguru
pip install python_dotenv
pip install -U git+https://github.com/Rapptz/discord.py
```
When adding the bot to your server(s), make sure to select the `bot` and `applications.commands` checkboxes within the OAuth2 URL Generator screen of your Discord Developer portal. You can select whichever permissions you feel comfortable with, as it doesn't require admin permissions to run. Then the bot invite link will generate at the bottom of that screen.

Save the files wherever you want on your machine. Within terminal, change directories (using cd) to where you saved the files. Then run the command `python3 punishmentbot.py`.

Your bot should now be up and running.

### Running With Docker
This assumes that you already have Docker installed on your machine.

You will first need to add your bot to each server you want it running in before running it. When adding the bot to your server(s), make sure to select the `bot` and `applications.commands` checkboxes within the OAuth2 URL Generator screen of your Discord Developer portal. You can select whichever permissions you feel comfortable with, as it doesn't require admin permissions to run. Then the bot invite link will generate at the bottom of that screen.

Save the files wherever you want on your machine. Within terminal, change directories (using cd) to where you saved the files.

Then make a new directory on your machine where you will mount the container's volume against using the following command:

```sudo mkdir /usr/src/bot```

Next run the following command to build the image for your bot:

```docker build -t punishmentbot:latest .```

Finally run the following command to run your Docker container using the newly created image, making sure to replace the `/DIRECTORY/WHERE/YOU/SAVED/THE/FILES` with the filepath where you save your files:

```docker run --name=punishmentbot -v /DIRECTORY/WHERE/YOU/SAVED/THE/FILES:/usr/src/bot --restart=always punishmentbot:latest```

Your bot should now be up and running in a Docker container named punishmentbot.

## Bot Features
### Punishing Responses
Once the bot is up and running it will respond to every message sent by anyone who has the Punish role assigned to them using the list of predetermined responses starting on line 119 of the punishmentbot.py file. It will choose the reponses by random from that list.

### Slash Commands
There are two slash commands included in this bot: `/say` and `/react`. `/say` allows you to have the bot say whatever you want. `/react` allows you to make the bot react to any message sent. These slash commands are anonymous to the server members, so no one will know who made the bot say or react to something. This will be captured in the logs, however, so the owner of the bot can check the logs to see who used the `/say` and `/react` commands.

### Logging
This bot keeps a log of all server activity. This includes everytime someone initiates one of the bot's protocols as well as everytime a message is sent in the server. A punishmentbot.log file will be created in the same directory as the other files that will save all of the server activity.
