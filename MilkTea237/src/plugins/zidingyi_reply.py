from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import datetime as datetime
from nonebot.typing import T_State
import json
import random


reply = on_message(priority=100)
@reply.handle()
async def reply_handle(bot: Bot, event: Event):
    toutou = ['不行的啦！','只有这次哦..！','但是我拒绝','不要喵不要喵','唔姆..','边泰也']
    reply_dic = {
        '你好': 'nihao' ,
        '早上好'  : '早上好~' ,
        '晚安'    : '好梦哦！',
        '奶茶酱'    :'在哦！如果有需要请发送/help来看酱酱能帮到你什么！',
        '奶茶透透':random.choice(toutou)
    }
    user_msg = str(event.get_message()).strip()
    try:
        reply_msg = reply_dic[user_msg]
        await reply.finish(reply_msg)
    except KeyError:
        pass
