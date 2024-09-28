from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import datetime as datetime
from nonebot.typing import T_State

sign = on_command("我的奶茶", aliases={"!mm", "mm"})
@sign.handle()
async def sign_handle(bot: Bot, event: Event, state: T_State):
    id = event.get_user_id()
    today = datetime.date.today()
    user_qq = int(event.get_user_id())
    nc_path = f'MilkTea237\\data\\Aqualite\\奶茶总数'
    nc_paths = f'{nc_path}\\{user_qq}.txt'
    ncs = open(nc_paths,'r',encoding='utf-8')
    ncms = ncs.readline()
    return1 = f"[CQ:at,qq={id}]"
    return2 = f'\n已经有了{ncms}杯奶茶喵！\n{today}'
    returnnn = return1 + return2
    await sign.finish(Message(f'{returnnn}'))