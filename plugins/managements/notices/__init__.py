from typing import Type

from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.internal.matcher import Matcher
from nonebot.rule import to_me

import lang.notices as lang

zysx: Type[Matcher] = on_fullmatch(lang.PATTERN, rule=to_me())


@zysx.handle()
async def _() -> None:
    msg: tuple[MessageSegment, MessageSegment] = (
        MessageSegment.text(lang.NOTICES_MSG),
        MessageSegment.image(lang.NOTICES_PIC_PATH),
    )
    await zysx.send(msg)
