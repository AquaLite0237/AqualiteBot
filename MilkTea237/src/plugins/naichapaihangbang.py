from nonebot.plugin import on_command
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import os
import datetime as datetime
try:
    from nonebot.adapters.onebot.v11 import Message, MessageSegment  # type: ignore
except ImportError:
    from nonebot.adapters.cqhttp import Message, MessageSegment  # type: ignore
today = datetime.date.today()
ncrank = on_command('奶茶排行',aliases={'奶茶排行榜','ncrank'})

@ncrank.handle()
async def _(bot: Bot, event: Event):
    user = int(event.get_user_id())
    usernickname_dict = await bot.get_stranger_info(user_id=user)
    user_nickname = usernickname_dict['nickname']
    nc_path = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\奶茶总数'
    count = 0
    ready_user_data = {}
    richlist = []
    for a in os.listdir(nc_path):
        count += 1
        user = a.replace('.txt','')
        user_have = open(nc_path + '\\' + a,'r').readline()
        ready_user_data[user_have] = user
        richlist.append(int(user_have))
    n = len(richlist)
    for i in range(n):
        for j in range(0, n-i-1):
            if richlist[j] < richlist[j+1]:
                richlist[j],richlist[j+1] = richlist[j+1], richlist[j]
    maxcount = 1
    usercount = 1
    ranklist_str = ''
    userrank = 'None'
    for p in richlist:
        if maxcount < 16:
            nickname_dict = await bot.get_stranger_info(user_id=int(ready_user_data[str(p)]))
            ranklist_str += f"第{maxcount}:{nickname_dict['nickname']}({ready_user_data[str(p)]})拥有:{p}杯\n"
            maxcount += 1
    for ps in richlist:
        if ready_user_data[str(ps)] == user:
            userrank = usercount
            break
        usercount += 1
    rankstr = f"{today}的奶茶排行榜(共{count}人)\n{ranklist_str}---------------\n你({user_nickname}({user}))的排名是{userrank}"
    await ncrank.finish(Message(rankstr))