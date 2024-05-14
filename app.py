import nonebot
from nonebot.adapters.onebot import V11Adapter as Adapter

from util.Path import PLUGIN_ROOT_PATH


def nonebot_init() -> None:
    # 初始化 NoneBot
    nonebot.init()

    # 注册适配器
    driver = nonebot.get_driver()
    driver.register_adapter(Adapter)

    # 在这里加载插件
    nonebot.load_plugins(str(PLUGIN_ROOT_PATH / "for_fun"))
    nonebot.load_plugins(str(PLUGIN_ROOT_PATH / "interactions"))
    # nonebot.load_plugins(str(PLUGIN_ROOT_PATH / "maimai"))
    nonebot.load_plugins("plugins_old/bot")
    nonebot.load_plugins("plugins_old/maimai")
    nonebot.load_plugins(str(PLUGIN_ROOT_PATH / "managements"))

    nonebot.run()
