from pathlib import Path
from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.internal.matcher import Matcher

import lang.poke as lang
from util.message import rand_message

poke: Type[Matcher] = on_regex(lang.PATTERN)


@poke.handle()
async def _() -> None:
    text, ran_number = rand_message(lang.RESULTS, lang.RESULT_WEIGHTS)
    filename: str = str(ran_number).zfill(2) + ".png"
    file_path: Path = lang.RESULT_PIC_ROOT_PATH / filename
    msg: tuple[MessageSegment, MessageSegment] = (
        MessageSegment.text(text),
        MessageSegment.image(file_path),
    )
    await poke.finish(msg)
