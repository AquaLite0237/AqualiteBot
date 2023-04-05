from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_command
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event
import pickle
import os

catch_str = on_command("/help", aliases={"菜单","help"})
sethelp = on_keyword({"/set_help"})
msg_path = 'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\sethelp'
msg_paths = f'{msg_path}\\helpmsg.pkl'


@catch_str.handle()
async def send_msg(bot: Bot, event: Event, state: T_State):
    id = event.get_user_id()
    msgf = open(msg_paths, "rb")
    msgdict = pickle.load(msgf)
    ncms = msgdict['msg']
    msg = "[CQ:at,qq={}]".format(id) + f'\n奶茶酱/Aqualite-bot帮助文档链接：https://note.youdao.com/s/TnWDjRH7\n\nGithub repository：https://github.com/MilkTeaqwq/AqualiteBot\nTips：{ncms}'
    await catch_str.finish(Message(f'{msg}'))

@sethelp.handle()
async def sendmsg(bot: Bot, event: Event, state: T_State):
    user = int(event.get_user_id())
    sethelp_ = str(event.get_message())
    sethelp = sethelp_.replace('/set_help', '', 1)
    if user != 1259891410:
        await sethelp.finish(Message(f'你无权使用SETHELP指令'))
    else:
        if not os.path.exists(msg_path):
            os.makedirs(msg_path)
        with open(msg_paths,'wb') as pl:
            dicttof = {}
            dicttof['msg'] = sethelp
            pickle.dump(dicttof,pl)
            pl.close
        await sethelp.finish(Message(f'已将HELP反馈文本中的<Tips>指向文本修改为{sethelp}'))
    