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
    filters.command(["pog", "piong"])
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

# Truth-------

TRUTH_STRINGS = (
    " What’s the last lie you told?",
    "What was the most embarrassing thing you’ve ever done on a date?",
    "Have you ever accidentally hit something (or someone!) with your car?",
    "Name someone you’ve pretended to like but actually couldn’t stand.",
    "What’s your most bizarre nickname?",
    "What’s been your most physically painful experience?",
    "What bridges are you glad that you burned?",
    "What’s the craziest thing you’ve done on public transportation?",
    "If you met a genie, what would your three wishes be?",
    "If you could write anyone on Earth in for President of the United States, who would it be and why?",
    "What’s the meanest thing you’ve ever said to someone else?",
    "Who was your worst kiss ever?",
    "What’s one thing you’d do if you knew there no consequences?",
    "What’s the craziest thing you’ve done in front of a mirror?",
    "What’s the meanest thing you’ve ever said about someone else?",
    "What’s something you love to do with your friends that you’d never do in front of your partner?",
    "Who are you most jealous of?",
    "What do your favorite pajamas look like?",
    "Have you ever faked sick to get out of a party?",
    "Who’s the oldest person you’ve dated?",
    "How many selfies do you take a day?",
    "Meatloaf says he’d do anything for love, but he won’t do “that.” What’s your “that?”",
    "How many times a week do you wear the same pants?",
    "Would you date your high school crush today?",
    "Where are you ticklish?",
    "Do you believe in any superstitions? If so, which ones?",
    "What’s one movie you’re embarrassed to admit you enjoy?",
    "What’s your most embarrassing grooming habit?",
    "When’s the last time you apologized? What for?",
    "How do you really feel about the Twilight saga?",
    "Where do most of your embarrassing odors come from?",
    "Have you ever considered cheating on a partner?",
    "Have you ever cheated on a partner?",
    "Boxers or briefs?",
    "Have you ever peed in a pool?",
    "What’s the weirdest place you’ve ever grown hair?",
    "If you were guaranteed to never get caught, who on Earth would you murder?",
    "What’s the cheapest gift you’ve ever gotten for someone else?",
    "What app do you waste the most time on?",
    "What’s the weirdest thing you’ve done on a plane?",
    "Have you ever been nude in public?",
    "How many gossip blogs do you read a day?",
    "What is the youngest age partner you’d date?",
    "Have you ever picked your nose in public?",
    "Have you ever lied about your age?",
    "If you had to delete one app from your phone, which one would it be?",
    "What’s your most embarrassing late night purchase?",
    "What’s the longest you’ve gone without showering?",
    "Have you ever used a fake ID?",
    "Who’s your hall pass?",
    "Be honest: Do you have a favorite child?",
    "Which of your family members annoys you the most and why?",
    "What is your greatest fear in a relationship?",
    "What’s your biggest pet peeve about the person to your left?",
    "What’s the most embarrassing text in your phone right now?",
    "Have you ever seen a dead body?",
    "What celebrity do you think is overrated?",
    "Have you ever lied to your boss?",
    "Have you ever stolen something from work?",
    "What’s the longest you’ve gone without brushing your teeth?",
    "What’s your biggest regret in life?",
    "Who would you hate to see naked?",
    "Describe the weirdest thing you’ve ever done while inebriated.",
    "Have you ever regifted a present?",
    "Would you break up with your partner for $1 million?",
    "Have you ever had a crush on a coworker?",
    "Do you still have feelings for any of your exes?",
    "What’s the smallest tip you’ve ever left at a restaurant?",
    "Have you ever regretted something you did to get a crush or partner’s attention?",
    "What’s one job you could never do?",
    "Have you ever ghosted a friend?",
    "Have you ever ghosted a partner?",
    "What’s the most scandalous photo in your cloud?",
    "If you switched genders for a day, what would you do?",
    "How many photo editing apps do you have on your phone?",
    "How many pairs of granny panties do you own?",
    "What are your favorite and least favorite of your body parts?",
    "When’s the last time you got dumped?",
    "What’s the most childish thing you still do?",
    "When’s the last time you dumped someone?",
    "If you had to pick someone in this room to be your partner on a game show, who would it be and why?",
    "Would you date someone shorter than you?",
    "Have you ever lied for a friend?",
    "Name one thing you’d change about every person in this room.",
    "When’s the last time you made someone else cry?",
    "What’s the most embarrassing thing you’ve done in front of a crowd?",
    "If you could become invisible, what’s the worst thing you’d do?",
    "After you’ve dropped a piece of food, what’s the longest time you’ve left it on the floor before eating it?",
    "What’s one thing in your life you wish you could change?",
    "If you could date two people at once, would you do it? If so, who?",
    "What’s something that overwhelms you?",
    "What was the greatest day of your life?",
    "What’s one useless skill you’d love to learn anyway?",
    "If I went through your cabinets, what’s the weirdest thing I’d find?",
    "Have you ever farted and blamed it on someone else?",
    "What’s the worst thing you’ve ever done at work?",
    "How many people have you kissed?",
    "What’s your number?",
    "Have you ever gotten mad at a friend for posting an unflattering picture of you?",
    "What’s your most absurd dealbreaker?",
    "Who in this room would you list as your emergency contact?",
    "What’s something you would die if your mom found out about?",
    "What’s the scariest thing that’s ever happened to you?",
    "If you could set anyone here up with your best friend, who would it be and why?",
    "How often do you wash your sheets?",
    "Have you ever farted in an elevator?",
    "Who was your first love?",
    "What’s the last purchase you regretted?",
    "Have you ever sent a sext?",
    "Have you ever sent a sext to the wrong person? Who?",
    "What’s the weirdest dream you’ve ever had?",
    "Have you ever had a one-night stand?",
    "Are you scared of getting old?",
    "What do you want on your tombstone?",
    "If you had one week to live and you had to marry someone in this room, who would it be?",
    "What’s the last movie that made you cry?",
    "List one positive and one negative thing about everyone in the room.",
    "When was your first time?",
    "Who was your first?",
    "What’s the most sinful thing you’ve done in a house of worship?",
    "Who would you call to help bury a body?",
    "Who would call you to help bury a body? Would you do it?",
    "When’s the last time you cried and why?",
    "What’s your favorite possession?",
    "Has anyone ever walked in on you in the bathroom?",
    "Who in this group would you want to swap lives with for a week?",
    "What was your biggest fear as a child?",
    "What’s your biggest fear today?",
    "What’s the most embarrassing thing your parents have caught you doing?",
    "Name a band you only pretend to like.",
    "What’s the last song that made you cry?",
    "Have you ever had a wardrobe malfunction?",
    "What’s the last thing you Googled?",
    "What is that one thing you would never do for all the money in the world?",
    "Who is your favorite person in your immediate family?",
    "If you could only hear one song for the rest of your life, what would it be?",
    "When’s the last time your partner embarrassed you?",
)

@Client.on_message(
    filters.command("truth")
)
async def truth(_, message):
    """ /truth strings """
    effective_string = random.choice(TRUTH_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
