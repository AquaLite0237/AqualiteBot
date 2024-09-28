from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event
import os
import random


picpath = 'MilkTea237\\data\\Aqualite\\longtu'
nmsl = on_command("龙图")

@nmsl.handle()
async def send_msgs(bot: Bot, event: Event, state: T_State):
    piclist = os.listdir(picpath)
    img = f"[CQ:image,file=MilkTea237/data/Aqualite/longtu/{random.choice(piclist)}]"
    await nmsl.finish(Message(img))