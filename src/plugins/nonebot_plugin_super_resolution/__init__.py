from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageEvent, MessageSegment
from nonebot.adapters.onebot.v11.helpers import extract_image_urls
from nonebot.log import logger
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg
from nonebot.typing import T_State

from .enhance import enhance_image, get_model

clarity = on_command("超分", aliases={"放大", "清晰", "超分辨率"})


@clarity.handle()
async def image_analysis(
    event: MessageEvent, matcher: Matcher, state: T_State, arg: Message = CommandArg()
):
    message = reply.message if (reply := event.reply) else event.message
    if imgs := message["image"]:
        matcher.set_arg("imgs", imgs)
    state["text"] = arg.extract_plain_text()


@clarity.got("imgs", prompt="请发送需要超分的图片")
async def get_image(state: T_State, imgs: Message = Arg()):
    urls = extract_image_urls(imgs)
    if not urls:
        await clarity.reject("没有找到图片, 请重新发送")
    state["urls"] = urls


@clarity.handle()
async def analysis_handle(state: T_State):
    model = get_model(state["text"])
    if model.scale not in [2, 3, 4]:
        await clarity.finish("超分失败, 倍率应为二/三/四倍", reply_message=True)

    await clarity.send("正在超分图像, 请稍等……")

    try:
        image = await enhance_image(state["urls"][0], model)
    except Exception as e:
        logger.opt(exception=e).error("超分图像失败")
        await clarity.finish("超分失败, 请稍后重试", reply_message=True)
    msg = str(model) + "\n" + MessageSegment.image(image)
    await clarity.finish(msg, reply_message=True)
