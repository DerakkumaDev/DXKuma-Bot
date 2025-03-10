import json
import os
from asyncio import Lock
from datetime import date
from os import path

from aiohttp import ClientError, ClientSession

music_data_lock = Lock()
chart_stats_lock = Lock()
alias_list_lxns_lock = Lock()
alias_list_ycn_lock = Lock()


async def get_music_data():
    cache_dir = "./Cache/Data/MusicData/"
    cache_path = f"{cache_dir}{date.today().isoformat()}.json"
    async with music_data_lock:
        if not path.exists(cache_path):
            files = os.listdir(cache_dir)
            async with ClientSession(conn_timeout=3) as session:
                try:
                    async with session.get(
                        "https://www.diving-fish.com/api/maimaidxprober/music_data"
                    ) as resp:
                        with open(cache_path, "wb") as fd:
                            async for chunk in resp.content.iter_chunked(1024):
                                fd.write(chunk)
                except ClientError:
                    if files:
                        with open(f"{cache_dir}{files[-1]}") as fd:
                            return json.loads(fd.read())
                    return list()
            if files:
                for file in files:
                    os.remove(f"{cache_dir}{file}")
    with open(cache_path) as fd:
        return json.loads(fd.read())


async def get_chart_stats():
    cache_dir = "./Cache/Data/ChartStats/"
    cache_path = f"{cache_dir}{date.today().isoformat()}.json"
    async with chart_stats_lock:
        if not path.exists(cache_path):
            files = os.listdir(cache_dir)
            async with ClientSession(conn_timeout=3) as session:
                try:
                    async with session.get(
                        "https://www.diving-fish.com/api/maimaidxprober/chart_stats"
                    ) as resp:
                        with open(cache_path, "wb") as fd:
                            async for chunk in resp.content.iter_chunked(1024):
                                fd.write(chunk)
                except ClientError:
                    if files:
                        with open(f"{cache_dir}{files[-1]}") as fd:
                            return json.loads(fd.read())
                    return {"charts": dict(), "diff_data": dict()}
            if files:
                for file in files:
                    os.remove(f"{cache_dir}{file}")
    with open(cache_path) as fd:
        return json.loads(fd.read())


async def get_alias_list_lxns():
    cache_dir = "./Cache/Data/Alias/Lxns/"
    cache_path = f"{cache_dir}{date.today().isoformat()}.json"
    async with alias_list_lxns_lock:
        if not os.path.exists(cache_path):
            files = os.listdir(cache_dir)
            async with ClientSession(conn_timeout=3) as session:
                try:
                    async with session.get(
                        "https://maimai.lxns.net/api/v0/maimai/alias/list"
                    ) as resp:
                        with open(cache_path, "wb") as fd:
                            async for chunk in resp.content.iter_chunked(1024):
                                fd.write(chunk)
                except ClientError:
                    if files:
                        with open(f"{cache_dir}{files[-1]}") as fd:
                            return json.loads(fd.read())
                    return {"aliases": list()}
            if files:
                for file in files:
                    os.remove(f"{cache_dir}{file}")
    with open(cache_path) as fd:
        return json.loads(fd.read())


async def get_alias_list_ycn():
    cache_dir = "./Cache/Data/Alias/YuzuChaN/"
    cache_path = f"{cache_dir}{date.today().isoformat()}.json"
    async with alias_list_ycn_lock:
        if not os.path.exists(cache_path):
            files = os.listdir(cache_dir)
            async with ClientSession(conn_timeout=3) as session:
                try:
                    async with session.get(
                        "https://api.yuzuchan.moe/maimaidx/maimaidxalias"
                    ) as resp:
                        with open(cache_path, "wb") as fd:
                            async for chunk in resp.content.iter_chunked(1024):
                                fd.write(chunk)
                except ClientError:
                    if files:
                        with open(f"{cache_dir}{files[-1]}") as fd:
                            return json.loads(fd.read())
                    return {"status_code": 504, "content": list()}
            if files:
                for file in files:
                    os.remove(f"{cache_dir}{file}")
    with open(cache_path) as fd:
        return json.loads(fd.read())


async def get_alias_list_xray():
    cache_dir = "./Cache/Data/Alias/Xray/"
    cache_path = f"{cache_dir}{date.today().isoformat()}.json"
    async with alias_list_ycn_lock:
        if not os.path.exists(cache_path):
            files = os.listdir(cache_dir)
            async with ClientSession(conn_timeout=3) as session:
                try:
                    async with session.get(
                        "https://download.xraybot.site/maimai/alias.json"
                    ) as resp:
                        with open(cache_path, "wb") as fd:
                            async for chunk in resp.content.iter_chunked(1024):
                                fd.write(chunk)
                except ClientError:
                    if files:
                        with open(f"{cache_dir}{files[-1]}") as fd:
                            return json.loads(fd.read())
                    return dict()
            if files:
                for file in files:
                    os.remove(f"{cache_dir}{file}")
    with open(cache_path) as fd:
        return json.loads(fd.read())
