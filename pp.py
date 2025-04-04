
from pyrogram import Client, types, filters, enums
from pyrogram.raw.functions.stories import GetPeerStories
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio, traceback

bot = Client("kkboty1",
             api_id=22935081,
             api_hash="ba799aab933aad0d41231f5112deb323",
             bot_token="7706982489:AAHg2tj-qKqUFDghIQSfKRVsV1UUMxfAe18")
client = Client("skeksioss",
                api_id=26965358,
                api_hash="0ef9b3131e2168949a634b7d5014290f",
                session_string="")

CHANNEL_USERNAME = "@telestoryup"  # قناة الاشتراك الاجباري

def check_subscription(client, user_id):
    try:
        member = client.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.on_message(filters.private & filters.regex('^/start$'))
async def bew(app: Client, message: types.Message):
    if not check_subscription(app, message.from_user.id):
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشترك في القناة", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}")],
            [InlineKeyboardButton("تحقق من الاشتراك", callback_data="check_sub")]
        ])
        await message.reply("عذراً، يجب عليك الاشتراك في القناة أولاً:", reply_markup=markup)
        return

    await message.reply(text="""**👋 اهلا بك عزيزي،— — — — — —
يمكنك تحميل ستوريات تيليكرام، قم بإرسال رابط الستوري. سأقوم بتحميل لك ستوري مثبت او ارسل يوزر واحمل لك الستوريات الحديثة فقط .
— — — — — —

تم تطوير البوت بواسطة: @its_aboody 🫳 .   **""",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton(text="( المبرمج )",
                                                 url='t.me/katas')
                        ]]))

@bot.on_callback_query(filters.regex("check_sub"))
async def check_sub_callback(_, callback_query):
    if check_subscription(bot, callback_query.from_user.id):
        await callback_query.message.edit_text("""**👋 اهلا بك عزيزي،— — — — — —
يمكنك تحميل ستوريات تيليكرام، قم بإرسال رابط الستوري. سأقوم بتحميل لك ستوري مثبت او ارسل يوزر واحمل لك الستوريات الحديثة فقط .
— — — — — —

تم تطوير البوت بواسطة: @its_aboody 🫳 .   **""",
                                            reply_markup=InlineKeyboardMarkup([[
                                                InlineKeyboardButton(text="( المبرمج )",
                                                                     url='t.me/its_aboody')
                                            ]]))
    else:
        await callback_query.answer("عذراً، يجب عليك الاشتراك في القناة أولاً!", show_alert=True)

async def storlink(app: Client, message: types.Message, use, idddd):
    if not check_subscription(app, message.from_user.id):
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشترك في القناة", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}")],
            [InlineKeyboardButton("تحقق من الاشتراك", callback_data="check_sub")]
        ])
        await message.reply("عذراً، يجب عليك الاشتراك في القناة أولاً:", reply_markup=markup)
        return

    try:
        async with client:
            story = await client.get_stories(chat_id=use, story_ids=idddd)
            file = await story.download(in_memory=True)
            story_date = story.date.strftime("%Y-%m-%d")
            story_time = story.date.strftime("%H:%M:%S")
            edited = story.edited
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
                f"👤 جهات محددة: {'نعم' if selected_contacts else 'لا'}\n")
            await bot.send_document(chat_id=message.chat.id,
                                    document=file,
                                    caption=caption)
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

async def stor(app: Client, message: types.Message, usernme):
    if not check_subscription(app, message.from_user.id):
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشترك في القناة", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}")],
            [InlineKeyboardButton("تحقق من الاشتراك", callback_data="check_sub")]
        ])
        await message.reply("عذراً، يجب عليك الاشتراك في القناة أولاً:", reply_markup=markup)
        return

    try:
        async with client:
            async for story in client.get_chat_stories(usernme):
                file = await story.download(in_memory=True)
                story_date = story.date.strftime("%Y-%m-%d")
                story_time = story.date.strftime("%H:%M:%S")
                edited = story.edited
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
                    f"👤 جهات محددة: {'نعم' if selected_contacts else 'لا'}\n")
                await bot.send_document(chat_id=message.chat.id,
                                        document=file,
                                        caption=caption)
    except Exception as e:
        print(f"Error: {e}")

import re

@bot.on_message(filters.private & filters.text)
async def j(app: Client, message: types.Message):
    if not check_subscription(app, message.from_user.id):
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشترك في القناة", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}")],
            [InlineKeyboardButton("تحقق من الاشتراك", callback_data="check_sub")]
        ])
        await message.reply("عذراً، يجب عليك الاشتراك في القناة أولاً:", reply_markup=markup)
        return

    if message.text.startswith('@'):
        await stor(app, message, message.text[1:])
    elif match := re.match(r'https://t.me/([^/]+)/s/([^/]+)', message.text):
        username6 = match.group(1)
        story_id = int(match.group(2))
        await storlink(app, message, username6, story_id)
    else:
        await message.reply("**يمكنك ارسال رابط ستوري ويوزر فقط **")

if __name__ == "__main__":
    bot.run()
