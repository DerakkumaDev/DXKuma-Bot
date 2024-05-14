import os
import shutil
import tomllib
from typing import List


class Config:
    def __init__(self) -> None:
        if not os.path.exists("./config.toml"):
            shutil.copyfile("./static/config_example.toml", "./config.toml")
        # info
        self.admin: List[int] | None = None
        self.dev_token: str | None = None
        # log
        self.log_level: str | None = None
        # backend
        self.is_lagrange: bool | None = None
        # nonebot
        self.listen_host: str | None = None
        self.listen_port: int | None = None
        self.token: str | None = None

        self.spec_groups: List[int] | None = None

        # 解析配置文件
        self.read_config()

    def read_config(self) -> None:
        with open("./config.toml", "rb") as f:
            data: dict[str, any] = tomllib.load(f)
            f.close()
        self.admin: List[int] | None = data["info"]["admin"]
        self.dev_token: str | None = data["info"]["dev_token"]
        self.log_level: str | None = data["log"]["log_level"]
        self.is_lagrange: bool | None = data["backend"]["is_lagrange"]
        self.listen_host: str | None = data["nonebot"]["listen_host"]
        self.listen_port: int | None = data["nonebot"]["listen_port"]
        self.token: str | None = data["nonebot"]["token"]
        self.spec_groups: List[int] | None = data["groups"]["spec"]


config: Config = Config()
