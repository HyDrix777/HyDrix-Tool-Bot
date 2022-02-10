import os, logging, asyncio
from telegraph import upload_file
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from bot import Client, filters





logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


moment_worker = []




# Mention All

@Client.on(events.NewMessage(pattern="^/tagall|/call|/tall|/all|#all|@all?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.respond("Use This In Channel or Group!")
  
  admins = []
  async for admin in decodebot.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Only Admin can use it.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("I can't Mention Members for Old Post!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Give me can an Argument. Ex: `/tag Hey, Where are you`")
  else:
    return await event.respond("Reply to Message or Give Some Text To Mention!")
    
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in decodebot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped!")
        return
      if usrnum == 5:
        await decodebot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in decodebot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped")
        return
      if usrnum == 5:
        await decodebot.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


# Cancle 

@Client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__There is no proccess on going...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('**__Stoped__**\n\n**__Powered By:__ @music_galaxy_dl"**')




print("Started Successfully Join Support")
print("¯\_(ツ)_/¯ Need Help Join @music_galaxy_dl")
