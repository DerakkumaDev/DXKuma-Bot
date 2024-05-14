from typing import Type

from nonebot import on_regex
from nonebot.adapters.onebot.v11 import Bot, MessageSegment
from nonebot.internal.matcher import Matcher

import lang.fan_rank as lang
from util.rand_pic.data import get_time, gen_rank

rank: Type[Matcher] = on_regex(lang.PATTERN)


@rank.handle()
async def _(bot: Bot) -> None:
    time: str = get_time()
    leaderboard_output: list[str] = []
    leaderboard: list[tuple[any, any]] = await gen_rank(time)
    count: int = min(len(leaderboard), 5)
    for i, (qq, total_count) in enumerate(leaderboard[:count], start=1):
        user_info: dict[str, any] = await bot.get_stranger_info(
            user_id=int(qq), no_cache=False
        )
        rank_str: str = f"{i}. {user_info['nickname']} - {total_count}"
        leaderboard_output.append(rank_str)
    ranks: str = "\n".join(leaderboard_output)
    formatted_msg: str = str.format(lang.RESULT, ranks, count)
    msg: MessageSegment = MessageSegment.text(formatted_msg)
    await rank.finish(msg)
