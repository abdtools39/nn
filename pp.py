from pyrogram import Client, types, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio, re, traceback

# بيانات البوت
bot = Client("kkboty1",
             api_id=22935081,
             api_hash="ba799aab933aad0d41231f5112deb323",
             bot_token="7706982489:AAHg2tj-qKqUFDghIQSfKRVsV1UUMxfAe18")

# قناة الاشتراك الإجباري
CHANNEL_USERNAME = "telestoryup"

async def is_subscribed(user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

@bot.on_message(filters.private & filters.regex("^/start$"))
async def start(app: Client, message: types.Message):
    user_id = message.from_user.id
    if await is_subscribed(user_id):
        await message.reply(
            "**👋 أهلا بك في البوت!**\n\n"
            "يمكنك تحميل ستوريات تيليجرام عبر إرسال رابط أو اسم مستخدم.\n\n"
            "**📌 المطور: @its_aboody**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📢 القناة الرسمية", url=f"https://t.me/{CHANNEL_USERNAME}")]])
        )
    else:
        await message.reply(
            "**🚨 للاستخدام، يجب الاشتراك في القناة أولًا!**\n\n"
            "انضم إلى القناة ثم اضغط /start مرة أخرى.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📢 اشترك الآن", url=f"https://t.me/{CHANNEL_USERNAME}")]])
        )

async def storlink(app: Client, message: types.Message, use, idddd):
    try:
        async with bot:
                story = await bot.get_stories(chat_id=use, story_ids=idddd)
                file = await story.download(in_memory=True)
                story_date = story.date.strftime("%Y-%m-%d")  
                story_time = story.date.strftime("%H:%M:%S") 
                pinned = story.pinned
                public = story.public
                close_friends = story.close_friends
                contacts = story.contacts
                selected_contacts = story.selected_contacts
                caption = (
                    f"📅 التاريخ: {story_date}\n"
                    f"⏰ الوقت: {story_time}\n"
                    f"📌 مثبت: {'نعم' if pinned else 'لا'}\n"
                    f"🔓 عام: {'نعم' if public else 'لا'}\n"
                    f"👥 أصدقاء مقربون: {'نعم' if close_friends else 'لا'}\n"
                    f"📞 جهات الاتصال: {'نعم' if contacts else 'لا'}\n"
                    f"👤 جهات محددة: {'نعم' if selected_contacts else 'لا'}\n"
                )
        await bot.send_document(
            chat_id=message.chat.id,
            document=file,
            caption=caption)
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

async def stor(app: Client, message: types.Message, usernme):
    try:
        async with bot:
            async for story in bot.get_chat_stories(usernme):
                file = await story.download(in_memory=True)              
                story_date = story.date.strftime("%Y-%m-%d")  
                story_time = story.date.strftime("%H:%M:%S") 
                pinned = story.pinned
                public = story.public
                close_friends = story.close_friends
                contacts = story.contacts
                selected_contacts = story.selected_contacts
                caption = (
                    f"📅 التاريخ: {story_date}\n"
                    f"⏰ الوقت: {story_time}\n"
                    f"📌 مثبت: {'نعم' if pinned else 'لا'}\n"
                    f"🔓 عام: {'نعم' if public else 'لا'}\n"
                    f"👥 أصدقاء مقربون: {'نعم' if close_friends else 'لا'}\n"
                    f"📞 جهات الاتصال: {'نعم' if contacts else 'لا'}\n"
                    f"👤 جهات محددة: {'نعم' if selected_contacts else 'لا'}\n"
                )            
                await bot.send_document(
                    chat_id=message.chat.id,
                    document=file,
                    caption=caption
                )
    except Exception as e:
        print(f"Error: {e}")

@bot.on_message(filters.private & filters.text)
async def handle_message(app: Client, message: types.Message):
    user_id = message.from_user.id
    if not await is_subscribed(user_id):
        await message.reply("🚨 يجب الاشتراك في القناة لاستخدام البوت!\n\n📢 اشترك هنا: [اضغط هنا](https://t.me/{CHANNEL_USERNAME})")
        return

    if message.text.startswith('@'):
        await stor(app, message, message.text[1:])
    elif match := re.match(r'https://t.me/([^/]+)/s/([^/]+)', message.text):
        username6 = match.group(1)
        story_id = int(match.group(2))       
        await storlink(app, message, username6, story_id)
    else:
        await message.reply("**يمكنك إرسال رابط ستوري أو يوزر فقط!**")

if __name__ == "__main__":
    bot.run()
