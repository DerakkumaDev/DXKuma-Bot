from typing import Type

from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot.internal.matcher import Matcher
from nonebot.rule import to_me

import lang.love_you as lang

wxhn: Type[Matcher] = on_fullmatch(lang.PATTERN, rule=to_me())


@wxhn.handle()
async def _(event: GroupMessageEvent) -> None:
    msg: tuple[MessageSegment, MessageSegment] = (
        MessageSegment.reply(event.message_id),
        MessageSegment.text(lang.REPLY_MSG),
    )
    await wxhn.send(msg)
