import datetime
import json
from datetime import date
from pathlib import Path

from util.Path import DATA_DIR_PATH

DATABASE_PATH: Path = DATA_DIR_PATH / "random_pic" / "count.json"


def get_time() -> str:
    today: date = datetime.date.today()
    year: int = today.year
    week_number: int = today.isocalendar()[1]
    result: str = str(year) + str(week_number)
    return result


async def update_count(time, qq: str, type_name: str) -> None:
    with open(DATABASE_PATH, "r") as f:
        count_data: dict = json.load(f)
    if qq not in count_data or time not in count_data:
        count_data.setdefault(qq, {})
        count_data[qq].setdefault(time, {"kuma": 0, "kuma_r18": 0})
    count_data[qq][time][type_name] += 1
    with open(DATABASE_PATH, "w") as f:
        json.dump(count_data, f, ensure_ascii=False, indent=4)


async def gen_rank(time: str) -> list[tuple[any, any]]:
    with open(DATABASE_PATH, "r") as f:
        count_data: dict = json.load(f)
    leaderboard: list[tuple[any, any]] = []
    for qq, qq_data in count_data.items():
        if time in qq_data:
            total_count = qq_data[time]["kuma"] + qq_data[time]["kuma_r18"]
            leaderboard.append((qq, total_count))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    return leaderboard[:5]
