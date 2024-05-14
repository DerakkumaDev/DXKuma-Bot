import asyncio
import os
import random
from pathlib import Path
from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.internal.matcher import Matcher

import lang.rand_pic as lang
from util.Config import config
from util.rand_pic.data import update_count, get_time

kuma_pic: Type[Matcher] = on_regex(lang.RULE)


@kuma_pic.handle()
async def _(bot: Bot, event: GroupMessageEvent) -> None:
    msg: str = event.raw_message
    # TODO: use regex replace contains
    if "涩图" in msg or "色图" in msg or "瑟图" in msg or "st" in msg:
        is_nsfw: bool = True
        path: Path = lang.NSFW_PIC_ROOT_PATH
    else:
        is_nsfw: bool = False
        path: Path = lang.PIC_ROOT_PATH

    weight: int = random.randint(1, 100)
    if is_nsfw and event.group_id not in config.spec_groups:
        msg: tuple[MessageSegment, MessageSegment] = (
            MessageSegment.text(lang.NOT_ALLOWED_MSG),
            MessageSegment.image(lang.NOT_ALLOWED_PIC_PATH),
        )
        await kuma_pic.send(msg)
    elif weight <= 10:
        if is_nsfw:
            msg: MessageSegment = MessageSegment.text(lang.SKIP_NSFW_MSG)
        else:
            msg: MessageSegment = MessageSegment.text(lang.SKIP_MSG)
        await kuma_pic.send(msg)
    else:
        time = get_time()
        files: list[str] = os.listdir(path)
        file: str = random.choice(files)
        pic_path: str = os.path.join(path, file)
        await update_count(
            time=time,
            qq=event.get_user_id(),
            type_name="kuma-r18" if is_nsfw else "kuma",
        )
        msg: MessageSegment = MessageSegment.image(Path(pic_path))
        send_msg: dict[str, any] = await kuma_pic.send(msg)
        if is_nsfw:
            await asyncio.sleep(10)
            msg_id: int = send_msg["message_id"]
            await bot.delete_msg(message_id=msg_id)
