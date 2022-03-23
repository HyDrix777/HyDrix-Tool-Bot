from pyrogram import Client , filters 
from pyyoutube import Data

        
 
@Client.on_message(filters.group & filters.regex("^https?:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}"))
async def tagremove(bot, message):
	ms = await message.reply_text('🤔')
	link = message.text
	yt = Data(link)
	title = yt.title
	thumb = yt.thumbnails
	views = yt.views
	likes = yt.likes
	dislikes = yt.dislikes
	publishdate = yt.publishdate
	category = yt.category
	subscriber = yt.subscriber
	channel_name = yt.channel_name
	cap = f"""
	Title :-  {title}
	Views :- {views}
	likes: - {likes}
	Dislikes :- {dislikes}
	Category :- {category}
	channel_name :- {channel_name}
	subscriber :- {subscriber}
	publishdate :- {publishdate}	
	"""
	await app.send_photo(message.chat.id,thumb,caption= cap)
	await ms.delete()

