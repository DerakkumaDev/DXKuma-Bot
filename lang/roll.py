from pathlib import Path

from util.Path import RESOURCE_ROOT_PATH

RULE: str = r"^(?:是)(.+)(?:还是(.+))+$"
NO_OPTION_MSG: str = "没有选项要让迪拉熊怎么选嘛~"
ONLY_ONE_MSG: str = "就一个选项要让迪拉熊怎么选嘛~"
RESULT_MSG: str = "迪拉熊建议你选择“{}”呢~"
CAN_NOT_PIC_PATH: Path = RESOURCE_ROOT_PATH / "选不了.png"
SELECTED_PIC_PATH: Path = RESOURCE_ROOT_PATH / "选择.png"
