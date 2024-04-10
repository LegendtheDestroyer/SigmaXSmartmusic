import re
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram.types import Message
from pyrogram import Client, filters
from DAXXMUSIC import app



# "/gn" command ka handler
@app.on_message(filters.command("oodnight", prefixes="g"))
def goodnight_command_handler(client: Client, message: Message):
    # Randomly decide whether to send a sticker or an emoji
    send_sticker = random.choice([True, False])
    
    # Send a sticker or an emoji based on the random choice
    if send_sticker:
        client.send_sticker(message.chat.id, get_random_sticker())
    else:
        client.send_message(message.chat.id, get_random_emoji())

# Function to get a random sticker
def get_random_sticker():
    stickers = [
        "CAACAgQAAxkBAAEL41BmFqrDJ9ea_EpyG8j-UKsyYmbBrwACOgkAAhTL8FDqxvaN6uy7ejQE",
        "CAACAgQAAxkBAAEL41JmFqri-EMQP36BlfX1AUImiqxkkwAC6REAAqbxcR4suLN3od21sjQE",
        "CAACAgQAAxkBAAEL41RmFqsVzrmNuSbepWhZj0oQjjUtOAACVQwAAuZzSFHgo3Wkl0r02jQE",
        "CAACAgQAAxkBAAEL41ZmFqtaS5VDbFc-aWphZTlf4THT2QACow0AAnQmEFD0xPrdn0moQDQE",
        "CAACAgUAAxkBAAEL41hmFqttk_Hc8wsU5f5SU1pugyao0AACagAD0DiULFrfMo2dWmRMNAQ",
    ]
    return random.choice(stickers)

# Function to get a random emoji
def get_random_emoji():
    emojis = [
        "😴",
        "😪", 
        "💤",
        
    ]
    return random.choice(emojis)
