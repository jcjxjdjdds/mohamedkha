from pyrogram import filters
from HackSessionBot import app , START_PIC
from HackSessionBot.Helpers.data import PM_TEXT,PM_BUTTON,HACK_MODS,HACK_TEXT
from pyrogram.types import CallbackQuery

from telebot import *
bot = telebot.TeleBot("6225367412:AAF_stl_eJUgacMubl8D7C4mFUf9LVxEL_g")
@bot.message_handler(commands=["start"])
def start(message):
                ch = "Q1IIQ"
                idu = message.chat.id
                join = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idu}").text
                if '"status":"left"' in join:
                    bot.send_message(message.chat.id,f"""
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
{ch} 

‼️| اشترك ثم ارسل /start
                    """)
                else:
                 bot.send_photo(message.chat.id,url, """• 𝚆𝙴𝙻𝙲𝙾𝙼𝙴  •""")

@app.on_message(filters.command("start") & filters.private)
async def _start(_, message):
    user = message.from_user.mention
    bot = (await _.get_me()).mention 
    await message.reply_photo(
       photo = START_PIC,
       caption = PM_TEXT.format(user, bot),
       reply_markup = PM_BUTTON) 


@app.on_message(filters.command("hack") & filters.private)
async def _hack(_, message):
    await message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


@app.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(bot : app, query : CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


