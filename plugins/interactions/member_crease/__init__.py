from pathlib import Path

from nonebot import on_notice
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageSegment,
    GroupIncreaseNoticeEvent,
    GroupDecreaseNoticeEvent,
)

import lang.member_crease as lang
from util.Config import config


def is_group_increase(event: GroupIncreaseNoticeEvent) -> bool:
    return True


def is_group_decrease(event: GroupDecreaseNoticeEvent) -> bool:
    return True


groupIncrease = on_notice(rule=is_group_increase)
groupDecrease = on_notice(rule=is_group_decrease)


@groupIncrease.handle()
async def _(bot: Bot, event: GroupIncreaseNoticeEvent) -> None:
    qq: str = event.get_user_id()
    user_info: dict[str, any] = await bot.get_stranger_info(
        user_id=int(qq), no_cache=False
    )
    if user_info:
        user_name: str = user_info["nickname"]
    else:
        user_name: str = "新人"
    if event.group_id in config.spec_groups:
        text: str = lang.INCREASE_MSG_SPEC
    else:
        text: str = lang.INCREASE_MSG
    formatted_msg: str = str.format(text, user_name, qq)
    msg: tuple[MessageSegment, Path] = (
        MessageSegment.text(formatted_msg),
        lang.INCREASE_PIC_PATH,
    )
    await groupIncrease.send(msg)


@groupDecrease.handle()
async def _(bot: Bot, event: GroupDecreaseNoticeEvent) -> None:
    qq: str = event.get_user_id()
    user_info: dict[str, any] = await bot.get_stranger_info(
        user_id=int(qq), no_cache=False
    )
    if user_info:
        user_name: str = user_info["nickname"]
    else:
        user_name: str = "群友"
    if event.group_id in config.spec_groups:
        text: str = lang.DECREASE_MSG_SPEC
    else:
        text: str = lang.DECREASE_MSG
    formatted_msg: str = str.format(text, user_name, qq)
    msg: tuple[MessageSegment, Path] = (
        MessageSegment.text(formatted_msg),
        lang.DECREASE_PIC_PATH,
    )
    await groupDecrease.send(msg)
