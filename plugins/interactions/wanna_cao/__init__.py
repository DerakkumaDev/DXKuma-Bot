from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.internal.matcher import Matcher

import lang.wanna_cao as lang
from util.message import rand_message

xc: Type[Matcher] = on_regex(lang.PATTERN)


@xc.handle()
async def _() -> None:
    text = rand_message(lang.RESULTS, lang.RESULT_WEIGHTS)
    msg: MessageSegment = MessageSegment.text(text)
    await xc.send(msg)
