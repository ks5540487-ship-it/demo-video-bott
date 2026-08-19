import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 5 Groups mein 50 categories
GROUPS = {
    "Group A - Main CP DEMO": [
        "Main CP DEMO",
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
   "Main CP DEMO": -1004304439937,
    "Indian r##p MMS Leaked": -1004360171518,
    "Chi$#dd mms leaked video DEMO": -1004339995876,
    "Desi Cucks Bundle DEMO": -1004346101582,
    "Punjabi leak Bundle DEMO": -1003934594969,
    "Desi viral Bhabhi DEMO": -1004317800836,
    "Jaslin Kaur Demo": -1003746920545,
    "Mom Son DEMO": -1003907927607,
    "Bro Sis Demo": -1003962620877,
    "Tango Live Video Call Demo": -1003922128376,
    "Best Edits Demo": -1004482705956,
    # Group B
    "Desi Flashing Demo": -1004281697182,
    "Full Open Dance demo": -1004467834124,
    "Dress Change Demo": -1004348122859,
    "Aditiy Mistry Demo": -1003643700138,
    "Full Webseries Demo": -1004462474135,
    "Desi Moti Gand Walking Demo": -1004363997989,
    "Teen CP Demo": -1003966340422,
    # Group C
    "Mom and Daughter CP Demo": -1004350514494,
    "Foreign CP Demo": -1004403613395,
    "Tamil CP Demo": -1004262611728,
    "𝗙𝗼𝗿𝗰𝗲𝗱 𝘀𝗲𝘅 CP Demo": -1004262611728,
    "𝗜𝗻𝗱𝗶𝗮𝗻 𝗽𝗲𝗱𝗼𝗺𝗼𝗺 CP Demo": -1004262611728,
  "𝗦𝗽𝘆 𝗰𝗮𝗺𝗲𝗿𝗮 CP Demo": -1004262611728,
    "𝗜𝗻𝗱𝗶𝗮𝗻 𝗚𝗮𝘆 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    "𝗜𝗻𝗱𝗶𝗮𝗻 𝗟𝗲𝘀𝗯𝗶𝗮𝗻𝘀 CP Demo": -1004262611728,
    "𝗠𝘂𝘀𝗹𝗶𝗺 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    # Group D
   "𝗦𝗹𝗲𝗲𝗽𝗶𝗻𝗴 𝘀𝗲𝘅 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    "𝗛𝗶𝗱𝗱𝗲𝗻 𝗖𝗮𝗺 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    "𝗥𝗲𝗱 𝗟𝗶𝗴𝗵𝘁 𝗔𝗿𝗲𝗮 CP Demo": -1004262611728,
    "𝗠𝗮𝗿𝗮𝘁𝗵𝗶 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    "𝗜𝗻𝗱𝗶𝗮𝗻 𝗰𝗼𝗹𝗹𝗲𝗴𝗲 𝗴𝗶𝗿𝗹𝘀 CP Demo": -1004262611728,
    "𝗧𝗲𝗹𝗴𝘂 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    "𝗠𝗮𝗹𝗮𝘆𝗮𝗹𝗮𝗺 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    "𝗞𝗮𝗻𝗻𝗮𝗱𝗮 𝘃𝗶𝗱𝗲𝗼𝘀 CP Demo": -1004262611728,
    "𝗙𝗮𝗺𝗶𝗹𝘆 𝗱𝗲𝘀𝗵𝗶 𝗖𝗵𝘂𝗱𝗮𝗶 CP Demo": -1004262611728,
    # Group E
      "𝗖𝗮𝗿𝘁𝗼𝗼𝗻 𝗦𝗲𝘅 CP Demo": -1004262611728,
    "𝗠𝘂𝗿𝗱𝗲𝗿 CP Demo": -1004262611728,
    "𝗕𝗹𝗮𝗰𝗸𝗺𝗮𝗶𝗹 CP Demo": -1004262611728,
    "𝗧𝗵𝗿𝗲𝗲𝘀𝗼𝗺𝗲 CP Demo": -1004262611728,
    "𝗚𝗮𝗻𝗴𝗯𝗮𝗻𝗴 CP Demo": -1004262611728,
    "𝗠𝗶𝗮 𝗸𝗵𝗮𝗹𝗶𝗳𝗮 CP Demo": -1004262611728,
    "𝗝𝗮𝗽𝗮𝗻𝗲𝘀𝗲 CP Demo": -1004262611728,
    "𝗔𝗻𝗶𝗺𝗮𝗹 𝘀𝗲𝘅 CP Demo": -1004262611728,
    "Bengli CP Demo": -1004262611728,
    "bhajpuri bhabhi CP Demo": -1004262611728,
    "All in one CP Demo": -1003931380677,
    "All complete Combo Package": -1004347644527,
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
