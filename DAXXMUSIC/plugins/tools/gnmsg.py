import re
from pyrogram import filters
import random
from DAXXMUSIC import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgQAAxkBAAEL41BmFqrDJ9ea_EpyG8j-UKsyYmbBrwACOgkAAhTL8FDqxvaN6uy7ejQE", # Sticker 1
        "CAACAgQAAxkBAAEL41JmFqri-EMQP36BlfX1AUImiqxkkwAC6REAAqbxcR4suLN3od21sjQE", # Sticker 2
        "CAACAgQAAxkBAAEL41RmFqsVzrmNuSbepWhZj0oQjjUtOAACVQwAAuZzSFHgo3Wkl0r02jQE", # Sticker 3
        "CAACAgQAAxkBAAEL41ZmFqtaS5VDbFc-aWphZTlf4THT2QACow0AAnQmEFD0xPrdn0moQDQE",
        "CAACAgUAAxkBAAEL41hmFqttk_Hc8wsU5f5SU1pugyao0AACagAD0DiULFrfMo2dWmRMNAQ",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
