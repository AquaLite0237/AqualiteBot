from nonebot.adapters import Message
from nonebot.params import ArgStr,CommandArg
from nonebot.matcher import Matcher
from nonebot import on_command
from .data_source import calculate_acc

malody = on_command('/acc')

@malody.handle()
async def _handle(matcher: Matcher,msg: Message = CommandArg()):
    msg = msg.extract_plain_text().split(" ")
    if len(msg) == 2:
        matcher.set_arg("t",msg[0])
        matcher.set_arg("accs",msg[1])

@malody.got("t", prompt = '请输入要查询的段位(regular*|regular*v2|ex*|ex*v2|reform*)[*换成对应的数字或字母]')
@malody.got('accs', prompt = '请按顺序输入acc如：99.26-98.63-97.32-96.11')
async def _got(t = ArgStr("t"),accs = ArgStr("accs")):
    accs = accs.strip().split("-")
    try:
        result = calculate_acc(accs[0],accs[1],accs[2],accs[3],t)
        acc1 = str(result[0])[:5]
        acc2 = str(result[1])[:5]
        acc3 = str(result[2])[:5]
        acc4 = str(result[3])[:5]
    except:
        await malody.finish("失败，输入参数有误或不存在",at_sender=True)
    await malody.finish("\n您的第一首acc是:{}%\n您的第二首acc是:{}%\n您的第三首acc是:{}%\n您的第四首acc是:{}%".format(acc1,acc2,acc3,acc4),at_sender=True)