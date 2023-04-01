# punishmentbot.py
import os
import random
import discord
import log
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# the Punishment Bot

# load token from .env file
load_dotenv()
token = os.getenv('token')

# guild IDs for slash commands
server = 000000000000000000 # replace 0's with guild (server) ID here
#server2 = 000000000000000000 # define additional servers to add bot to multiple servers (as many as you want)


# define Punishment Bot as a bot called client that responds to commands beginning with ! and give him all discord intents
class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix = "!", intents = intents)

    async def setup_hook(self):
        guilds = [str(server)] # you can add to additional servers, just add str(server2) separated using commas
        for guild in guilds:
            await self.tree.sync(guild = discord.Object(id = guild))
        print(f"Synced slash commands for {self.user}.")

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

client = Bot()


# let you know when Punishment Bot has joined the chat
@client.event
async def on_ready():
    print('Punishment Bot is ready for payback!')


# setup the logger to see who's using Punishment Bot
logger = log.setup_logger(__name__)


# *********** Punishment Bot slash commands ***********

# *********** Punishment Bot react to message protocol ***********

@client.hybrid_command(name = "react", with_app_command = True, description = "Make Punishment Bot react to a message.")
@app_commands.guilds(discord.Object(id = server)) # you can add to additional servers, just add discord.Object(id = server2) separated using commas
@app_commands.describe(message_id = "What is the message ID number? (Click 'Copy ID' in the message's submenu to obtain it.)")
@app_commands.describe(emoji = "What emoji would you like Punishment Bot to react with?")
async def react(ctx: discord.Interaction, message_id, emoji: str):
    """Make Punishment Bot react to a message using the /react slash command"""
    channel = ctx.channel
    username = str(ctx.author)
    channel_str = str(ctx.channel)
    server = str(ctx.guild)
    msg = await channel.fetch_message(message_id)
    logger.info(f"\x1b[31m{username}\x1b[0m asked for Punishment Bot to react with {emoji} to the message 'ID: {msg.id}' - '{msg.content}' in the \x1b[31m{channel_str}\x1b[0m channel in the \x1b[31m{server}\x1b[0m server.")
    await msg.add_reaction(emoji)
    await ctx.reply("reacted", delete_after = 3, ephemeral = True)


# *********** Punishment Bot say custom message protocol ***********

@client.hybrid_command(name = 'say', with_app_command = True, description = "Make Punishment Bot say whatever you want.")
@app_commands.guilds(discord.Object(id = server)) # you can add to additional servers, just add discord.Object(id = server2) separated using commas
async def say(ctx, message: str):
    """Make Punishment Bot say whatever you want using the /say slash command"""
    channel = ctx.channel
    username = str(ctx.author)
    channel_str = str(ctx.channel)
    server = str(ctx.guild)
    logger.info(f"\x1b[31m{username}\x1b[0m asked for Punishment Bot to say '{message}' in the \x1b[31m{channel_str}\x1b[0m channel in the \x1b[31m{server}\x1b[0m server.")
    await ctx.channel.send(message)
    await ctx.reply("sent", delete_after = 3, ephemeral = True)


# *********** Punishment Bot message response triggers ***********

# *********** Punishment Bot sarcasm protocol ***********

def sarcasm(input):
    input = list(input.lower())

    for x in range(len(input)):
        if x % 2 == 0:
            input[x] = input[x].lower()
        else:
            input[x] = input[x].upper()

    input = ''.join(input)
    return(input)


# *********** Punishment Bot punishment protocol ***********

@client.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    server = str(message.guild)

    # Punishment Bot message logger protocol
    logger.info(f"New message sent from \x1b[31m{username}\x1b[0m in the \x1b[31m{channel}\x1b[0m channel in the \x1b[31m{server}\x1b[0m server : '{user_message}'")

    # Punishment Bot punishment protocol
    if message.author != client.user:
        role = discord.utils.get(message.author.roles, name = "Punished")
        if role is not None and role.name == "Punished":

            responses = [sarcasm(message.content),
                         "hey " + format(message.author.display_name) + " you're an idiot",
                         "you should ligma",
                         "wow " + format(message.author.display_name) + ", you're so fucking cool",
                         "hey " + format(message.author.display_name) + ", will you marry me?",
                         "how'd you get so fucking smart?",
                         sarcasm(message.content),
                         "how insightful",
                         format(message.author.display_name) + " you come up with that thought all on your own?",
                         "can you send feet pics " + format(message.author.display_name) + "?",
                         "*pees in your butt*",
                         "tell 'em " + format(message.author.display_name) + "!",
                         sarcasm(message.content)]

                         # add as many responses as you want to the list of punishing retorts above, separated by commas

            logger.info(f"\x1b[31m{username}\x1b[0m triggered Punishment Bot's punishment protocol in the \x1b[31m{channel}\x1b[0m channel in the \x1b[31m{server}\x1b[0m server : '{user_message}'")

            await message.channel.send(f'{random.choice(responses)}')
        else:
            return

    await client.process_commands(message)


# ******************************************************

client.run(token)
