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

# Rather-------

WYR_STRINGS = (
    "Would you rather 🔴 go into the past and meet your ancestors or 🔵 go into the future and meet your great-great grandchildren?",
    "Would you rather 🔴 have more time or 🔵 more money?",
    "Would you rather 🔴 have a rewind button or 🔵 a pause button on your life?",
    "Would you rather 🔴 be able to talk with the animals or 🔵 speak all foreign languages?",
    "Would you rather 🔴 win the lottery or 🔵 live twice as long?",
    "Would you 🔴 feel worse if no one showed up to your wedding or 🔵 to your funeral?",
    "Would you rather 🔴 be without internet for a week, or 🔵 without your phone?",
    "Would you rather 🔴 meet your Nikola Tesla, or 🔵 the Elbert Einstein?",
    "Would you rather 🔴 the aliens that make first contact be robotic or 🔵 organic?",
    "Would you rather 🔴 lose the ability to read or 🔵 lose the ability to speak?",
)

@Client.on_message(
    filters.command("rather")
)
async def rather(_, message):
    """ /rather strings """
    effective_string = random.choice(WYR_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Dare-----

DARE_STRINGS = (
    "Change your profile pic to some naked character for 3 days.",
    "Do a photograph reveal.",
    "Share your telegram password.",
    "Send 'I Love You' to 20 people in your PM [Private Messaging] list and share screenshots of the task.",
    "Send hentai to 10 people in your PM [Private Messaging list and share screenshots of the task.",
    "Send your phone number to 10 people in the group and share screenshots of the task.",
    "Share your every social media account username.",
    "Send most embarrising photograph.",
    "Send 'I want your nudes' to 10 people in your PM [Private Messaging list and share screenshots of the task.]",
    "Make your phone number public for 3 minutes.",
    "Set your bio as, 'I am gay and I want to sleep with the person reading this right now' for 2 days.",
    "Send the pictures of your ex's panties.",
    "Ask for nudes from strangers and share screenshots of the task.",
    "Share screenshot from most recent chat on WhatsApp.",
    "Join/Start Voice Chat and sing a song.",
    "Join/Start Voice Chat and say, 'Ara Ara', in sexy voice",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and shout 'Fuck you all'. [Screen Record the task and send it in group.]",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and seduce a person. [Screen Record the task and send it in group.]",
    "Download a nude pic using google, PM it to a member of random Anime themed Group with caption as, 'These nudes are mine, wanna share yours?'. [Share screenshots of the task.]",
    "Open the top most chat on your PM List and screen record chat for last 3 days and send it in group.",
    "Reveal your instagram password to someone who is online.",
    "Click a photo of yours right now and send it in group.",
    "Set your bio as, 'Free blowjob if you send your nudes.' for 2 days.",
    "Join/Start Voice Chat and say, 'Onii Chan no Hentai', in sexy voice.",
    "Let someone from the players log in to your Telegram account.",
    "Send 10 most recent images from your galary.",
    "Send more suggestions to @A_lonelyPerson",
)

@Client.on_message(
    filters.command("dare")
)
async def dare(_, message):
    """ /dare strings """
    effective_string = random.choice(DARE_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Tord------

TORD_STRINGS = (
    "Change your profile pic to a dog.",
    "Do a photograph reveal.",
    "Share your telegram password.",
    "Send 'I Love You' to 20 people in your PM [Private Messaging] list and share screenshots of the task.",
    "Send hentai to 10 people in your PM [Private Messaging list and share screenshots of the task.",
    "Send your phone number to 10 people in the group and share screenshots of the task.",
    "Share your every social media account username.",
    "Send most embarrising photograph.",
    "Send 'I want your nudes' to 10 people in your PM [Private Messaging list and share screenshots of the task.",
    "Make your phone number public for 3 minutes.",
    "Set your bio as, 'I am gay and I want to sleep with the person reading this right now' for 2 days.",
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
    "Who will be your choice to become your boyfriend/girlfriend from the group?",
    "If you had a chance to kill someone, who would it be from the group?",
    "Who is the most hated and liked person in your group from your perspective?",
    "Have you ever loved someone, if so, who was it and for how long, if not, how will you show your love to them?",
    "If you were asked to propose someone from your friends on Telegram, who will be your first choice and why?",
    "If you were to hate someone from your friends on Telegram, who will be your first choice and why?",
    "What are your views on the topic of Human Cannibalism?",
    "If you were asked to kill someone in your most horrific way, how will it be?",
    "Join/Start Voice Chat and sing a song.",
    "Join/Start Voice Chat and say, 'Ara Ara', in sexy voice",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and shout 'Fuck you all'. [Screen Record the task and send it in group.]",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and seduce a person. [Screen Record the task and send it in group.]",
    "Download a nude pic using google, PM it to a member of random Anime themed Group with caption as, 'These nudes are mine, wanna share yours?'. [Share screenshots of the task.]",
    "Open the top most chat on your PM List and screen record chat for last 3 days and send it in group.",
    "Reveal your instagram password to someone who is online.",
    "Click a photo of yours right now and send it in group.",
    "Set your bio as, 'Free blowjob if you send your nudes.' for 2 days.",
    "Join/Start Voice Chat and say, 'Onii Chan no Hentai', in sexy voice.",
    "Let someone from the players log in to your Telegram account.",
    "Send 10 most recent images from your galary.",
)

@Client.on_message(
    filters.command("tord")
)
async def tord(_, message):
    """ /tord strings """
    effective_string = random.choice(TORD_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Good night----

GDNIGHT_STRINGS = (
    "`Good night keep your dreams alive`",
    "`Night, night, to a dear friend! May you sleep well!`",
    "`May the night fill with stars for you. May counting every one, give you contentment!`",
    "`Wishing you comfort, happiness, and a good night’s sleep!`",
    "`Now relax. The day is over. You did your best. And tomorrow you’ll do better. Good Night!`",
    "`Good night to a friend who is the best! Get your forty winks!`",
    "`May your pillow be soft, and your rest be long! Good night, friend!`",
    "`Let there be no troubles, dear friend! Have a Good Night!`",
    "`Rest soundly tonight, friend!`",
    "`Have the best night’s sleep, friend! Sleep well!`",
    "`Have a very, good night, friend! You are wonderful!`",
    "`Relaxation is in order for you! Good night, friend!`",
    "`Good night. May you have sweet dreams tonight.`",
    "`Sleep well, dear friend and have sweet dreams.`",
    "`As we wait for a brand new day, good night and have beautiful dreams.`",
    "`Dear friend, I wish you a night of peace and bliss. Good night.`",
    "`Darkness cannot last forever. Keep the hope alive. Good night.`",
    "`By hook or crook you shall have sweet dreams tonight. Have a good night, buddy!`",
    "`Good night, my friend. I pray that the good Lord watches over you as you sleep. Sweet dreams.`",
    "`Good night, friend! May you be filled with tranquility!`",
    "`Wishing you a calm night, friend! I hope it is good!`",
    "`Wishing you a night where you can recharge for tomorrow!`",
    "`Slumber tonight, good friend, and feel well rested, tomorrow!`",
    "`Wishing my good friend relief from a hard day’s work! Good Night!`",
    "`Good night, friend! May you have silence for sleep!`",
    "`Sleep tonight, friend and be well! Know that you have done your very best today, and that you will do your very best, tomorrow!`",
    "`Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow!`",
    "`Friend, I want to remind you that your strong mind has brought you peace, before. May it do that again, tonight! May you hold acknowledgment of this with you!`",
    "`Wishing you a calm, night, friend! Hoping everything winds down to your liking and that the following day meets your standards!`",
    "`May the darkness of the night cloak you in a sleep that is sound and good! Dear friend, may this feeling carry you through the next day!`",
    "`Friend, may the quietude you experience tonight move you to have many more nights like it! May you find your peace and hold on to it!`",
    "`May there be no activity for you tonight, friend! May the rest that you have coming to you arrive swiftly! May the activity that you do tomorrow match your pace and be all of your own making!`",
    "`When the day is done, friend, may you know that you have done well! When you sleep tonight, friend, may you view all the you hope for, tomorrow!`",
    "`When everything is brought to a standstill, friend, I hope that your thoughts are good, as you drift to sleep! May those thoughts remain with you, during all of your days!`",
    "`Every day, you encourage me to do new things, friend! May tonight’s rest bring a new day that overflows with courage and exciting events!`",
)

@Client.on_message(
    filters.command("goodnight")
)
async def goodnight(_, message):
    """ /goodnight strings """
    effective_string = random.choice(GDNIGHT_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Gmorning----

GDMORNING_STRINGS = (
    "`Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning!`",
    "`It doesn’t matter how bad was your yesterday. Today, you are going to make it a good one. Wishing you a good morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good morning!`",
    "`May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!`",
    "`May the sun shower you with blessings and prosperity in the days ahead. Good morning!`",
    "`Every sunrise marks the rise of life over death, hope over despair and happiness over suffering. Wishing you a very enjoyable morning today!`",
    "`Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time!`",
    "`Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today. Wishing you a very good morning!`",
    "`You have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning! Good morning to you!`",
    "`Waking up in such a beautiful morning is a guaranty for a day that’s beyond amazing. I hope you’ll make the best of it. Good morning!`",
    "`Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile. Good morning! Wishing you a great day.`",
    "`Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. Wishing you a wonderful morning!`",
    "`Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning!`",
    "`A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!`",
    "`The darkness of night has ended. A new sun is up there to guide you towards a life so bright and blissful. Good morning dear!`",
    "`Wake up, have your cup of morning tea and let the morning wind freshen you up like a happiness pill. Wishing you a good morning and a good day ahead!`",
    "`Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning! Have a wonderful day ahead.`",
    "`A bad day will always have a good morning, hope all your worries are gone and everything you wish could find a place. Good morning!`",
    "`A great end may not be decided but a good creative beginning can be planned and achieved. Good morning, have a productive day!`",
    "`Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your “Good Morning” have a nice day!`",
    "`Anything can go wrong in the day but the morning has to be beautiful, so I am making sure your morning starts beautiful. Good morning!`",
    "`Open your eyes with a smile, pray and thank god that you are waking up to a new beginning. Good morning!`",
    "`Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning.`",
    "`Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good Morning!`",
    "`Birds are singing sweet melodies and a gentle breeze is blowing through the trees, what a perfect morning to wake you up. Good morning!`",
    "`This morning is so relaxing and beautiful that I really don’t want you to miss it in any way. So, wake up dear friend. A hearty good morning to you!`",
    "`Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning!`",
    "`Every morning brings you new hopes and new opportunities. Don’t miss any one of them while you’re sleeping. Good morning!`",
    "`Start your day with solid determination and great attitude. You’re going to have a good day today. Good morning my friend!`",
    "`Friendship is what makes life worth living. I want to thank you for being such a special friend of mine. Good morning to you!`",
    "`A friend like you is pretty hard to come by in life. I must consider myself lucky enough to have you. Good morning. Wish you an amazing day ahead!`",
    "`The more you count yourself as blessed, the more blessed you will be. Thank God for this beautiful morning and let friendship and love prevail this morning.`",
    "`Wake up and sip a cup of loving friendship. Eat your heart out from a plate of hope. To top it up, a fork full of kindness and love. Enough for a happy good morning!`",
    "`It is easy to imagine the world coming to an end. But it is difficult to imagine spending a day without my friends. Good morning.`",
)

@Client.on_message(
    filters.command("morning")
)
async def morning(_, message):
    """ /morning strings """
    effective_string = random.choice(GDMORNING_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Abuse----

ABUSE_STRINGS = (
    "Owww ... Such a stupid idiot.",
    "Don't drink and type.",
    "I think you should go home or better a mental asylum.",
    "Command not found. Just like your brain.",
    "Do you realize you are making a fool of yourself? Apparently not.",
    "You can type better than that.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "Sorry, we do not sell brains.",
    "Believe me you are not normal.",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "Zombies eat brains... you're safe.",
    "You didn't evolve from apes, they evolved from you.",
    "Come back and talk to me when your I.Q. exceeds your age.",
    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.",
    "What language are you speaking? Cause it sounds like bullshit.",
    "Stupidity is not a crime so you are free to go.",
    "You are proof that evolution CAN go in reverse.",
    "I would ask you how old you are but I know you can't count that high.",
    "As an outsider, what do you think of the human race?",
    "Brains aren't everything. In your case they're nothing.",
    "Ordinarily people live and learn. You just live.",
    "I don't know what makes you so stupid, but it really works.",
    "Keep talking, someday you'll say something intelligent! (I doubt it though)",
    "Shock me, say something intelligent.",
    "Your IQ's lower than your shoe size.",
    "Alas! Your neurotransmitters are no more working.",
    "Are you crazy you fool.",
    "Everyone has the right to be stupid but you are abusing the privilege.",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",
    "You should try tasting cyanide.",
    "Your enzymes are meant to digest rat poison.",
    "You should try sleeping forever.",
    "Pick up a gun and shoot yourself.",
    "You could make a world record by jumping from a plane without parachute.",
    "Stop talking BS and jump in front of a running bullet train.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.",
    "Go Green! Stop inhaling Oxygen.",
    "God was searching for you. You should leave to meet him.",
    "give your 100%. Now, go donate blood.",
    "Try jumping from a hundred story building but you can do it only once.",
    "You should donate your brain seeing that you never used it.",
    "Volunteer for target in an firing range.",
    "Head shots are fun. Get yourself one.",
    "You should try swimming with great white sharks.",
    "You should paint yourself red and run in a bull marathon.",
    "You can stay underwater for the rest of your life without coming back up.",
    "How about you stop breathing for like 1 day? That'll be great.",
    "Try provoking a tiger while you both are in a cage.",
    "Have you tried shooting yourself as high as 100m using a canon.",
    "You should try holding TNT in your mouth and igniting it.",
    "Try playing catch and throw with RDX its fun.",
    "I heard phogine is poisonous but i guess you wont mind inhaling it for fun.",
    "Launch yourself into outer space while forgetting oxygen on Earth.",
    "You should try playing snake and ladders, with real snakes and no ladders.",
    "Dance naked on a couple of HT wires.",
    "Active Volcano is the best swimming pool for you.",
    "You should try hot bath in a volcano.",
    "Try to spend one day in a coffin and it will be yours forever.",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
    "You can be the first person to step on sun. Have a try.",
)

@Client.on_message(
    filters.command("abuse")
)
async def abuse(_, message):
    """ /abuse strings """
    effective_string = random.choice(ABUSE_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
