from pathlib import Path

from util.Path import RESOURCE_ROOT_PATH

RULE: str = "注意事项"
NOTICES_MSG: str = (
    "注意事项\n"
    "❶本bot为娱乐性质bot，不支持更新查分器，小黑屋等科技功能\n"
    "❷发送dlxhelp查看指令大全\n"
    "❸号主随时会顶号与大家聊天解惑，介意勿用（不影响bot使用）\n"
    "❹大多数指令不需要@bot，直接输入指令即可（dlxhelp会标注需要@的功能）\n"
    "❺想让自己的群拥有bot可以直接加好友，同意之后就可以拉了\n"
    "❻QQ空间可查看bot的更新日志\n"
    "❼如不需要迪拉熊了，请直接私聊bot说明，不要直接踢\n"
    "❽有任何建议或者bug反馈，可加入bot测试群：959231211\n"
    "希望大家用的开心~"
)
NOTICES_PIC_PATH: Path = RESOURCE_ROOT_PATH / "zysx.jpg"
