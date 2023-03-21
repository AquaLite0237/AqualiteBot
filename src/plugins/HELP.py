from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event

catch_str = on_keyword({'/help','菜单','help'})


@catch_str.handle()
async def send_msg(bot: Bot, event: Event, state: T_State):
    id = event.get_user_id()
    msg = "[CQ:at,qq={}]".format(id) + '\n奶茶酱/Aqualite-bot帮助文档链接：https://note.youdao.com/s/TnWDjRH7\nGithub repository：https://github.com/MilkTeaqwq/AqualiteBot'

    await catch_str.finish(Message(f'{msg}'))
