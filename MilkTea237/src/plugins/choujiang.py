import random
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import datetime as datetime
import os
from nonebot.adapters.onebot.v11.message import Message

cj = on_command("抽奶茶")


@cj.handle()
async def cj_handle(bot: Bot, event: Event):
    id = event.get_user_id()
    today = datetime.date.today()
    nums = str(event.get_message()).replace('抽奶茶','')
    if nums == '':
        nums = 1
    try:
        nums = int(nums)
    except:
        nums = 1
    huafei = nums*2
    user_qq = int(event.get_user_id())
    yanwenzi = [" ( ੭ ˙ᗜ˙ )","٩( ๑╹ ꇴ╹)۶","✧(≖ ◡ ≖✿)","٩( 'ω' )و ","(›´ω`‹ )"]
    getrnd = random.randint(1,65)
    chos = random.randint(1,13)
    nc_path = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\奶茶总数'
    nc_paths = f'{nc_path}\\{user_qq}.txt'
    if not os.path.exists(nc_paths):
        await cj.finish(Message(f'至少要2杯奶茶才能抽哦！你还没有奶茶，先发送 签到 试试吧！'))
    ncsp = int(open(nc_paths,'r',encoding='utf-8').read())
    if nums > 50:
        await cj.finish(Message('抽奖次数太大啦！(必须小于50)'))
    if ncsp >= huafei:
        if nums != 1:
            sendend = ''
            tmp = 0
            for io in range(nums):
                getrnd = random.randint(1,50)
                chos = random.randint(1,15)
                if chos == 1:
                    tmp += getrnd
                    sendend += f"轮{io+1}:获得{getrnd} {random.choice(yanwenzi)}；"
                else:
                    sendend += f"轮{io+1}:-2;"
                    tmp -= 2
            with open(nc_paths, 'w') as n:
                n.write(str(ncsp+tmp))
                n.close()
            await cj.finish(Message(f"进行了{nums}次抽奖\n{sendend[:-1]}\n总变化：{tmp}"))
        if chos == 1:
            ncs = open(nc_paths,'r',encoding='utf-8').read()
            with open(nc_paths, 'w') as n:
                ncms = int(ncs) + getrnd
                n.write(str(ncms))
                n.close()
                cj_ok1 = f"[CQ:at,qq={id}]"
                cjmsg = cj_ok1 + f"\n恭喜{random.choice(yanwenzi)}\n获得了{getrnd}杯奶茶"
                await cj.finish(Message(cjmsg))
        else:
            ncs = open(nc_paths,'r',encoding='utf-8').read()
            with open(nc_paths, 'w') as n:
                ncms = int(ncs) - 2
                n.write(str(ncms))
                n.close()
                cj_ok1 = f"[CQ:at,qq={id}]"
                cjmsg = cj_ok1 + f"\n啊呜..\n没有抽到什么呢（失去了2杯奶茶）\n获奖偏移值：{21-chos}（数字越小越接近中奖，最大为20）"
                await cj.finish(Message(cjmsg))
    else:
        await cj.finish(Message(f'抽{nums}次需要{huafei}杯奶茶才能抽哦！你目前只有{ncsp}杯'))