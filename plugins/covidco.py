
from covid import Covid

from . import *


@Client.on_message(filters.command("covid"))
async def covid(bot, message):
    covid = Covid()
    text = message.text
    okie = text.split(" ", maxsplit=1)
    try:
        country = okie[1]
    except IndexError:
        await eor(message, "Give a country name to Search for it's Covid Cases!")
        return
    try:
        cases = covid.get_status_by_country_name((country).lower())
        act = cases["active"]
        conf = cases["confirmed"]
        dec = cases["deaths"]
        rec = cases["recovered"]
        await eor(
            event,
            f"**Country:** **{country.capitalize()}**\n**Active:** {act}\n**Confirmed:** {conf}\n**Recovered:** {rec}\n**Deceased:** {dec}",
        )
    except ValueError:
        await eor(message, f"It seems that Country {country} is invalid!")
        
CMD_HELP.update(
    {
        "": """**Plugin : **`Covid`
        
**Commands in animation4 are **
 
✘ Commands Available
• `.covid country name`
    Gets the Covid-19 Status of a given Country.


  
**Function : **__shows covid information .__"""
    }
)
