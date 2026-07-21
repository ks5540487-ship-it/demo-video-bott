import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
SOURCE_CHANNEL_ID = int(os.environ.get("SOURCE_CHANNEL_ID"))

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("▶️ Start Now — Watch All Videos", callback_data="send_videos")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 *Welcome!*\n\n"
        "🎬 Click *Start Now* to get all demo videos instantly!",
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )

async def send_videos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    await query.message.reply_text(
        "⏳ *Please wait...*\nSending all videos to you!",
        parse_mode="Markdown"
    )

    success = 0

    # Sirf 50 tak check karega — fast hoga
    for msg_id in range(1, 50):
        try:
            await context.bot.forward_message(
                chat_id=user_id,
                from_chat_id=SOURCE_CHANNEL_ID,
                message_id=msg_id
            )
            success += 1
        except Exception:
            continue

    if success > 0:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ *Done!*\n\n🎬 Total *{success}* videos sent!\nEnjoy watching! 🍿",
            parse_mode="Markdown"
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text="❌ No videos found. Please contact admin.",
            parse_mode="Markdown"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(send_videos, pattern="send_videos"))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
