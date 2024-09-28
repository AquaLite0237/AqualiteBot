import os
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.typing import T_State
import random

randchoice = on_keyword({'/帮我选择'})

@randchoice.handle()
async def _(bot: Bot, event: Event):
    getmsg_ = str(event.get_message())
    getmsg = getmsg_.replace('/帮我选择', '', 1) + '或'
    choilist = []
    msgpp = ''
    for a in list(getmsg):
        if a == '或':
            choilist.append(msgpp)
            msgpp = ''
        else:
            msgpp += a
    get_rand = random.choice(choilist)
    replylist = [f'嘛..咱觉得还是选择\n{get_rand}吧！',f'如果让我在{choilist}里面选择的话，我会选{get_rand}哦！',f'那我就随便选咯？就是你了！{get_rand}']
    await randchoice.finish(Message(f'{random.choice(replylist)}'))