from pathlib import Path

from util.Path import KUMA_PIC_ROOT_PATH

PATTERN: str = r"^(戳屁)(屁|股)$"
RESULTS: dict[int, str] = {
    1: "不可以戳迪拉熊的屁股啦~",
    2: "你怎么能戳迪拉熊的屁股！",
    3: "为什么要戳迪拉熊的屁股呢？",
    4: "再戳我屁股迪拉熊就不跟你玩了！",
    5: "你再戳一个试试！",
    6: "讨厌啦~不要戳迪拉熊的屁股啦~",
    7: "你觉得戳迪拉熊的屁股很好玩吗？",
    8: "不许戳迪拉熊的屁股啦！",
    9: "迪拉熊懂你的意思~",
    10: "再戳迪拉熊就跟你绝交！",
}
RESULT_WEIGHTS: list[int | float] = [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5]
RESULT_PIC_ROOT_PATH: Path = KUMA_PIC_ROOT_PATH / "poke"
