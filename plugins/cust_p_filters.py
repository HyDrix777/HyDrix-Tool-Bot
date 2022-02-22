from pyrogram import (
    filters
)
from plugins.admin_check import admin_check
import os





async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)
