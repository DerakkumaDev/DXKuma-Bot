from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.internal.matcher import Matcher

import lang.help as lang

all_help: Type[Matcher] = on_regex(lang.PATTERN)


@all_help.handle()
async def _() -> None:
    msg: MessageSegment = MessageSegment.image(lang.CMD_PIC_PATH)
    await all_help.send(msg)
