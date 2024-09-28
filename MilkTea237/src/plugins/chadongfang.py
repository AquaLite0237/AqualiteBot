from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message
from nonebot import on_command
import time
import requests



cssm = on_regex("^(看船长|看村纱水蜜|看水蜜)$", priority=5, block=True)
yl = on_regex("^(看永琳)$", priority=5, block=True)
xem = on_regex("^(看小恶魔)$", priority=5, block=True)
miyasemahiro = on_regex("^(看miyase_mahiro)$", priority=5, block=True)
zlz = on_regex("^(看朱鹭子)$", priority=5, block=True)
keta = on_regex("^(看ryosios)$", priority=5, block=True)
hutao = on_regex("^(看胡桃)$", priority=5, block=True)
mdl = on_regex("^(看摩多罗)$", priority=5, block=True)
uuz = on_regex("^(看幽幽子|看uuz)$", priority=5, block=True)
yj = on_regex("^(看妖精|看大酱|看大妖精)$", priority=5, block=True)
fsy = on_regex("^(看封兽鵺|看鵺)$", priority=5, block=True)
ml = on_regex("^(看梅莉)$", priority=5, block=True)
lz = on_regex("^(看莲子)$", priority=5, block=True)
al = on_regex("^(看艾丽)$", priority=5, block=True)
xs = on_regex("^(看小伞)$", priority=5, block=True)
ch = on_regex("^(看纯狐)$", priority=5, block=True)
qjm = on_regex("^(看秋姐妹)$", priority=5, block=True)
mm = on_regex("^(看魅魔)$", priority=5, block=True)
hh = on_regex("^(看犬走椛|看椛椛)$", priority=5, block=True)
hm = on_regex("^(看花妈|看幽香)$", priority=5, block=True)
llb = on_regex("^(看莉莉白|看莉莉怀特|看莉莉霍怀特)$", priority=5, block=True)
zy = on_regex("^(看紫苑)$", priority=5, block=True)
sy = on_regex("^(看神绮)$", priority=5, block=True)
shi = on_regex("^(看⑩|看露米娅)$", priority=5, block=True)
tn = on_regex("^(看探女)$", priority=5, block=True)
wu = on_regex("^(看觉|看小⑤|看古明地觉|看⑤|看小五)$", priority=5, block=True)
np = on_regex("^(看女仆|看咲夜)$", priority=5, block=True)
dz = on_regex("^(看堇子)$", priority=5, block=True)
sz = on_regex("^(看婶子|看神子)$", priority=5, block=True)
zi = on_regex("^(看紫|看八云紫|看紫老太婆|看紫m|看紫妈)$", priority=5, block=True)
qx = on_regex("^(看秦心)$", priority=5, block=True)
ym = on_regex("^(看妖梦)$", priority=5, block=True)
lx = on_regex("^(看铃仙)$", priority=5, block=True)
yp = on_regex("^(看帝|看因幡|看因幡帝|看因幡天为)$", priority=5, block=True)
yq = on_regex("^(看夜雀|看小碎骨|看米斯蒂娅)$", priority=5, block=True)
zm = on_regex("^(看早苗|看苗爷|看东风谷早苗)$", priority=5, block=True)
loli = on_regex("^(看萝莉)$", priority=5, block=True)
alice = on_regex("^(看爱丽丝|看小爱)$", priority=5, block=True)
zz = on_regex("^(看转转|看键山雏)$", priority=5, block=True)
fl = on_regex("^(看芙兰|看芙兰朵露|看二小姐)$", priority=5, block=True)
sn = on_regex("^(看山女|看黑谷山女)$", priority=5, block=True)
tz = on_regex("^(看天子|看比那名居天子)$", priority=5, block=True)
ww = on_regex("^(看文文|看射命丸文|看文)$", priority=5, block=True)
pq = on_regex("^(看姆q|看帕秋莉|看帕琪)$", priority=5, block=True)
mls = on_regex("^(看魔理沙|看摸你傻)$", priority=5, block=True)
cx = on_regex("^(看西瓜|看翠香|看伊吹萃香)$", priority=5, block=True)
ll = on_regex("^(看恋恋|看古明地恋|看小石|看小石头)$", priority=5, block=True)
lmly = on_regex("^(看蕾米|看蕾米莉亚|看威严满满|看威严扫地|看大小姐)$", priority=5, block=True)
mh = on_regex("^(看妹红)$", priority=5, block=True)
lmm = on_regex("^(看灵梦|看博丽灵梦|看红白|看十万|看十万灵梦|看赤色杀人魔)$", priority=5, block=True)
hy = on_regex("^(看辉夜|看蓬莱山辉夜)$", priority=5, block=True)
baka = on_regex("^(看⑨|看琪露诺|看baka)$", priority=5, block=True)
touhou = on_regex("^(看东方)$", priority=5, block=True)
xl = on_regex("^(看小铃|看本居小铃|看防撞桶)$", priority=5, block=True)
hyy = on_regex("^(看老师|看慧音)$", priority=5, block=True)
lgl = on_regex("^(看莉格露)$", priority=5, block=True)
hml = on_regex("^(看火焰猫燐|看啊燐|看燐|看阿燐)$", priority=5, block=True)
qyl = on_regex("^(看今泉影狼|看影狼)$", priority=5, block=True)
nzl = on_regex("^(看纳兹琳)$", priority=5, block=True)
kon = on_regex("^(看啊空|看阿空|看灵乌路空|看乌路灵空|看⑥)$", priority=5, block=True)
kty = on_regex("^(看赫卡提亚|看赫卡|看赫卡缇亚)$", priority=5, block=True)
yy = on_regex("^(看冴月麟|看啊麟|看阿麟)$", priority=5, block=True)
ht = on_regex("^(看河城荷取|看河童|看荷取)$", priority=5, block=True)
ny = on_regex("^(看依神女苑|看女苑)$", priority=5, block=True)
lan = on_regex("^(看八云蓝|看蓝)$", priority=5, block=True)
cn = on_regex("^(看橙)$", priority=5, block=True)
shiki = on_regex("^(看四季映姫|看四季)$", priority=5, block=True)
cmq = on_regex("^(看赤蛮奇)$", priority=5, block=True)

def image(url):
    url = requests.get(url).content
    with open('cdongpipic.png','wb') as op:
        op.write(url)
        op.close()
    msg = f"[CQ:image,file=file:///C:\\Users\\Administrator\\Desktop\\MilkTea237\\cdongpipic.png]"
    return Message(f'{msg}')

@cssm.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=minamitsu&size=all&proxy=1"
        msg_id = await cssm.send(image(url))

    except Exception as e:
        await cssm.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@yl.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=eirin&size=all&proxy=1"
        msg_id = await yl.send(image(url))

    except Exception as e:
        await yl.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")

@xem.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=koakuma&size=all&proxy=1"
        msg_id = await xem.send(image(url))

    except Exception as e:
        await xem.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@miyasemahiro.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=miyase_mahiro&size=all&proxy=1"
        msg_id = await miyasemahiro.send(image(url))

    except Exception as e:
        await miyasemahiro.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@zlz.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=tokiko&size=all&proxy=1"
        msg_id = await zlz.send(image(url))

    except Exception as e:
        await zlz.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@keta.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=ryosios&tag=touhou&size=all&proxy=1"
        msg_id = await keta.send(image(url))

    except Exception as e:
        await keta.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@hutao.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kurumi&size=all&proxy=1"
        msg_id = await hutao.send(image(url))

    except Exception as e:
        await hutao.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@mdl.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=okina&tag=touhou&size=all&proxy=1"
        msg_id = await mdl.send(image(url))

    except Exception as e:
        await mdl.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")

@uuz.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=yuyuko&size=all&proxy=1"
        msg_id = await uuz.send(image(url))

    except Exception as e:
        await uuz.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@yj.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=daiyousei&size=all&proxy=1"
        msg_id = await yj.send(image(url))

    except Exception as e:
        await yj.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@fsy.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=nue&size=all&proxy=1"
        msg_id = await fsy.send(image(url))

    except Exception as e:
        await fsy.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@ml.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=maribel&size=all&proxy=1"
        msg_id = await ml.send(image(url))

    except Exception as e:
        await ml.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@al.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=elly&size=all&proxy=1"
        msg_id = await al.send(image(url))

    except Exception as e:
        await al.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@xs.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kogasa&size=all&proxy=1"
        msg_id = await xs.send(image(url))

    except Exception as e:
        await xs.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
       
@ch.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=junko&size=all&proxy=1"
        msg_id = await ch.send(image(url))

    except Exception as e:
        await ch.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@qjm.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=shizuha&size=all&proxy=1"
        msg_id = await qjm.send(image(url))

    except Exception as e:
        await qjm.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@mm.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=mima&size=all&proxy=1"
        msg_id = await mm.send(image(url))

    except Exception as e:
        await mm.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@hh.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=momiji&size=all&proxy=1"
        msg_id = await hh.send(image(url))

    except Exception as e:
        await hh.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@hm.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kazami&size=all&proxy=1"
        msg_id = await hm.send(image(url))

    except Exception as e:
        await hm.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@llb.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=lily_white&size=all&proxy=1"
        msg_id = await llb.send(image(url))

    except Exception as e:
        await llb.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@zy.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=yorigami_shion&size=all&proxy=1"
        msg_id = await zy.send(image(url))

    except Exception as e:
        await zy.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@sy.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=shinki&size=all&proxy=1"
        msg_id = await sy.send(image(url))

    except Exception as e:
        await sy.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@shi.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=rumia&size=all&proxy=1"
        msg_id = await shi.send(image(url))

    except Exception as e:
        await shi.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@tn.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=sagume&size=all&proxy=1"
        msg_id = await tn.send(image(url))

    except Exception as e:
        await tn.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@wu.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=satori&size=all&proxy=1"
        msg_id = await wu.send(image(url))

    except Exception as e:
        await wu.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@np.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=sakuya&size=all&proxy=1"
        msg_id = await np.send(image(url))

    except Exception as e:
        await np.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@dz.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=sumireko&size=all&proxy=1"
        msg_id = await dz.send(image(url))

    except Exception as e:
        await dz.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@sz.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=toyosatomimi&size=all&proxy=1"
        msg_id = await sz.send(image(url))

    except Exception as e:
        await sz.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@zi.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=yuka&size=all&proxy=1"
        msg_id = await zi.send(image(url))

    except Exception as e:
        await zi.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@qx.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kokoro&size=all&proxy=1"
        msg_id = await qx.send(image(url))

    except Exception as e:
        await qx.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@ym.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=youmu&size=all&proxy=1"
        msg_id = await ym.send(image(url))

    except Exception as e:
        await ym.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@lx.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=reisen&size=all&proxy=1"
        msg_id = await lx.send(image(url))

    except Exception as e:
        await lx.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
     
@yp.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=tewi&size=all&proxy=1"
        msg_id = await yp.send(image(url))

    except Exception as e:
        await yp.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@yq.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=mystia&size=all&proxy=1"
        msg_id = await yq.send(image(url))

    except Exception as e:
        await yq.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@zm.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=sanae&size=all&proxy=1"
        msg_id = await zm.send(image(url))

    except Exception as e:
        await zm.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@loli.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=loli&size=all&proxy=1"
        msg_id = await loli.send(image(url))

    except Exception as e:
        await loli.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@alice.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=alice&size=all&proxy=1"
        msg_id = await alice.send(image(url))

    except Exception as e:
        await alice.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@zz.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kagiyama&size=all&proxy=1"
        msg_id = await zz.send(image(url))

    except Exception as e:
        await zz.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@fl.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=flandre&size=all&proxy=1"
        msg_id = await fl.send(image(url))

    except Exception as e:
        await fl.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@sn.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=yamame&size=all&proxy=1"
        msg_id = await sn.send(image(url))

    except Exception as e:
        await sn.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@tz.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=tenshi&size=all&proxy=1"
        msg_id = await tz.send(image(url))

    except Exception as e:
        await tz.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@ww.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=aya&size=all&proxy=1"
        msg_id = await ww.send(image(url))

    except Exception as e:
        await ww.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@pq.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=patchouli&size=all&proxy=1"
        msg_id = await pq.send(image(url))

    except Exception as e:
        await pq.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
     
@mls.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=marisa&size=all&proxy=1"
        msg_id = await mls.send(image(url))

    except Exception as e:
        await mls.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@cx.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=suika&size=all&proxy=1"
        msg_id = await cx.send(image(url))

    except Exception as e:
        await cx.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@ll.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=koishi&size=all&proxy=1"
        msg_id = await ll.send(image(url))

    except Exception as e:
        await ll.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@lmly.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=remilia&size=all&proxy=1"
        msg_id = await lmly.send(image(url))

    except Exception as e:
        await lmly.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@mh.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=mokou&size=all&proxy=1"
        msg_id = await mh.send(image(url))

    except Exception as e:
        await mh.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
               
@lmm.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=reimu&size=all&proxy=1"
        msg_id = await lmm.send(image(url))

    except Exception as e:
        await lmm.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@hy.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kaguya&size=all&proxy=1"
        msg_id = await hy.send(image(url))

    except Exception as e:
        await hy.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@baka.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=cirno&size=all&proxy=1"
        msg_id = await baka.send(image(url))

    except Exception as e:
        await baka.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@touhou.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?size=all&proxy=1"
        msg_id = await touhou.send(image(url))

    except Exception as e:
        await touhou.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@xl.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kosuzu&size=all&proxy=1"
        msg_id = await xl.send(image(url))

    except Exception as e:
        await xl.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
               
@hyy.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kamishirasawa_keine&proxy=1"
        msg_id = await hyy.send(image(url))

    except Exception as e:
        await hyy.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@lgl.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=wriggle_nightbug&proxy=1"
        msg_id = await lgl.send(image(url))

    except Exception as e:
        await lgl.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@hml.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kaenbyou_rin&proxy=1"
        msg_id = await hml.send(image(url))

    except Exception as e:
        await hml.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@qyl.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=imaizumi_kagerou&proxy=1"
        msg_id = await qyl.send(image(url))

    except Exception as e:
        await qyl.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@nzl.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=nazrin&proxy=1"
        msg_id = await nzl.send(image(url))

    except Exception as e:
        await nzl.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@kon.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=reiuji_utsuho&proxy=1"
        msg_id = await kon.send(image(url))

    except Exception as e:
        await kon.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@kty.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=hecatia_lapislazuli&proxy=1"
        msg_id = await kty.send(image(url))

    except Exception as e:
        await kty.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@yy.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=satsuki_rin&proxy=1"
        msg_id = await yy.send(image(url))

    except Exception as e:
        await yy.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@ht.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=kawashiro_nitori&proxy=1"
        msg_id = await ht.send(image(url))

    except Exception as e:
        await ht.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@ny.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=yorigami_joon&proxy=1"
        msg_id = await ny.send(image(url))

    except Exception as e:
        await ny.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@lan.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=yakumo_ran&proxy=1"
        msg_id = await lan.send(image(url))

    except Exception as e:
        await lan.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@cn.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=chen&proxy=1"
        msg_id = await cn.send(image(url))

    except Exception as e:
        await cn.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@shiki.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=shiki&proxy=1"
        msg_id = await shiki.send(image(url))

    except Exception as e:
        await shiki.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
        
@cmq.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        url = "https://img.paulzzh.com/touhou/random?tag=sekibanki&proxy=1"
        msg_id = await cmq.send(image(url))

    except Exception as e:
        await cmq.send("出错了！")
        logger.error(f"看东方 发送了未知错误 {type(e)}：{e}")
