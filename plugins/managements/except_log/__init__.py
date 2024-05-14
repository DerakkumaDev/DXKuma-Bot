import traceback
from typing import Optional

from nonebot import get_bot, Bot
from nonebot.adapters.onebot.v11 import Event, ActionFailed, MessageSegment
from nonebot.internal.matcher import Matcher
from nonebot.message import run_postprocessor

import lang.except_log as lang


@run_postprocessor
async def _(event: Event, matcher: Matcher, exception: Optional[Exception]) -> None:
    if not exception or (
        isinstance(exception, ActionFailed) and exception.info["retcode"] is 200
    ):
        return
    bot: Bot = get_bot()
    trace: list[str] = traceback.format_exception(exception)
    formatted_trace: str = "".join(trace).replace("\\n", "\n")
    msg: MessageSegment = MessageSegment.text(f"{formatted_trace}{event.raw_message}")
    await bot.send_msg(group_id=236030263, message=msg)
    feedback: tuple[MessageSegment, MessageSegment] = (
        MessageSegment.reply(event.message_id),
        MessageSegment.text(lang.FEEDBACK_MSG),
    )
    await matcher.send(feedback)
