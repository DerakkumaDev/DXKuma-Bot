from pathlib import Path

from util.Path import KUMA_PIC_ROOT_PATH, RESOURCE_ROOT_PATH

PATTERN: str = r"^((随机)(迪拉|滴蜡)熊|dlx)(涩图|色图|瑟图|st|)$"
PIC_ROOT_PATH: Path = KUMA_PIC_ROOT_PATH / "normal"
NSFW_PIC_ROOT_PATH: Path = KUMA_PIC_ROOT_PATH / "r18"
NOT_ALLOWED_MSG: str = "迪拉熊不准你看"
NOT_ALLOWED_PIC_PATH: Path = RESOURCE_ROOT_PATH / "notplay.png"
SKIP_MSG: str = "迪拉熊怕你沉溺其中，所以图就不发了~"
SKIP_NSFW_MSG: str = "迪拉熊关心你的身体健康，所以图就不发了~"
