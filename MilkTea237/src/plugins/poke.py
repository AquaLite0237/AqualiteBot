import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import datetime as datetime
from nonebot.adapters.onebot.v11.message import Message
import nonebot
from nonebot.plugin.on import on_notice
from nonebot.adapters.onebot.v11 import MessageSegment
import json
import time


test = on_command("botvalue")


@test.handle()
async def jrrp_handle(bot: Bot, event: Event):
	await test.finish(Message(nonebot.get_bots()))

async def _group_poke(bot: Bot, event: Event) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
    return value


chat_notice = on_notice(rule=_group_poke, priority=10, block=True)


@chat_notice.handle()
async def handle_first_receive(bot: Bot, event: Event):
	if event.__getattribute__('group_id') is None:
		event.__delattr__('group_id')
	mode = random.randint(1,5)
	if mode == 1:
		await chat_notice.send(Message([
        MessageSegment("poke",  {
           "qq": f"{event.get_user_id}"
       })
    ]))
		await chat_notice.send(Message('我也戳！'))
		time.sleep(1)
		await chat_notice.send(Message([
        MessageSegment("poke",  {
           "qq": f"{event.get_user_id}"
       })
    ]))
		await chat_notice.finish(Message('UwU'))
	replydic = ["不要戳咱啦..","诶诶?被拍了咩","检测到未知钝状物体冲击..","笨蛋笨蛋笨蛋","生气一秒钟","再戳我就!","（熟睡中）zzzz...","不理你一秒钟","喵喵喵🐱","被戳晕一秒钟..",'ovo?','什么什么什么！','咱也会！']
	pokereply = random.choice(replydic)
	await chat_notice.send(Message([
        MessageSegment("poke",  {
           "qq": f"{event.get_user_id}"
       })
    ]))
	await chat_notice.finish(Message(pokereply))