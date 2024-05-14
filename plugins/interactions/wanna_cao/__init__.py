import random
from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.internal.matcher import Matcher

import lang.wanna_cao as lang

xc: Type[Matcher] = on_regex(lang.RULE)


@xc.handle()
async def _() -> None:
    ran_number: list[int] = random.choices(
        range(1, len(lang.RESULTS) + 1), weights=lang.RESULT_WEIGHTS, k=1
    )
    text: str = lang.RESULTS[ran_number[0]]
    msg: MessageSegment = MessageSegment.text(text)
    await xc.send(msg)
