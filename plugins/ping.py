
import time
from pyrogram import Client, filters
from infog import (
    COMMAND_HAND_LER
)
from plugins.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "Glad to hear that and really nice to know that I am not talking to a ghost."
HELP = "CAACAgUAAxkBAAEBTsthlWY_Pte1RC4yhz3nD1utGagSSwAC0gIAAsaPcVUSPJS_m8rS5h4E"



@Client.on_message(
    filters.command(["alive", "start"], COMMAND_HAND_LER) &
    f_onw_fliter
)
async def check_alive(_, message):
    await message.reply_text(ALIVE)



@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"HyDrix Tools Bot is working good with a ping of `{time_taken_s:.3f} ms`\n\n[🏓](https://telegra.ph/file/a064672a214fca3be84ca.jpg) `PONG!!`\n⚡ `{time_taken_s:.3f} ms`")
