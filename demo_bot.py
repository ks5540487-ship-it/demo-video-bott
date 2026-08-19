import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 5 Groups mein 50 categories
GROUPS = {
    "Group A - Finance & Marketing": [
        "MBA in Finance",
        "MBA in Marketing",
        "MBA in HR",
        "MBA in Operations",
        "MBA in IT",
        "MBA in Business Analytics",
        "MBA in International Business",
        "MBA in Healthcare Management",
        "MBA in Supply Chain",
        "MBA in Retail Management",
    ],
    "Group B - Digital & Sales": [
        "MBA in Digital Marketing",
        "MBA in Entrepreneurship",
        "MBA in Banking & Finance",
        "MBA in Hospitality",
        "MBA in Project Management",
        "MBA in Business Management",
        "MBA in Strategic Management",
        "MBA in General Management",
        "MBA in Risk Management",
        "MBA in Investment Management",
    ],
    "Group C - Corporate & Brand": [
        "MBA in Financial Management",
        "MBA in Corporate Finance",
        "MBA in Marketing Management",
        "MBA in Sales Management",
        "MBA in Brand Management",
        "MBA in Advertising & PR",
        "MBA in International Marketing",
        "MBA in E-Commerce",
        "MBA in Logistics",
        "MBA in Procurement",
    ],
    "Group D - Tech & Healthcare": [
        "MBA in Manufacturing",
        "MBA in Quality Management",
        "MBA in Technology Management",
        "MBA in AI & Machine Learning",
        "MBA in Data Science",
        "MBA in Cybersecurity",
        "MBA in Healthcare Admin",
        "MBA in Hospital Management",
        "MBA in Pharma Management",
        "MBA in Aviation Management",
    ],
    "Group E - Specialized": [
        "MBA in Tourism",
        "MBA in Event Management",
        "MBA in Construction",
        "MBA in Real Estate",
        "MBA in Media & Entertainment",
        "MBA in Sports Management",
        "MBA in Rural Management",
        "MBA in Agribusiness",
        "MBA in Energy Management",
        "MBA in Sustainability",
    ],
}

# Har category ki Channel ID yahan daalo
CHANNEL_IDS = {
    # Group A
    "MBA in Finance": -100YAHAN_ID_DAALO,
    "MBA in Marketing": -100YAHAN_ID_DAALO,
    "MBA in HR": -100YAHAN_ID_DAALO,
    "MBA in Operations": -100YAHAN_ID_DAALO,
    "MBA in IT": -100YAHAN_ID_DAALO,
    "MBA in Business Analytics": -100YAHAN_ID_DAALO,
    "MBA in International Business": -100YAHAN_ID_DAALO,
    "MBA in Healthcare Management": -100YAHAN_ID_DAALO,
    "MBA in Supply Chain": -100YAHAN_ID_DAALO,
    "MBA in Retail Management": -100YAHAN_ID_DAALO,
    # Group B
    "MBA in Digital Marketing": -100YAHAN_ID_DAALO,
    "MBA in Entrepreneurship": -100YAHAN_ID_DAALO,
    "MBA in Banking & Finance": -100YAHAN_ID_DAALO,
    "MBA in Hospitality": -100YAHAN_ID_DAALO,
    "MBA in Project Management": -100YAHAN_ID_DAALO,
    "MBA in Business Management": -100YAHAN_ID_DAALO,
    "MBA in Strategic Management": -100YAHAN_ID_DAALO,
    "MBA in General Management": -100YAHAN_ID_DAALO,
    "MBA in Risk Management": -100YAHAN_ID_DAALO,
    "MBA in Investment Management": -100YAHAN_ID_DAALO,
    # Group C
    "MBA in Financial Management": -100YAHAN_ID_DAALO,
    "MBA in Corporate Finance": -100YAHAN_ID_DAALO,
    "MBA in Marketing Management": -100YAHAN_ID_DAALO,
    "MBA in Sales Management": -100YAHAN_ID_DAALO,
    "MBA in Brand Management": -100YAHAN_ID_DAALO,
    "MBA in Advertising & PR": -100YAHAN_ID_DAALO,
    "MBA in International Marketing": -100YAHAN_ID_DAALO,
    "MBA in E-Commerce": -100YAHAN_ID_DAALO,
    "MBA in Logistics": -100YAHAN_ID_DAALO,
    "MBA in Procurement": -100YAHAN_ID_DAALO,
    # Group D
    "MBA in Manufacturing": -100YAHAN_ID_DAALO,
    "MBA in Quality Management": -100YAHAN_ID_DAALO,
    "MBA in Technology Management": -100YAHAN_ID_DAALO,
    "MBA in AI & Machine Learning": -100YAHAN_ID_DAALO,
    "MBA in Data Science": -100YAHAN_ID_DAALO,
    "MBA in Cybersecurity": -100YAHAN_ID_DAALO,
    "MBA in Healthcare Admin": -100YAHAN_ID_DAALO,
    "MBA in Hospital Management": -100YAHAN_ID_DAALO,
    "MBA in Pharma Management": -100YAHAN_ID_DAALO,
    "MBA in Aviation Management": -100YAHAN_ID_DAALO,
    # Group E
    "MBA in Tourism": -100YAHAN_ID_DAALO,
    "MBA in Event Management": -100YAHAN_ID_DAALO,
    "MBA in Construction": -100YAHAN_ID_DAALO,
    "MBA in Real Estate": -100YAHAN_ID_DAALO,
    "MBA in Media & Entertainment": -100YAHAN_ID_DAALO,
    "MBA in Sports Management": -100YAHAN_ID_DAALO,
    "MBA in Rural Management": -100YAHAN_ID_DAALO,
    "MBA in Agribusiness": -100YAHAN_ID_DAALO,
    "MBA in Energy Management": -100YAHAN_ID_DAALO,
    "MBA in Sustainability": -100YAHAN_ID_DAALO,
}

logging.basicConfig(level=logging.INFO)

# Main menu — 5 groups dikhao
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for i, group in enumerate(GROUPS.keys()):
        keyboard.append([InlineKeyboardButton(group, callback_data="g" + str(i))])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to MBA Demo Bot!\n\nSelect a Group to see categories:",
        reply_markup=reply_markup,
    )

# Group select karne pe categories dikhao
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Back to main menu
    if data == "back_main":
        keyboard = []
        for i, group in enumerate(GROUPS.keys()):
            keyboard.append([InlineKeyboardButton(group, callback_data="g" + str(i))])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            "Select a Group:",
            reply_markup=reply_markup,
        )
        return

    # Back to group
    if data.startswith("back_g"):
        group_idx = int(data.replace("back_g", ""))
        group_name = list(GROUPS.keys())[group_idx]
        categories = GROUPS[group_name]
        keyboard = []
        for j, cat in enumerate(categories):
            keyboard.append([InlineKeyboardButton(cat, callback_data="c" + str(group_idx) + "_" + str(j))])
        keyboard.append([InlineKeyboardButton("Back to Groups", callback_data="back_main")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            group_name + "\n\nSelect a category:",
            reply_markup=reply_markup,
        )
        return

    # Group selected
    if data.startswith("g") and "_" not in data:
        group_idx = int(data[1:])
        group_name = list(GROUPS.keys())[group_idx]
        categories = GROUPS[group_name]
        keyboard = []
        for j, cat in enumerate(categories):
            keyboard.append([InlineKeyboardButton(cat, callback_data="c" + str(group_idx) + "_" + str(j))])
        keyboard.append([InlineKeyboardButton("Back to Groups", callback_data="back_main")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            group_name + "\n\nSelect a category:",
            reply_markup=reply_markup,
        )
        return

    # Category selected — videos bhejo
    if data.startswith("c"):
        parts = data[1:].split("_")
        group_idx = int(parts[0])
        cat_idx = int(parts[1])
        group_name = list(GROUPS.keys())[group_idx]
        category = GROUPS[group_name][cat_idx]
        channel_id = CHANNEL_IDS.get(category)
        user_id = query.from_user.id

        await query.message.reply_text("Please wait... Sending " + category + " demo videos!")

        success = 0
        for msg_id in range(1, 50):
            try:
                await context.bot.forward_message(
                    chat_id=user_id,
                    from_chat_id=channel_id,
                    message_id=msg_id
                )
                success += 1
            except:
                continue

        keyboard = [
            [InlineKeyboardButton("Back to Categories", callback_data="back_g" + str(group_idx))],
            [InlineKeyboardButton("Back to Groups", callback_data="back_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if success > 0:
            msg = "Done! " + str(success) + " videos sent!\n\nPayment karke full access lo!\nScreenshot bhejo: @Kraja8"
        else:
            msg = "No videos found.\n\nPayment karke full access lo!\nScreenshot bhejo: @Kraja8"

        await context.bot.send_message(chat_id=user_id, text=msg, reply_markup=reply_markup)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
