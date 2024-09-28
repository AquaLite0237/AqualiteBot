from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_command
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event
import pickle
import os

forwardhelp = on_command("/fhelp", aliases={"f菜单","fhelp"})
catch_str = on_command("/help", aliases={"菜单","help"})
sethelp = on_keyword({"/set_help"})
extendhelp = on_keyword({"/extend_help"})

msg_path = 'MilkTea237\\data\\Aqualite\\sethelp'
msg_paths = f'{msg_path}\\helpmsg.pkl'
extendpath = 'MilkTea237\\data\\Aqualite\\hbnode'
extendpaths = 'MilkTea237\\data\\Aqualite\\hbnode\\hbmsglist.pkl'


@forwardhelp.handle()
async def send_msgs(bot: Bot, event: Event, state: T_State):
    id = event.get_user_id()
    msgf = open(extendpaths, "rb")
    send_end = pickle.load(msgf)
    await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
    await forwardhelp.finish()

@extendhelp.handle()
async def send_msgs(bot: Bot, event: Event, state: T_State):
    id = event.get_user_id()
    if int(id) != 1259891410:
        await extendhelp.finish(Message('你无权使用extendhelp命令集'))
    try:
        msgf = open(extendpaths, "rb")
        send_ena = pickle.load(msgf)
    except:
        pass
    send_end = []
    try:
        send_end.extend(send_ena)
    except:
        pass
    sethelp_ = str(event.get_message())
    msg = sethelp_.replace('/extend_help', '', 1)
    send_end.extend(
                    [
                        MessageSegment.node_custom(
                            user_id=2710022737,
                            nickname="奶茶酱-AqualiteBot",
                            content=Message(f"{msg}")
                        )
                    ]
                )
    await extendhelp.send(Message('extend to send_end'))
    await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
    if not os.path.exists(extendpath):
        os.makedirs(extendpath)
    with open(extendpaths,'wb') as pl:
        pickle.dump(send_end,pl)
        pl.close
    await extendhelp.finish(Message('wb'))


@catch_str.handle()
async def send_msg(bot: Bot, event: Event, state: T_State):
    id = event.get_user_id()
    msg = f"___(>^ω^<)___\n奶茶酱/Aqualite-bot帮助文档链接[想要查看奶茶酱可以做什么（指令汇总）都可以在上面的网站找到哦！]：\nhttps://note.youdao.com/s/TnWDjRH7\n\n相关信息：bot开发：奶茶sama/Aqualite[1259891410]（QQ）(请备注来意)\n群聊：奇异搞笑群聊＆[920410742]\n群偏向游戏 生活 弱智事物分享捏 欢迎大家加入！\n\ntip:若您看到的help样式是这样的文本样式则代表合并消息被风控了，一段时间后恢复ovo"
    await catch_str.finish(Message(f'{msg}'))


    

@sethelp.handle()
async def sendmsg(bot: Bot, event: Event, state: T_State):
    id = event.get_user_id()
    if int(id) != 1259891410:
        await extendhelp.finish(Message('你无权使用extendhelp命令集'))
    try:
        msgf = open(extendpaths, "rb")
        send_end = pickle.load(msgf)
    except:
        pass
    sethelp_ = str(event.get_message())
    msg = sethelp_.replace('/set_help', '', 1)
    listsy = ""
    for af in list(msg):
        if af == '#':
            break
        else:
            listsy += str(af)
    msg = msg.replace(listsy + '#', '', 1)
    send_end[int(listsy)] = MessageSegment.node_custom(
                            user_id=2710022737,
                            nickname="奶茶酱-AqualiteBot",
                            content=Message(msg)
                        )
    await sethelp.send(Message('send_end update'))
    await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
    if not os.path.exists(extendpath):
        os.makedirs(extendpath)
    with open(extendpaths,'wb') as pl:
        pickle.dump(send_end,pl)
        pl.close