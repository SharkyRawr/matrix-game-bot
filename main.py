#! /usr/bin/env python3

import asyncio
import logging
logger = logging.getLogger(__name__)

from nio import (
    AsyncClient,
    RoomMessageText,
)

from config import Config
cfg = Config()

def callback_room_message_text(room, event):
    logger.info("Message received for room {} | {}: {}".format(
            room.display_name, room.user_name(event.sender), event.body
        ))

    ## Plug in game modules here
    if room.is_group:
        # ad-hoc, direct chat
        pass
    else:
        # group chat
        pass


async def main():
    client = AsyncClient(cfg.get('homeserver'), cfg.get('userid'))

    await client.login('somepass')

    if client.logged_in is False:
        raise Exception("Login failed.")

    ## Do more stuff here
    client.add_event_callback(callback_room_message_text, RoomMessageText)

    await client.sync_forever(timeout=30000)


asyncio.get_event_loop().run_until_complete(main())




