import pickle
from nonebot.plugin import on_command,on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
import os
import datetime as datetime


ocmd = on_command('/ncrv')

@ocmd.handle()
async def ncrv(bot: Bot, event: GroupMessageEvent):
    user:str = event.get_user_id()
    msg = str(event.get_message()).replace('/ncrv','',1)
    if user != '1259891410':
        await ocmd.finish(Message('[ERROR]您无权使用ncrv命令 请联系开发者1259891410'))
    pouser = ''
    for m in msg:
        if m == '#':
            break
        pouser += m
    nc_path = f'MilkTea237\\data\\Aqualite\\奶茶总数\\{pouser}.txt'
    msg = msg.replace(pouser,'',1).replace('#','',1)
    with open(nc_path,'w') as wt:
        wt.write(msg)
        wt.close()
    await ocmd.finish(Message(f'{pouser}->{msg}\n修改完成ovo'))
    