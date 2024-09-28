from fastapi import FastAPI
import os
import time
import uvicorn
import threading


cqpath = 'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237'
timer = time.time()

API = FastAPI()
last_triggered_time = None
cooldown_minutes = 5  # 冷却时间（分钟）

def relive():
    os.system('%s%s' % ("taskkill /f /im ",'go-cqhttp.exe'))
    os.system('cd C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237 && start go-cqhttp.bat')

@API.get('/restart')
async def status():
    global last_triggered_time
    current_time = time.time()

    if last_triggered_time == None or current_time - last_triggered_time >= cooldown_minutes * 60:
        task = threading.Thread(target=relive)
        task.start()
        last_triggered_time = current_time
        return {
            'code':1,
            'message':'提交线程成功，请等待1分钟后检查bot存活状态，如还无法使用请联系1259891410 tip:刚复活的前五分钟最多发送不到十条消息就会哑巴一会，tx的风控发力了，等到正式开放官方bot接口（个人群聊）并且我的申请通过的时候这个问题就彻底没了'
        }
    else:
        # 冷却中
        remaining_cooldown = int((cooldown_minutes * 60) - (current_time - last_triggered_time))
        return f"冷却中，剩余时间：{remaining_cooldown} 秒"



if __name__ == '__main__':
    uvicorn.run(host=f'0.0.0.0',port=8000,app=API)