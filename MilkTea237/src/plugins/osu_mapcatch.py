import requests
import json
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import random
try:
    from nonebot.adapters.onebot.v11 import Message, MessageSegment  # type: ignore
except ImportError:
    from nonebot.adapters.cqhttp import Message, MessageSegment  # type: ignore
secc = on_command('osu mapsec',block=True)
def getdata(keyword):
    url = 'https://api.sayobot.cn/?post'
    headers = {
        'Host': 'api.sayobot.cn', 
        'Connection': 'keep-alive', 
        'Content-Length': '78', 
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"', 
        'Accept': 'application/json, text/plain, */*', 
        'Content-Type': 'text/plain', 'sec-ch-ua-mobile': '?0', 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54', 
        'sec-ch-ua-platform': '"Windows"', 
        'Origin': 'https://osu.sayobot.cn', 
        'Sec-Fetch-Site': 'same-site', 
        'Sec-Fetch-Mode': 'cors', 
        'Sec-Fetch-Dest': 'empty', 
        'Referer': 'https://osu.sayobot.cn/', 
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }
    data = {
        "cmd":"beatmaplist",
        "limit":25,
        "offset":0,
        "type":"search",
        "keyword":keyword
    }
    dataset = requests.post(url, headers=headers,data=json.dumps(data)).text
    return json.loads(dataset)

'''
api返回字典，data作为key,有一个数据列表
[
                {
                        "approved" : -2,
                        "artist" : "Various Artists",
                        "artistU" : "",
                        "creator" : "HoshiMiya_",
                        "favourite_count" : 3,
                        "lastupdate" : 1686162820,
                        "modes" : 8,
                        "order" : 0.0,
                        "play_count" : 2508,
                        "sid" : 2005847,
                        "title" : "120BPM Jack Practice",
                        "titleU" : ""
                },
'''

@secc.handle()
async def get_best(bot: Bot, event: Event):
    msg = str(event.get_message()).replace('/','').replace('osu mapsec','')
    data = getdata(msg)
    send_end = []
    send_end.extend(
        [
            MessageSegment.node_custom(
                user_id=2710022737,
                nickname="bot/聊天群:955760779",
                content=Message(f'搜索<{msg}>结果如下\n最大返回25条，得到的SID可以通过/osudl [SID]进行下载谱面并推送到群聊')
            )
        ]
    )
    try:
        datadict = data['data']
    except:
        await secc.finish(Message('没有搜到这样的曲目呢'))
    for dt in datadict:
        endmsg = f"[CQ:image,file=https://a.sayobot.cn/beatmaps/{dt['sid']}/covers/cover.webp?0]\n标题:{dt['title']}\nSID:{dt['sid']}\n艺术家:{dt['artist']}\n创建者:{dt['creator']}\n小红心数:{dt['favourite_count']}\n总游玩次数:{dt['play_count']}\n"
        send_end.extend(
        [
            MessageSegment.node_custom(
                user_id=2710022737,
                nickname="奶茶酱-AqualiteBot",
                content=Message(endmsg)
            )
        ]
    )
    if len(send_end) == 1:
        await secc.finish(f'没有搜到和<{msg}>有关的谱面哦')
    await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
    await secc.finish()