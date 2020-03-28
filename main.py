#! /usr/bin/env python3

import asyncio
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

from nio import (
    Api,
    AsyncClient,
    RoomMessageText,
    InviteEvent
)

from config import Config
cfg = Config()

client = AsyncClient(cfg.get('homeserver'), cfg.get('userid'))

async def callback_room_message_text(room, event):
    logger.info("Message received for room {} | {}: {}".format(
            room.display_name, room.user_name(event.sender), event.body
        ))
    
    # so apparently this API isn't implemented yet in the async client :(
    r = Api.room_read_markers(client.access_token, room.room_id, event.event_id, event.event_id)
    await client.send(*r)
    # but this works!

    ## Plug in game modules here
    if room.is_group:
        # ad-hoc, direct chat
        pass
    else:
        # group chat
        pass


async def callback_room_invite(source, sender):
    print(source)
    print(sender)
    await client.join(source.room_id)

async def main():

    await client.login(cfg.get('password'))

    if client.logged_in is False:
        raise Exception("Login failed.")

    ## Do more stuff here
    client.add_event_callback(callback_room_message_text, RoomMessageText)
    client.add_event_callback(callback_room_invite, InviteEvent)

    await client.sync_forever(timeout=30000)


asyncio.get_event_loop().run_until_complete(main())




