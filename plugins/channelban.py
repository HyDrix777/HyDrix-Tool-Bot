from pyrogram import Client, idle
from pyrogram.raw.types import UpdateGroupCallParticipants, PeerChannel
from pyrogram.raw.functions.channels import EditBanned
from pyrogram.raw.types import InputPeerChannel, InputChannel, ChatBannedRights, InputGroupCall
from pyrogram.raw.functions.phone import EditGroupCallParticipant, GetGroupParticipants



@Client.on_raw_update()
async def hemheupdet(client, update, users, chats):
    banchat = await client.resolve_peer("Tg_Galaxy")
    if isinstance(update, UpdateGroupCallParticipants):
        for x in update.participants:
            if isinstance(x.peer, PeerChannel):
                    await client.send(EditGroupCallParticipant(call=update.call, participant=x.peer (int(str(-100) + str(x.peer.channel_id))), muted=True))
                    await client.kick_chat_member("DecodeSupport", x.peer.channel_id)
                    await client.send_message(chat, f"Successfully Banned str(x.peer.channel_id)")
                    await client.send_message(chat, f"{e} \n\n{x.peer}")
