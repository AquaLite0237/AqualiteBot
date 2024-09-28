import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import datetime as datetime
from nonebot.adapters.onebot.v11.message import Message
import requests

dfsj = on_command("东方随机图", aliases={"看东方", "东批"})


@dfsj.handle()
async def jrrp_handle(bot: Bot, event: Event):
    url = requests.get('https://img.paulzzh.tech/touhou/random').content
    with open('dongpipic.png','wb') as op:
        op.write(url)
        op.close()
    msg = f"[CQ:image,file=file:///C:\\Users\\Administrator\\Desktop\\MilkTea237\\dongpipic.png]"
    msg2 = '东方Project随机图'
    out = msg2 + msg
    await dfsj.finish(Message(f'{out}'))