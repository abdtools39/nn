from pyrogram import Client, types, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio, traceback

# بيانات البوت
bot = Client("kkboty1",
             api_id=22935081,
             api_hash="ba799aab933aad0d41231f5112deb323",
             bot_token="7706982489:AAHg2tj-qKqUFDghIQSfKRVsV1UUMxfAe18")

# اسم القناة (بدون "t.me/")
CHANNEL_USERNAME = "telestoryup"

async def is_subscribed(user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(f"خطأ أثناء التحقق من الاشتراك: {e}")
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
            "**🚨 لا يمكنك استخدام البوت حتى تشترك في القناة!**\n\n"
            "انضم إلى القناة ثم اضغط /start مرة أخرى.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📢 اشترك الآن", url=f"https://t.me/{CHANNEL_USERNAME}")]])
        )

@bot.on_message(filters.private & filters.text)
async def handle_message(app: Client, message: types.Message):
    user_id = message.from_user.id
    if not await is_subscribed(user_id):
        await message.reply("🚨 يجب الاشتراك في القناة لاستخدام البوت!\n\n📢 اشترك هنا: [اضغط هنا](https://t.me/{CHANNEL_USERNAME})")
        return

    await message.reply("✅ أنت مشترك بالفعل، يمكنك استخدام البوت الآن!")

if __name__ == "__main__":
    bot.run()
