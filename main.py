#! /usr/bin/env python3

import asyncio
import logging
logger = logging.getLogger(__name__)

from nio import (
    AsyncClient,
    RoomMessageText
)

def callback_room_message_text(room, event):
    logger.info("Message received for room {} | {}: {}".format(
            room.display_name, room.user_name(event.sender), event.body
        ))

async def main():
    client = AsyncClient('https://shark.pm', '@gamebot:shark.pm')

    await client.login('somepass')

    if client.logged_in is False:
        raise Exception("Login failed.")

    ## Do more stuff here
    client.add_event_callback(callback_room_message_text, RoomMessageText)

    await client.sync_forever(timeout=30000)


asyncio.get_event_loop().run_until_complete(main())




