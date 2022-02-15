from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from os import environ





GUESS_COUNT = int(environ.get("GUESS_COUNT", ""))

MAX_GUESSES = int(environ.get("MAX_GUESSES", ""))

SECRET_WORD = environ.get("Any word that you want your users to guess")




guess = ""
out_of_guesses = False

@Client.on_message(filters.command("guess"))
async def guess(bot, m:Message):
  await m.reply_text(START_TXT.format(m.from_user.mention),
  reply_markup=InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("Start Guessing", callback_data="game")
    ]]
  ))

@Client.on_callback_query("game")
async def game(bot, m:Message, guess, out_of_guesses):
  while guess != SECRET_WORD and not(out_of_guesses):
    if GUESS_COUNT < MAX_GUESSES:
      guess = await m.reply_text(f"Enter your guesses : ")
      GUESS_COUNT += 1
    else:
      out_of_guesses = True
      
  if out_of_guesses:
    await m.reply_text("Sorry, " + (m.from_user.mention) + " You're out of guesses, YOU LOSE")
  else:
    await m.reply_text("Hurray " + (m.from_user.mention) + " You've won the guess")

