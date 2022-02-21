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
         await message.reply_text(" `𝐍𝐨 𝐓𝐚𝐠𝐬 𝐅𝐨𝐮𝐧𝐝 🔖`")
    else:
         await message.reply_text(text=f"** 𝑺𝒆𝒍𝒆𝒄𝒕 𝒘𝒉𝒂𝒕 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒂𝒄𝒄𝒐𝒎𝒑𝒍𝒊𝒔𝒉 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒃𝒖𝒕𝒕𝒐𝒏 𝒃𝒆𝒍𝒐𝒘 **\n\n𝓣𝓱𝓮𝓼𝓮 𝓪𝓻𝓮 𝓽𝓱𝓮 𝓽𝓪𝓰𝓼 𝓾𝓼𝓮𝓭 𝓯𝓸𝓻 𝓽𝓱𝓮 𝓿𝓲𝓭𝓮𝓸 𝔂𝓸𝓾 𝓼𝓮𝓷𝓽 𝓶𝓮\n\n\n ` {tags} ` \n\n\n 🔥 Pọwẹrẹɗ Ɓy : @mrkpbots\n\n☘️ 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 : @rajeshsaini2115",reply_markup=BUTTON)
 

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
                switch_pm_text="**Error: Search timed out❌**",
                switch_pm_parameter="",
            )
