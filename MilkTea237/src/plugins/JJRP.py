import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import datetime as datetime
from nonebot.adapters.onebot.v11.message import Message
import requests

jrrp = on_command("今日人品", aliases={".jrrp", "jrrp"})
def getapi():
    return "https://api.oick.cn/random/api.php"

@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    today = datetime.date.today()
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1, 100)
    picnum = str(random.random())
    url = requests.get("https://t.alcy.cc/pc/",timeout=3).content
    with open('jrrppic.png','wb') as op:
        op.write(url)
        op.close()
    msg = f"\n[CQ:image,file=file:///C:\\Users\\Administrator\\Desktop\\MilkTea237/jrrppic.png]\n"
    msg2 = f'[CQ:at,qq={event.get_user_id()}]\n今日({today})的人品为：<{lucknum}！>'
    msg3 = f'Pic_seed：{picnum}'
    out = msg2 + msg + msg3
    await jrrp.finish(Message(f'{out}'))
