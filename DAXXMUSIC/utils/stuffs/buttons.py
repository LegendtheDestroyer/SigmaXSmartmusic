from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("◈ 𝐂ʜᴀᴛ𝐆ᴘᴛ ◈", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("◈ 𝐆ʀᴏᴜᴘs ◈", callback_data="mplus HELP_Group"),InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("◈ 𝐓ᴀɢ-𝐀ʟʟ ◈", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("◈ 𝐈ɴғᴏ ◈", callback_data="mplus HELP_Info"),InlineKeyboardButton("◈ 𝐄xᴛʀᴀ ◈", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("◈ 𝐈ᴍᴀɢᴇ ◈", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("◈ 𝐀ᴄᴛɪᴏɴ ◈", callback_data="mplus HELP_Action"),InlineKeyboardButton("◈ 𝐒ᴇᴀʀᴄʜ ◈", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("◈ 𝐅ᴏɴᴛ ◈", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("◈ 𝐆ᴀᴍᴇs ◈", callback_data="mplus HELP_Game"),InlineKeyboardButton("◈ Ⓣ︎-𝐆ʀᴀᴘʜ ◈", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("◈ 𝐈ᴍᴘᴏsᴛᴇʀ ◈", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("◈ 𝐓ʀᴜᴛʜ-𝐃ᴀʀᴇ ◈", callback_data="mplus HELP_TD"),InlineKeyboardButton("◈ 𝐇ᴀsᴛᴀɢ ◈", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("◈ 𝐓𝐓s ◈", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("◈ 𝐅ᴜɴ ◈", callback_data="mplus HELP_Fun"),InlineKeyboardButton("◈ 𝐐ᴜᴏᴛʟʏ ◈", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("⇦", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("⇨", callback_data=f"managebot123 settings_back_helper"),
    ]]
