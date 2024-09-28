from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event,Message, MessageSegment
from nonebot.adapters.onebot.v11.helpers import extract_image_urls
from nonebot.typing import T_State
from nonebot.params import Arg
import cv2
import os
import requests

unlocker = on_command('mai unlock',aliases={'解小黑屋','maiunlock'})

@unlocker.got('imgs',prompt='请在大约3s后发送您的最新舞萌登录二维码')
async def getimg(state:T_State,imgs:Message = Arg()):
    urls = extract_image_urls(imgs)
    if not urls:
        await unlocker.finish(Message('未发现二维码登录图\nMaimai_unlocker_Thread:close()'))
    state['urls'] = urls

@unlocker.handle()
async def unlock(state:T_State,event:Event):
    await unlocker.send('收到图片，正在解析二维码并尝试解锁 请耐心等待')
    try:
        user = int(event.get_user_id())
        url = state['urls'][0]
        with open(f'tmp_{user}.png','wb') as tp:
            res_tmp = requests.get(url).content
            tp.write(res_tmp)
            tp.close()
        img = cv2.imread(f'tmp_{user}.png')
        det = cv2.QRCodeDetector()
        val, pts, st_code = det.detectAndDecode(img)
        print(val)
        contenter = requests.get(f'https://maihook.lemonkoi.one/api/hook?id={val}').text
        os.remove(f'tmp_{user}.png')
        await unlocker.finish(Message(contenter))
    except Exception as err:
        await unlocker.finish(Message(f'发生错误啦：{err}\n请联系开发者1259891410解决'))