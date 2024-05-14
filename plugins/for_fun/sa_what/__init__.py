import os
import random
from pathlib import Path
from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot.internal.matcher import Matcher

import lang.sa_what as lang

sa_what: Type[Matcher] = on_regex(lang.PATTERN)


@sa_what.handle()
async def _(event: GroupMessageEvent) -> None:
    files: list[str] = os.listdir(lang.PIC_ROOT_PATH)
    file: str = random.choice(files)
    name, price = file.split("-")
    price: str = price.replace(".jpeg", "")
    pic_path: str = os.path.join(lang.PIC_ROOT_PATH, file)
    formatted_msg = str.format(lang.RESULT_MSG, name, price)
    msg: tuple[MessageSegment, MessageSegment, MessageSegment, MessageSegment] = (
        MessageSegment.reply(event.message_id),
        MessageSegment.text(formatted_msg),
        MessageSegment.image(Path(pic_path)),
        MessageSegment.text(lang.TIP_MSG),
    )
    await sa_what.finish(msg)
