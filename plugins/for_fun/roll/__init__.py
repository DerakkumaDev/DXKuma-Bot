from random import SystemRandom as Random
from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot.internal.matcher import Matcher

import lang.roll as lang

roll: Type[Matcher] = on_regex(lang.PATTERN)


@roll.handle()
async def _(event: GroupMessageEvent) -> None:
    # TODO: use regex replace split
    roll_list: list[str] = event.raw_message[1:].split("还是")
    if not roll_list:
        msg: tuple[MessageSegment, MessageSegment, MessageSegment] = (
            MessageSegment.reply(event.message_id),
            MessageSegment.text(lang.NO_OPTION_MSG),
            MessageSegment.image(lang.CAN_NOT_PIC_PATH),
        )
    elif len(set(roll_list)) <= 1:
        msg: tuple[MessageSegment, MessageSegment, MessageSegment] = (
            MessageSegment.reply(event.message_id),
            MessageSegment.text(lang.ONLY_ONE_MSG),
            MessageSegment.image(lang.CAN_NOT_PIC_PATH),
        )
    else:
        output: str = Random().choice(roll_list)
        formatted_msg: str = str.format(lang.RESULT_MSG, output)
        msg: tuple[MessageSegment, MessageSegment, MessageSegment] = (
            MessageSegment.reply(event.message_id),
            MessageSegment.text(formatted_msg),
            MessageSegment.image(lang.SELECTED_PIC_PATH),
        )
    await roll.send(msg)
