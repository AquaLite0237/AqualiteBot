from nonebot.plugin import on_command,on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
import datetime as datetime
import random

piwo = on_command('劈我')

@piwo.handle()
async def pi(bot: Bot, event: GroupMessageEvent):
    if random.randint(1,3) == 1:
        await bot.set_group_ban(group_id=event.group_id,user_id=int(event.get_user_id()),duration=random.randint(1,300))
        await piwo.finish(Message('🌩'))
    await piwo.finish(Message(random.choice(['☁️','🌞'])))