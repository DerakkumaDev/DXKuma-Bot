import random
from pathlib import Path
from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.internal.matcher import Matcher

import lang.poke as lang

poke: Type[Matcher] = on_regex(lang.RULE)


@poke.handle()
async def _() -> None:
    ran_number: list[int] = random.choices(
        range(1, len(lang.RESULTS) + 1), weights=lang.RESULT_WEIGHTS, k=1
    )
    text: str = lang.RESULTS[ran_number[0]]
    filename: str = str(ran_number).zfill(2) + ".png"
    file_path: Path = lang.RESULT_PIC_ROOT_PATH / filename
    msg: tuple[MessageSegment, MessageSegment] = (
        MessageSegment.text(text),
        MessageSegment.image(file_path),
    )
    await poke.finish(msg)
