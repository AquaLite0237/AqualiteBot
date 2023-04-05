import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import datetime as datetime
from nonebot.adapters.onebot.v11.message import Message

jrrp = on_command("今日人品", aliases={".jrrp", "jrrp"})


@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    today = datetime.date.today()
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1, 100)
    picnum = str(random.random())
    msg = "[CQ:image,file=https://api.vvhan.com/api/acgimg?" + picnum + "]"
    msg2 = f'[CQ:at,qq={event.get_user_id()}]\n今日({today})的人品为：<{lucknum}！>'
    msg3 = f'Pic_seed：{picnum}'
    out = msg2 + msg + msg3
    await jrrp.finish(Message(f'{out}'))
