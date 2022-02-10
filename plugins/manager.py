from pyrogram import Client , filters
import wget
import os
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
import psutil
import requests
import json
import subprocess


sudo_users = 1520625615 , 1871813121
owner_id = [1871813121]




@Client.on_message(filters.command(["ban"]))
async def ban (client , message):
    try:
        get =await client.get_chat_member(message.chat.id,message.from_user.id) 
        status = get. status 
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id
        cmd_user = ["administrator","creator"] 
        if status in cmd_user:
            chat_id = message.chat.id
            user_id  = message.reply_to_message.from_user.id
            await ZeroTwo.ban_chat_member(chat_id, user_id)
            await message.reply_text(text= "**BANNED SUCCESFULLY**")
        else:
            await message.reply_text(text = "** YOU ARE NOT A ADMIN IN THIS CHAT **")
    except:
        await message.reply_text("**Error Occured Report in Support Group!!**")


@Client.on_message(filters.command(["unban"]))
async def unban (client , message):
    try:
        get =await client.get_chat_member(message.chat.id,message.from_user.id) 
        status = get. status 
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id
        cmd_user = ["administrator","creator"] 
        if status in cmd_user:
            chat_id = message.chat.id
            user_id  = message.reply_to_message.from_user.id
            await ZeroTwo.unban_chat_member(chat_id, user_id)
            await message.reply_text(text= "**UNBANNED SUCCESFULLY**")
        else:
            await message.reply_text(text = "** YOU ARE NOT A ADMIN IN THIS CHAT **")
    except:
        await message.reply_text("**Error Occured Report in Support Group!!**")


@Client.on_message(filters.command(["promote"]))
async def promote (client , message):
    try:
        get =await client.get_chat_member(message.chat.id,message.from_user.id) 
        status = get. status 
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id
        cmd_user = ["administrator","creator"] 
        if status in cmd_user:
            user_id = message.reply_to_message.from_user.id
            await ZeroTwo.promote_chat_member(chat_id, user_id)
            await ZeroTwo.send_message(chat_id, "promoted successfully")
        else:
            await message.reply_text("You don't have enough rights!!")
    except:
        await message.reply_text("ERROR OCCURED TRY CONTACTING OUR SUPPORT GROUP")

@Client.on_message(filters.command(["pin"]))
async def pin (client , message):
  try:
      get =await client.get_chat_member(message.chat.id,message.from_user.id) 
      status = get. status 
      chat_id = message.chat.id
      message_id = message.reply_to_message.message_id
      cmd_user = ["administrator","creator"] 
      if status in cmd_user:
          await ZeroTwo.pin_chat_message(chat_id, message_id)
          await message.reply_text(text = "Pinned to Top🥺")
      
      else:
          await message.reply_text('Only Admin Can Pin Messages')
  except:
        await message.reply_text("REPLY TO A MESSAGE TO PIN IT ")

@Client.on_message(filters.command(["admintitle"]))
async def adminTITLE(client , message):
    chat_id = message.chat.id
    get =await client.get_chat_member(message.chat.id,message.from_user.id) 
    status = get.status
    cmd_user = ["administrator","creator"]
    msg = message.text
    title = msg.split(' ')[1]
    user_id = message.reply_to_message.from_user.id
    try:
        if status in cmd_user:
            await ZeroTwo.set_administrator_title(chat_id, user_id, title)
            await message.reply_text("title updated")
        else:
            await ZeroTwo.send_message(chat_id, "you dont have enough rights , to make changes!!")
    except:
            await message.reply_text("ERROR OCCURED TRY CONTACTING OUR SUPPORT GROUP")


@Client.on_message(filters.command(["eval"]))
async def eval (client , message):
    chat_id = message.chat.id
    inputgot = message.text[0]
    string = subprocess.run([inputgot], capture_output=True)
    await message.reply(text = string)



@Client.on_message(filters.command(["adminlist"]))
async def adminlist (client , message):
    chat_id = message.chat.id
    chat_name = message.chat.username
    async for member in ZeroTwo.iter_chat_members(chat_name, filter="administrators"):
        print(member.user.first_name + ' is admin!')
        await message.reply_text(text = member.user.first_name + ' is admin!')

