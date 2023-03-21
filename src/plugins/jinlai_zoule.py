from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.plugin.on import on_notice
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters.onebot.v11.event import GroupIncreaseNoticeEvent
from nonebot.adapters.onebot.v11.event import GroupDecreaseNoticeEvent
from nonebot.adapters.onebot.v11.message import Message
 
welcum_zoule=on_notice()
 
@welcum_zoule.handle()
async def welcome(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "欢迎！：[CQ:at,qq={}]".format(user)
    msg = at_ + '大佬进群！这里是Aqualite-bot，可以称呼我奶茶酱哦！如果想知道奶茶酱能做到什么的话请发送/help喔！'
    await welcum_zoule.finish(Message(f'{msg}'))
 
@welcum_zoule.handle()
async def gunchuqu(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    msg = "{}退出了群聊..可能是家里空调忘记关了，大家出门记得关空调哦！".format(user)
    await welcum_zoule.finish(Message(f'{msg}'))
 
 