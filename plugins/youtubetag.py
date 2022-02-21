import os
import pyrogram
from pyrogram import Client, filters
from youtubesearchpython import VideosSearch
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import YoutubeTags
from YoutubeTags import videotags





@Client.on_message(filters.regex("https://www.youtube.com") | filters.regex("http://www.youtube.com") | filters.regex("https://youtu.be/") | filters.regex("https://www.youtu.be/") | filters.regex("http://www.youtu.be/"))
async def tag(bot, message):
    link = str(message.text)
    tags = videotags(link) 
    if tags=="":
         await message.reply_text(" `Nᴏ ᴛᴀɢ ғᴏᴜɴᴅ 🔖`")
    else:
         await message.reply_text(text=f"__Sᴇʟᴇᴄᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴄᴄᴏᴍᴘʟɪsʜ ᴡɪᴛʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ__\n\n__Tʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴛᴀɢs ᴜsᴇᴅ ғᴏʀ ᴛʜᴇ ᴠɪᴅᴇᴏ ʏᴏᴜ sᴇɴᴅ ᴍᴇ__\n\n\n ` {tags} ` \n\n\n ♥️ Pᴏᴡᴇʀᴇᴅ ʙʏ : @HTGToolBot")

@Client.on_inline_query()
async def search(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="Type video name here..",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(search_query, limit=50)

        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=" {} .".format(
                       v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="**Error: Sᴇᴀʀᴄʜ ᴛɪᴍᴇᴅ ᴏᴜᴛ❌**",
                switch_pm_parameter="",
            )
