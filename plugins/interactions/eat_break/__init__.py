from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot.internal.matcher import Matcher

import lang.eat_break as lang

eat_break: Type[Matcher] = on_regex(lang.PATTERN)


@eat_break.handle()
async def _(event: GroupMessageEvent) -> None:
    msg: tuple[MessageSegment, MessageSegment, MessageSegment] = (
        MessageSegment.reply(event.message_id),
        MessageSegment.text(lang.REPLY_MSG),
        MessageSegment.image(lang.REPLY_PIC_PATH),
    )
    await eat_break.send(msg)
