import re
from typing import Type

from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.internal.matcher import Matcher

from . import config

repeater_group: list[str] = config.repeater_group
shortest: int = config.shortest_length
blacklist: list[str] = config.blacklist

m: Type[Matcher] = on_message()

last_message: dict[str, str] = {}
message_times: dict[str, int] = {}


# 消息预处理
def message_preprocess(message: str) -> tuple[str, str]:
    raw_message: str = message
    contained_images: dict[str, list[str]] = {}
    images: list[str] = re.findall(r"\[CQ:image.*?]", message)
    pattern: str = r"file=http://gchat.qpic.cn/gchatpic_new/\d+/\d+-\d+-(.*?)/.*?[,\]]"
    for i in images:
        image_url: list[str] = re.findall(r"url=(.*?)[,\]]", i)
        pattern_match: list[str] = re.findall(pattern, i)
        if image_url and pattern_match:
            contained_images.update({i: [image_url[0], pattern_match[0]]})
    for i, v in contained_images.items():
        message: str = message.replace(i, f"[{v[1]}]")
    return message, raw_message


@m.handle()
async def repeater(bot: Bot, event: GroupMessageEvent) -> None:
    if event.raw_message in blacklist:
        return
    gid: str = str(event.group_id)
    if gid in repeater_group or "all" in repeater_group:
        global last_message, message_times
        message, raw_message = message_preprocess(str(event.message))
        if last_message.get(gid) != message:
            message_times[gid] = 1
        else:
            message_times[gid] += 1
        if message_times.get(gid) == config.shortest_times:
            await bot.send_group_msg(
                group_id=event.group_id, message=raw_message, auto_escape=False
            )
        last_message[gid] = message
