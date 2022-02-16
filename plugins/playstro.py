import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *





@Client.on_message(filters.private & filters.command("pstor"))
async def pstor(bot, update):
    text = "▶️ __Search play store apps using below buttons__.\n\nMy group : @Music_Galaxy_Dl"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="sᴇᴀʀᴄʜ ʜᴇʀᴇ", switch_inline_query_current_chat="")],
            [InlineKeyboardButton(text="sᴇᴀʀᴄʜ ɪɴ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀᴛ", switch_inline_query="")]
        ]
    )
    await update.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_inline_query()
async def search(bot, update):
    results = play_scraper.search(update.query)
    answers = []
    for result in results:
        details = "**Title:** `{}`".format(result["title"]) + "\n" \
        "**Description:** `{}`".format(result["description"]) + "\n" \
        "**App ID:** `{}`".format(result["app_id"]) + "\n" \
        "**Developer:** `{}`".format(result["developer"]) + "\n" \
        "**Developer ID:** `{}`".format(result["developer_id"]) + "\n" \
        "**Score:** `{}`".format(result["score"]) + "\n" \
        "**Price:** `{}`".format(result["price"]) + "\n" \
        "**Full Price:** `{}`".format(result["full_price"]) + "\n" \
        "**Free:** `{}`".format(result["free"]) + "\n" \
        "\n" + "ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ @HTGToolBot 🤖"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ᴘʟᴀʏ sᴛᴏʀᴇ", url="https://play.google.com"+result["url"])]]
        )
        try:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description=result.get("description", None),
                    thumb_url=result.get("icon", None),
                    input_message_content=InputTextMessageContent(
                        message_text=details, disable_web_page_preview=True
                    ),
                    reply_markup=reply_markup
                )
            )
        except Exception as error:
            print(error)
    await update.answer(answers)
