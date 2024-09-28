from nonebot import on_message,on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import os
import time

run = on_command('runqsign')

@run.handle()
async def sign_handle(bot: Bot, event: Event):
    user_qq = int(event.get_user_id())
    await run.finish(Message("当前部署了qsign可用性自查服务，手动启动qsighserver暂不可用"))
    try:
        await run.finish((Message('QsignServer服务运行正常！')))
        return 1
    except:
        pass
    os.system('cd C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237 && start Start_Qsign.bat')
    time.sleep(8)
    await run.finish((Message('QsignServer服务运行正常！')))
