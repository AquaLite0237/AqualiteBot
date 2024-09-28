from e621 import E621
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import random
try:
    from nonebot.adapters.onebot.v11 import Message, MessageSegment  # type: ignore
except ImportError:
    from nonebot.adapters.cqhttp import Message, MessageSegment  # type: ignore
typein = on_command('e621 sec')
getpic = on_command('e621 get')
furrand = on_command('e621 rand',aliases={'er'})
@furrand.handle()
async def get_best(bot: Bot, event: Event):
    msg = str(event.get_message())
    if msg[0]+msg[1] == 'er':
        msg = msg[2:]
    typeinto = msg.replace('/','').replace('e621 rand','').replace(' ','_').replace('#',' ')
    try:
        api = E621()#('Aqualie237','wb6C4vrMXxr95G7SZr1ky63G'))
        posts = api.posts.search(typeinto,limit=320)
    except:
        await furrand.finish(Message(f'出现了未预料的报错，可以尝试更改搜索词来重新获取'))
    lst = posts
    try:
        file = random.choice(lst)
    except:
        await furrand.finish(Message(f'未找到<{typeinto}>的图片,无法随机获取'))
    if file.rating == 's':
        safe = '否'
        pic = f"[CQ:image,file={file.file.url}]"
    else:
        safe = '是'
        pic = f"图片被列为R18评级，请使用下方image_url查看\n\n{file.file.url}"
    sed = f'{pic}\n键入搜索：{typeinto}\nID:{file.id}\n图片安全(是否为r18)评级:{safe}({file.rating})\nscore.TOTAL:{file.score.total}\n从{len(lst)}个搜索结果中抽取（max_limit=320）'
    await furrand.finish(Message(sed))
    
@typein.handle()
async def get_best(bot: Bot, event: Event):
    fullmode = 50
    typeinto = str(event.get_message()).replace('/','').replace('e621 sec','').replace(' ','_').replace('#',' ')
    for ia in typeinto:
        if ia == '@':
            fullmode = 25
            typeinto = typeinto[1:]
            await typein.send(Message(f'已收到指令，正在使用全局原图模式/FULLMODE搜索<{typeinto}>\n如果超时(30s)则可能为风控，无法发送合并消息，请晚些时候再搜索哦'))
            break
        else:
            await typein.send(Message(f'已收到指令，正在搜索<{typeinto}>\n如果超时(30s)则可能为风控，无法发送合并消息，请晚些时候再搜索哦'))
            break
    api = E621()#('Aqualie237','wb6C4vrMXxr95G7SZr1ky63G'))
    posts = api.posts.search(typeinto)
    send_end = []
    send_end.extend(
        [
            MessageSegment.node_custom(
                user_id=2710022737,
                nickname="bot/聊天群:955760779",
                content=Message(f'搜索<{typeinto}>结果如下\n要查看ID的高清原图请发送/e621 get[ID]\n如/e621 get114514\n\n更多详细指令说明请发送/help移步指令文档查看')
            )
        ]
        )
    count = 0
    tmsg = '预览图(如果图片太涩就不会直接展示图片)'
    for post in posts:
        if fullmode == 50:
            if post.rating == 's':
                msgp = f"\n[CQ:image,file={post.preview.url}]"
            else:
                msgp = post.preview.url
        else:
            msgp = f"\n[CQ:image,file={post.preview.url}]"
            tmsg = 'FULLMODE/全局展示原图'
        count += 1
        if count == fullmode:
            break
        send_end.extend(
        [
            MessageSegment.node_custom(
                user_id=2710022737,
                nickname="奶茶酱-AqualiteBot",
                content=Message(f'序号:{count}\n{tmsg}\n{msgp}\nID:{post.id}\n图片安全(是否为r18)评级:{post.rating}\n\n标签:{post.all_tags}\n\nscore.TOTAL:{post.score.total}')
            )
        ]
    )
    if len(send_end) == 1:
        await typein.finish(Message(f'未找到<{typeinto}>的图片,无法随机获取'))
    await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
    await typein.finish()
@getpic.handle()
async def get_best(bot: Bot, event: Event):
    typeinto = str(event.get_message()).replace('/','').replace('e621 get','')
    api = E621()
    pic = api.posts.get(int(typeinto))
    msg = f"\n[CQ:image,file={pic.file.url}]"
    msg2 = f'ID:{pic.id}\n创建时间:{pic.created_at}\n图片参数(宽/高):{pic.file.width}/{pic.file.height}'
    if pic.rating != 's':
        await getpic.finish(Message(f"当前搜索ID图片安全评级不为<Safe>,因为有点/太瑟了！故不展示图片，如需查看请访问下方图片直链\n{msg2}\n图片直链：{pic.file.url}"))
    await getpic.finish(Message(f"{msg + msg2}"))