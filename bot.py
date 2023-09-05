import discord
import re
import name_identifier
from dotenv import load_dotenv
import os

#Set client key
load_dotenv()
client_key = os.environ.get('CLIENT_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    poke_user_id = 716390085896962058 #Poketwo user id

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message is from Poketwo
    if message.author.id == poke_user_id:

        cleaned_message = message.content.replace("\\","")

        # Check if it is a hint message
        if re.search("The pokémon is (.*?)\.", cleaned_message):
            hint = name_identifier.capture_pokemon_hint(cleaned_message)
            solution = name_identifier.main(hint)

            await message.channel.send(f'{solution}')

# Run bot
client.run(client_key)