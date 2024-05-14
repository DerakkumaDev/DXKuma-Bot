from pathlib import Path

from util.Path import RESOURCE_ROOT_PATH

RULE: str = r"^(绝赞(给|请)你吃|(给|请)你吃绝赞)$"
REPLY_MSG: str = "谢谢~"
REPLY_PIC_PATH: Path = RESOURCE_ROOT_PATH / "eatbreak.png"
