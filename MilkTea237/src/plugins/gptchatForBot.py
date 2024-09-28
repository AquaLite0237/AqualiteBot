from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
import requests
import json

class API(object):
    def NoMemory(text):
        url = "https://api.chatanywhere.com.cn/v1/chat/completions"
        payload = json.dumps({
           "model": "gpt-3.5-turbo",
           "messages": [
                {
                 "role": "user",
                 "content": text
              }
           ]
        })
        headers = {
           'Authorization': 'Bearer sk-uAiYjvIW1H1ChxqPi45BoS17MxYFKiBq7yQ9TfirGNphsBsr',
           'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
           'Content-Type': 'application/json'
        }

        res_text = json.loads(requests.request("POST", url, headers=headers, data=payload).text)
        res_text = f"{res_text['choices'][0]['message']['content']}"
        return res_text

no_memorychat = on_command("/chat",block=True)

@no_memorychat.handle()
async def nomem(bot: Bot, event: MessageEvent, state: T_State):
   id = event.get_user_id()
   msg = str(event.get_message())
   chattext = msg.replace('/chat','',1)
   chattext = f"[CQ:at,qq={id}]\n{API.NoMemory(chattext)}\n\n返回ChatGPT3.5 turbo模型生成，内容与此bot项目及开发者1259891410无关"
   await no_memorychat.finish(Message(chattext))
