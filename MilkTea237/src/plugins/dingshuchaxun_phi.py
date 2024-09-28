from nonebot.plugin import on_command
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import os
import random
import json
try:
    from nonebot.adapters.onebot.v11 import Message, MessageSegment  # type: ignore
except ImportError:
    from nonebot.adapters.cqhttp import Message, MessageSegment  # type: ignore

datepath_phi = 'C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/PhigrosData/Phigros.json'
datepath_tips = 'C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/PhigrosData/tips.json'
sec_phi = on_keyword({'/phi song'},priority=8)
mohu_sec = on_keyword({'/phi sec'},priority=7)
ran_tips = on_command('/phi tip')

@ran_tips.handle()
async def mhsc(bot: Bot, event: Event):
    date_phi_file = open(datepath_tips, 'rb')
    date_phi = json.load(date_phi_file)
    await ran_tips.finish(Message(f"{random.choice(date_phi['tips'])}"))


@sec_phi.handle()
async def mhsc(bot: Bot, event: Event):
    getmsg_ = str(event.get_message())
    user = event.get_user_id()
    getmsg = getmsg_.replace('/phi song', '', 1)
    date_phi_file = open(datepath_phi,'rb')
    date_phi = json.load(date_phi_file)
    try:
        head_dic = date_phi[getmsg]
    except KeyError:
        await sec_phi.finish(Message(f'呜呜..\n数据库中找不到<{getmsg}>曲目诶,请留意大小写或空格！'))
    msg1 = f'[CQ:at,qq={event.get_user_id()}]\n'
    msg2 = f"[CQ:image,file={head_dic['illustration_big']}]"
    try:
        msg3 = f"曲名：{head_dic['song']}\n归属于:{head_dic['chapter']}\n曲师:{head_dic['composer']}\nBPM:{head_dic['bpm']}\n曲目/谱面时长：{head_dic['length']}\nAT{head_dic['chart']['AT']['difficulty']}(Max_combo:{head_dic['chart']['AT']['combo']})\nIN{head_dic['chart']['IN']['difficulty']}(Max_combo:{head_dic['chart']['IN']['combo']})\nHD{head_dic['chart']['HD']['difficulty']}(Max_combo:{head_dic['chart']['HD']['combo']})\nEZ{head_dic['chart']['EZ']['difficulty']}(Max_combo:{head_dic['chart']['EZ']['combo']})"
    except:
        msg3 = f"曲名：{head_dic['song']}\n归属于:{head_dic['chapter']}\n曲师:{head_dic['composer']}\nBPM:{head_dic['bpm']}\n曲目/谱面时长：{head_dic['length']}\nIN{head_dic['chart']['IN']['difficulty']}(Max_combo:{head_dic['chart']['IN']['combo']})\nHD{head_dic['chart']['HD']['difficulty']}(Max_combo:{head_dic['chart']['HD']['combo']})\nEZ{head_dic['chart']['EZ']['difficulty']}(Max_combo:{head_dic['chart']['EZ']['combo']})"
    msg = msg2 + msg1 +msg3
    await sec_phi.finish(Message(msg))

@mohu_sec.handle()
async def mhssc(bot: Bot, event: Event):
    getmsg_ = str(event.get_message())
    user = event.get_user_id()
    getmsg = getmsg_.replace('/phi sec', '', 1)
    date_phi_file = open(datepath_phi, 'rb')
    date_phi = json.load(date_phi_file)
    send_end = []
    send_end.extend(
        [
            MessageSegment.node_custom(
                user_id=2710022737,
                nickname="奶茶酱-AqualiteBot",
                content=Message('如下为模糊搜索结果，如需要高清封面图请使用/phi song[曲目]来单独检索')
            )
        ]
    )
    atry = 0
    await mohu_sec.send(Message(f'{getmsg_}模糊检索任务进行中，请稍后..'))
    for sk in list(date_phi.keys()):
        clear_lo = sk.lower()
        clear = clear_lo.replace(' ', '')
        if clear.find(getmsg) != -1:
            head_dic = date_phi[sk]
            msg2 = f"[CQ:image,file={head_dic['illustration']}]"
            try:
                msg3 = f"曲名：{head_dic['song']}\n归属于:{head_dic['chapter']}\n曲师:{head_dic['composer']}\nBPM:{head_dic['bpm']}\n曲目/谱面时长：{head_dic['length']}\nAT{head_dic['chart']['AT']['difficulty']}(Max_combo:{head_dic['chart']['AT']['combo']})\nIN{head_dic['chart']['IN']['difficulty']}(Max_combo:{head_dic['chart']['IN']['combo']})\nHD{head_dic['chart']['HD']['difficulty']}(Max_combo:{head_dic['chart']['HD']['combo']})\nEZ{head_dic['chart']['EZ']['difficulty']}(Max_combo:{head_dic['chart']['EZ']['combo']})"
            except:
                msg3 = f"曲名：{head_dic['song']}\n归属于:{head_dic['chapter']}\n曲师:{head_dic['composer']}\nBPM:{head_dic['bpm']}\n曲目/谱面时长：{head_dic['length']}\nIN{head_dic['chart']['IN']['difficulty']}(Max_combo:{head_dic['chart']['IN']['combo']})\nHD{head_dic['chart']['HD']['difficulty']}(Max_combo:{head_dic['chart']['HD']['combo']})\nEZ{head_dic['chart']['EZ']['difficulty']}(Max_combo:{head_dic['chart']['EZ']['combo']})"
            msg = msg2 + msg3
            atry = 1
            send_end.extend(
                [
                    MessageSegment.node_custom(
                        user_id=2710022737,
                        nickname="奶茶酱-AqualiteBot",
                        content=Message(msg)
                    )
                ]
            )
    if atry == 1:
        await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
        await mohu_sec.finish()
    await mohu_sec.finish(Message(f'呜呜..\n数据库中模糊检索<{getmsg}>无结果诶'))