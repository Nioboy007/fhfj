from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your Telegram API credentials
api_id = '10471716'
api_hash = 'f8a1b21a13af154596e2ff5bed164860'
bot_token = '6365859811:AAGK5hlLKtLf-RqlaEXngZTWnfSPISerWPI'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start"))
async def start_command(client, message):
    start_text = "Welcome! Click on the buttons below:"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Help", callback_data="help")],
            [InlineKeyboardButton("Test", callback_data="test")],
        ]
    )
    await message.reply_text(start_text, reply_markup=keyboard)


@app.on_callback_query()
async def handle_callback(client, callback_query):
    data = callback_query.data
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.id

    if data == "help":
        await client.edit_message_text(
            chat_id,
            message_id,
            "Help is coming!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="back")]]
            ),
        )
    elif data == "back":
        await client.edit_message_text(
            chat_id,
            message_id,
            "Welcome! Click on the buttons below:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Help", callback_data="help")],
                    [InlineKeyboardButton("Test", callback_data="test")],
                ]
            ),
        )
    elif data == "test":
        await client.send_message(chat_id, "Working!")

app.run()
