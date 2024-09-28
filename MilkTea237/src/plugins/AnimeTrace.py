import os
import random
from nonebot import on_command
from nonebot.typing import T_State
from hashlib import md5
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent,Message
import json
from nonebot.adapters.onebot.v11.helpers import extract_image_urls
from nonebot.params import Arg



#fork from nonebot_plugin_animetrace 稍作兼容性适配

async def getData(imageUrl, model="anime", mode=0):
    save_name = md5(imageUrl.encode("utf-8")).hexdigest() + ".png"
    await AsyncHttpx.download_file(imageUrl, save_name)
    files = {
        'image': open(save_name, 'rb')
    }
    content = await AsyncHttpx.post(f"https://aiapiv2.animedb.cn/ai/api/detect?model={model}&force_one={mode}",
                                    data=None, files=files)
    content = json.loads(content.text)
    return content


def buildMessage(result, mode, Model):
    modelName = ""
    if Model == 'game':
        modelName = "游戏"
    else:
        modelName = "动漫"

    """
    :param Model: 
    :param result: result from AnimeTrace
    :param mode: mode
    :return: message_build
    """
    if mode == 0:
        char = ""
        for i in result['data']:
            message = "人物:" + i['name'] + f"--来自{modelName}《" + i['cartoonname'] + "》" + "\n"
            char += message
        return char

    else:
        char = ""
        count = 0
        message_list = []

        message_list.append(link(f"API from AnimeTrace 模型{modelName}图片预测结果"))
        for i in result['data']:
            count += 1
            message = f"第{count}个人物:" + i['char'][0]['name'] + f"--来自{modelName}《" + i['char'][0][
                'cartoonname'] + "》" + "\n"
            if (len(i['char']) != 1):
                for idx, d in enumerate(i['char']):
                    if (idx == 0):
                        continue
                    message += "--其他可能性"
                    message += "-" + d['name'] + f"--来自{modelName}《" + d['cartoonname'] + "》" + "\n"
            char += message
            message_list.append(link(char, i['char'][0]['name']))
            char = ""
        message_list.append(link("共预测到" + str(len(result['data'])) + "个角色\n"))
        return message_list


def link(string, name=None):
    return {
        "type": "node",
        "data": {
            "name": f"{name}",
            "uin": f"2710022737",  # 这里可以自定义
            "content": string,
        },
    }


moevision = on_command("动漫识别")
more_moevision = on_command("多可能动漫识别")
galvision = on_command("游戏识别")
more_galvision = on_command("多可能游戏识别")

@moevision.got("img_url", prompt="请给出带有人物的图片")
async def handle_event(bot: Bot, event: MessageEvent, state: T_State,imgs:Message = Arg()):
    img_url = extract_image_urls(imgs)
    state["img_url"] = img_url
    print(state)
    result = await getData(state["img_url"][0], "anime", 0)
    message = buildMessage(result, 0, "anime")
    if len(result['data']) == 0:
        await moevision.send("抱歉图片中未识别到动漫人物")
        return
    await moevision.send("API from AnimeTrace，您的图片预测结果是\n" + str(message) + "共预测到" + str(
        len(result['data'])) + "个角色\n" + "")
    removeTemp(state["img_url"][0])


@more_moevision.got("img_url", prompt="请给出带有人物的图片")
async def handle_event(bot: Bot, event: MessageEvent, state: T_State,imgs:Message = Arg()):
    img_url = extract_image_urls(imgs)
    state["img_url"] = img_url
    result = await getData(state["img_url"][0], "anime", 1)
    if len(result['data']) == 0:
        await more_moevision.send("抱歉图片中未识别到动漫人物")
        return
    message = buildMessage(result, 1, "anime")
    await bot.send_group_forward_msg(group_id=event.group_id, messages=message) if isinstance(event,
                                                                                              GroupMessageEvent) else await bot.send_private_forward_msg(
        user_id=event.user_id, messages=message)
    removeTemp(state["img_url"][0])


@galvision.got("img_url", prompt="请给出带有人物的图片")
async def handle_event(bot: Bot, event: MessageEvent, state: T_State,imgs:Message = Arg()):
    img_url = extract_image_urls(imgs)
    state["img_url"] = img_url
    result = await getData(state["img_url"][0], "game", 0)
    message = buildMessage(result, 0, "game")
    if len(result['data']) == 0:
        await galvision.send("图片中未识别到游戏人物")
        return
    await galvision.send("API from AnimeTrace，您的图片预测结果是\n" + str(message) + "共预测到" + str(
        len(result['data'])) + "个角色\n" + "")
    removeTemp(state["img_url"][0])


@more_galvision.got("img_url", prompt="请给出带有人物的图片")
async def handle_event(bot: Bot, event: MessageEvent, state: T_State,imgs:Message = Arg()):
    img_url = extract_image_urls(imgs)
    state["img_url"] = img_url
    result = await getData(state["img_url"][0], "game", 1)
    if len(result['data']) == 0:
        await more_galvision.send("图片中未识别到游戏人物")
        return
    message = buildMessage(result, 1, "game")
    await bot.send_group_forward_msg(group_id=event.group_id, messages=message) if isinstance(event,
                                                                                              GroupMessageEvent) else await bot.send_private_forward_msg(
        user_id=event.user_id, messages=message)
    removeTemp(state["img_url"][0])


def removeTemp(img):
    try:
        os.remove(md5(img.encode("utf-8")).hexdigest() + ".png")
    except:
        return
