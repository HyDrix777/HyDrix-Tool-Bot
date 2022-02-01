from pyrogram import Client, filters


def aesthetify(string):
    PRINTABLE_ASCII = range(0x21, 0x7f)
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@Client.on_message(
    filters.command(["ae"]))
async def aesthetic(client, message):
    status_message = await message.reply_text("...")
    text = "".join(str(e) for e in message.command[1:])
    text = "".join(aesthetify(text))
    await status_message.edit(text)

# DART------------

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["throw", "dart"])
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


# LUCK------------

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck an @animatedluck """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# GOAL------------ 

# EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["goal", "shoot"])
)
async def roll_shoot(client, message):
    """ @Goal """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# PONG------------ 

# EMOJI CONSTANTS
PONG_E_MOJI = "🎳"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["pog", "ping"])
)
async def pog_ping(client, message):
    """ @pog """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=PONG_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# BASKETBALL------------ 

# EMOJI CONSTANTS
BALL_E_MOJI = "🏀"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["ball", "shoot"])
)
async def ball_shoot(client, message):
    """ @ball """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BALL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# DICE------------ 

# EMOJI CONSTANTS
ROLL_E_MOJI = "🎲"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["roll", "dice"])
)
async def roll_dice(client, message):
    """ @roll """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=ROLL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


# RUN-----------------

import random

RUN_STRINGS = (
    "A broken of a demeanly filled with darkness \
    Why have you come to remind it ",
    "We have become the lives to be the underwater to the underwater that we do not know.",
    "You want the bad call ... but you need good thunder ....",
    "Oh Bloody Grama Virtues!",
    "Sea MUGGie I Am Going to Pay The Bill.",
    "Want with me!",
    "You are not a male chaff !!",
    "I locked it, and the good beach is done by the good beach.",
    "Kindi ... Kindi ...!",
    "Giving the stems and then showing one and show the ISI Mark",
    "Dayveyeese, Kingfisher ... Childe ...!.",
    "You have made your father for half of the midnight?",
    "This is the King of our work.",
    "I'm fetts to feed ...."
    "Mumak is every Bearby Kachyo ...",
    "Oh it moves it .... When we moves it ...",
    "The self of carpenter is the virtue of a carpenter.",
    "Why not to feel this intelligence in Da Vijaya ...!",
    "Where was this time ...."
    "Save me only ...."
    "I know his father's name is Bhavaniami ....",
    "Da Dasa ...",
    "Uppukam's English Salt Mongo Tree .....",
    "Children ..",
    "Your father to Paul ....",
    "Car Engine Out Completely .....",
    "This is the eye or magnety ...",
    "Before falling in the 4th pegging, I will arrive there.",
    "The drunk rains and wast ...."
    "To tell me I love Yo ...."
    "No, the Meenaka of Verbapur is not ....",
    "Look out for the wall!",
    "Get back here!",
    "Don't leave me alone with them!!",
    "Naruto run activated",
    "Hey take responsibilty for what you just did!",
    "Run everyone, they just dropped a bomb 💣😱",
    "Legend has it, they're still running.",
    "Ah, what a waste. I liked that one.",
    "As The Doctor would say... RUN!",
    "Hasta la vista, baby.",
    "And they disappeared forever, never to be seen again.",
)


@Client.on_message(
    filters.command("run")
)
async def run(_, message):
    """ /run strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# lucky number------------

import random

LNM_STRINGS = (
    "1",
    "8",
    "4",
    "7",
    "3",
    "9",
    "5",
    "2",
    "6",
    "10",
)


@Client.on_message(
    filters.command("lnm")
)
async def lnm(_, message):
    """ /lnm strings """
    effective_string = random.choice(LNM_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# LOVE-------

import random

LOV_STRINGS = (
    "(๑♡⌓♡๑)",
    "꒰⑅ᵕ༚ᵕ꒱˖♡",
    "♡˖꒰ᵕ༚ᵕ⑅꒱",
    "(◍•ᴗ•◍)❤",
    "(✿ ♡‿♡)",
    "♡(ӦｖӦ｡)",
    "(灬º‿º灬)♡",
    "( ˘ ³˘)♥",
    "(っ˘з(˘⌣˘ )",
    "(๑˙❥˙๑)",
    "(●’3)♡(ε`●)",
    "(๑♡⌓♡๑)",
    "(｡♡‿♡｡)",
    "(●♡∀♡)",
    "( ◜‿◝ )♡",
    "♡(> ਊ <)♡",
)


@Client.on_message(
    filters.command("love")
)
async def love(_, message):
    """ /love strings """
    effective_string = random.choice(LOV_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# SHRUGLE-------

import random

SRG_STRINGS = (
    "¯\_(ツ)_/¯",
    "¯\_༼ •́ ͜ʖ •̀ ༽_/¯",
    "¯\_( ͡° ͜ʖ ͡°)_/¯",
    "乁༼☯‿☯✿༽ㄏ",
    "¯\_༼ᴼل͜ᴼ༽_/¯",
    "乁[ᓀ˵▾˵ᓂ]ㄏ",
    "¯\_(☯෴☯)_/¯",
    "乁ʕ •̀ ۝ •́ ʔㄏ",
    "乁║ ˙ 益 ˙ ║ㄏ",
    "乁( ⁰͡ Ĺ̯ ⁰͡ ) ㄏ",
    "¯\_〳 •̀ o •́ 〵_/¯",
    "乁( •_• )ㄏ",
    "乁[ ◕ ᴥ ◕ ]ㄏ",
    "¯\_ʘ‿ʘ_/¯",
    "¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "¯\(◉‿◉)/¯",
)


@Client.on_message(
    filters.command("shrug")
)
async def shrug(_, message):
    """ /shrug strings """
    effective_string = random.choice(SRG_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# TOSS TAIL-------

import random

THT_STRINGS = (
    "Heads",
    "Tails",
    "Tails",
    "Heads",
    "Tails",
    "Heads",
    "Heads",
    "Heads",
    "Tails",
    "Tails",
)


@Client.on_message(
    filters.command("toss")
)
async def toss(_, message):
    """ /toss strings """
    effective_string = random.choice(THT_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)


#  TABLE--------

import random

TBL_STRINGS = (
    "(ノಠ益ಠ)ノ彡┻━┻",
    "(╯°□°）╯︵ ┻━┻",
    "(┛◉Д◉)┛彡┻━┻",
    "(ﾉ≧∇≦)ﾉ ﾐ ┻━┻",
    "(ﾉ´･ω･)ﾉ ﾐ ┻━┻",
    "(┛ಸ_ಸ)┛彡┻━┻",
    "(╯ರ ~ ರ)╯︵ ┻━┻",
    "(ノಥ,_｣ಥ)ノ彡┻━┻",
    "(┛✧Д✧))┛彡┻━┻",
    "┻┻︵¯\(ツ)/¯︵┻┻",
    "┻┻︵ヽ(`Д´)ﾉ︵┻┻",
    "(/¯◡ ‿ ◡)/¯ ~ ┻━┻",
    "┻━┻ミ＼(≧ﾛ≦＼)",
    "(ノ￣皿￣)ノ ⌒== ┫",
    "(┛❍ᴥ❍)┛彡┻━┻",
    "─=≡Σ(╯°□°)╯︵┻┻",
    "┻━┻ ヘ╰( •̀ε•́ ╰)",
    "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
    "(ヘ･_･)ヘ┳━┳",
    "I ran out of tables, will order more.",
    "Go do some work instead of flippin tables.",
)


@Client.on_message(
    filters.command("table")
)
async def table(_, message):
    """ /table strings """
    effective_string = random.choice(TBL_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

#  YES OR NO--------

import random

DCD_STRINGS = (
    "Yes",
    "No",
)


@Client.on_message(
    filters.command("decide")
)
async def decide(_, message):
    """ /decide strings """
    effective_string = random.choice(DCD_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
