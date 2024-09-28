import requests
import pickle
from nonebot.plugin import on_command
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import os
import json
try:
    from nonebot.adapters.onebot.v11 import Message, MessageSegment  # type: ignore
except ImportError:
    from nonebot.adapters.cqhttp import Message, MessageSegment  # type: ignore

User_info = on_command('/wlf bind')
User_Output = on_command('/wlf',priority=8)
restart_user = on_command('/wlf restart_user')
bindsec = on_command('/wlf bindsec')
best = on_command('/wlf best')
dumpdata = on_command('/wlf dump')
sec_music = on_keyword({'/wlf sec'},priority=5)
sec_music_id = on_keyword({'/wlf secid'},priority=4)
sec_score = on_keyword({'/wlf 查分'},priority=4)
mohu_sec_score = on_keyword({'/wlf 模糊查分'},priority=3)
newsong = on_command('/wlf 新曲成绩',aliases={"/wlf 新歌成绩"})

path = 'MilkTea237\\data\\Aqualite\\DanceCube'
user_file = 'MilkTea237\\data\\Aqualite\\DanceCube\\user.pkl'
get_headers = {
    'User-Agent': "Mozilla/5.0 (Windows  NT 10.0; Win64; x64)pyh AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 'content-type': 'application/x-www-form-urlencoded'"
}

def music_type(chos):
    url_new = 'https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=1&musicIDList=&machineType=0'
    url_chin = 'https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=2&musicIDList=&machineType=0'
    url_yueyu = 'https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=3&musicIDList=&machineType=0'
    url_axiba = 'https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=4&musicIDList=&machineType=0'
    url_oumei = 'https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=5&musicIDList=&machineType=0'
    url_other = 'https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=6&musicIDList=&machineType=0'
    if chos == '国语':
        return url_chin
    elif chos == '粤语':
        return  url_yueyu
    elif chos == '韩语':
        return url_axiba
    elif chos == '欧美':
        return url_oumei
    elif chos == '其他':
        return url_other
    elif chos == '最新':
        return url_new
    else:
        return '000'

@newsong.handle()
async def mhsc(bot: Bot, event: Event):
    User_qq = int(event.get_user_id())
    counter_n = open(user_file, 'rb')
    counter_dict = pickle.load(counter_n)
    try:
        user_id = counter_dict[f'{User_qq}_id']
        user_token = counter_dict[f'{User_qq}_token']
        print(user_id)
        print(user_token)
    except KeyError:
        await newsong.finish(Message(f'你还没有绑定哦！请先发送/help 查看舞立方模块绑定账号指令'))
    get_type_url = music_type('最新')
    if get_type_url == '000':
        await newsong.finish(Message(f'[ERROR]类型错误\n歌曲类型只能键入[最新，国语，粤语，韩语，欧美，其他]，自制谱面列属于‘其他’类型中\n例:/wlf 模糊查分其他Eltaw'))
    atry = 0
    User_info_headers = {}
    # User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {user_token}"
    rea = requests.get(
        url=get_type_url,
        headers=User_info_headers, stream=True, verify=False).text
    return_score_dict = json.loads(rea)
    send_end = []
    send_end.extend(
        [
            MessageSegment.node_custom(
                user_id=2710022737,
                nickname="奶茶酱-AqualiteBot",
                content=Message(f'如下为玩家ID为<{user_id}>的<最新>类别歌曲成绩汇总！')
            )
        ]
    )
    for sk in return_score_dict:
        clear_na = sk['Name']
        clear_lo = clear_na.lower()
        clear = clear_lo.replace(' ', '')
        headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
        headpic_ = f"C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
        if not os.path.exists(headpic_):
            headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/picnotfound.jpg"
        score_msg = f"封面↑\n曲名：{sk['Name']}\n(难度：{sk['MusicRank']})\n总得分：{sk['Score']}\n最大连击:{sk['ComCount']}\nMiss数:{sk['MissCount']}\nACC/准确率：{sk['PercentScore']}\n全国排名：{sk['LvRecord']}({sk['Time']})"
        atry = 1
        send_end.extend(
                [
                    MessageSegment.node_custom(
                        user_id=2710022737,
                        nickname="奶茶酱-AqualiteBot",
                        content=Message(f'[CQ:image,file={headpic}]\n{score_msg}')
                    )
                ]
            )
    await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
    await newsong.finish()


@mohu_sec_score.handle()
async def mhsc(bot: Bot, event: Event):
    getmsg_ = str(event.get_message())
    User_qq = int(event.get_user_id())
    counter_n = open(user_file, 'rb')
    counter_dict = pickle.load(counter_n)
    try:
        user_id = counter_dict[f'{User_qq}_id']
        user_token = counter_dict[f'{User_qq}_token']
        print(user_id)
        print(user_token)
    except KeyError:
        await mohu_sec_score.finish(Message(f'你还没有绑定哦！请先发送/help 查看舞立方模块绑定账号指令'))
    getmsg = getmsg_.replace('/wlf 模糊查分', '', 1)
    msg_list = list(getmsg)
    get_chos_type = msg_list[0] + msg_list[1]
    get_type_url = music_type(get_chos_type)
    if get_type_url == '000':
        await mohu_sec_score.finish(Message(f'[ERROR]类型错误\n歌曲类型只能键入[最新，国语，粤语，韩语，欧美，其他]，自制谱面列属于‘其他’类型中\n例:/wlf 模糊查分其他Eltaw'))
    aa_noend = getmsg.replace(get_chos_type, '', 1)
    a_noend = aa_noend.replace(' ', '')
    end_a = a_noend.lower()
    atry = 0
    User_info_headers = {}
    # User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {user_token}"
    rea = requests.get(
        url=get_type_url,
        headers=User_info_headers, stream=True, verify=False).text
    return_score_dict = json.loads(rea)
    send_end = []
    for sk in return_score_dict:
        clear_na = sk['Name']
        clear_lo = clear_na.lower()
        clear = clear_lo.replace(' ', '')
        if clear.find(end_a) != -1:
            headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
            headpic_ = f"C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
            if not os.path.exists(headpic_):
                headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/picnotfound.jpg"
            score_msg = f"封面↑\n曲名：{sk['Name']}\n(难度：{sk['MusicRank']})\n总得分：{sk['Score']}\n最大连击:{sk['ComCount']}\nMiss数:{sk['MissCount']}\nACC/准确率：{sk['PercentScore']}\n全国排名：{sk['LvRecord']}({sk['Time']})"
            atry = 1
            send_end.extend(
                    [
                        MessageSegment.node_custom(
                            user_id=2710022737,
                            nickname="奶茶酱-AqualiteBot",
                            content=Message(f'[CQ:image,file={headpic}]\n{score_msg}')
                        )
                    ]
                )
    if atry == 1:
        await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
        await mohu_sec_score.finish()
    await mohu_sec_score.finish(Message(f'模糊查询 {get_chos_type} 类型中的曲目 {end_a}，失败啦!'))


@sec_score.handle()
async def get_score(bot: Bot, event: Event):
    getmsg_ = str(event.get_message())
    User_qq = int(event.get_user_id())
    counter_n = open(user_file, 'rb')
    counter_dict = pickle.load(counter_n)
    try:
        user_id = counter_dict[f'{User_qq}_id']
        user_token = counter_dict[f'{User_qq}_token']
        print(user_id)
        print(user_token)
    except KeyError:
        await sec_score.finish(Message(f'你还没有绑定哦！请先发送/help 查看舞立方模块绑定账号指令'))
    getmsg = getmsg_.replace('/wlf 查分', '', 1)
    msg_list = list(getmsg)
    get_chos_type = msg_list[0] + msg_list[1]
    get_type_url = music_type(get_chos_type)
    if get_type_url == '000':
        await sec_score.finish(Message(f'[ERROR]类型错误\n歌曲类型只能键入[最新，国语，粤语，韩语，欧美，其他]，自制谱面列属于‘其他’类型中\n例:/wlf 查分其他Eltaw'))
    aa_noend = getmsg.replace(get_chos_type, '', 1)
    a_noend = aa_noend.replace(' ', '')
    end_a = a_noend.lower()
    atry = 0
    score_msg = ''
    User_info_headers = {}
    # User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {user_token}"
    rea = requests.get(
        url=get_type_url,
        headers=User_info_headers, stream=True, verify=False).text
    return_score_dict = json.loads(rea)
    send_end = []
    for sk in return_score_dict:
        clear_na = sk['Name']
        clear_lo = clear_na.lower()
        clear = clear_lo.replace(' ', '')
        if clear == str(end_a):
            headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
            headpic_ = f"C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
            if not os.path.exists(headpic_):
                headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/picnotfound.jpg"
            score_msg = f"封面↑\n曲名：{sk['Name']}\n(难度：{sk['MusicRank']})\n总得分：{sk['Score']}\n最大连击:{sk['ComCount']}\nMiss数:{sk['MissCount']}\nACC/准确率：{sk['PercentScore']}\n全国排名：{sk['LvRecord']}({sk['Time']})"
            atry = 1
            send_end.extend(
                [
                    MessageSegment.node_custom(
                        user_id=2710022737,
                        nickname="奶茶酱-AqualiteBot",
                        content=Message(f'[CQ:image,file={headpic}]\n{score_msg}')
                    )
                ]
            )
    if atry == 1:
        await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
        await sec_score.finish()
    await sec_score.finish(Message(f'查询 {get_chos_type} 类型中的曲目 {end_a}，失败啦..可能是你未游玩过此曲目或键入的曲目名称不为全称，酱酱暂时不支持别称查询哦！果咩纳塞！'))

@sec_music_id.handle()
async def get_qrcode(bot: Bot, event: Event):
    getmsg_ = str(event.get_message())
    getmsg = getmsg_.replace('/wlf secid', '', 1)
    try:
        int(getmsg)
    except ValueError:
        await sec_music_id.finish(Message('[ERROR]:ValueError\n可能是你键入的id不为纯数字，请输入纯数字的谱面id\n例：/wlf secid5496)'))
    User_info_headers = {}
    # User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers[
        "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    # ia = str(input('a'))
    try:
        rea = requests.get(
            url=f'https://dancedemo.shenghuayule.com/Dance/api/Goods/GetGoodsMusic?page=1&pagesize=10&tag=&language=&orderby=1&ordertype=1&keyword={getmsg}',
            headers=User_info_headers, stream=True, verify=False).text
        date_ = json.loads(rea)
        datea = date_['List']
    except Exception as ss:
        await sec_music_id.finish(Message(f'[ERROR]api无返回，请尝试重新登录\n{ss}'))
    list_long = len(datea)
    if list_long == 0:
        await sec_music_id.finish(Message(f'搜索{getmsg}无结果哦！'))
    date = date_['List'][0]
    if list_long > 1:
        await sec_music_id.finish(Message('[ERROR]:LenError\n可能是你键入的id不唯一，请输入完整谱面id\n例：/wlf secid1510\n我也不知道会不会报这个错，先写着吧)'))
    owner_name = date['OwnerName']
    owner_id = date['OwnerID']
    goodid = date['MusicID']
    goodname = date['GoodsName']
    levels = ''
    for level in date['LevelList']:
        levels += f"{level['MusicLevel']}/"
    headpic = f"[CQ:image,file={date['PicPath']}]"
    sendmsg = f"\n曲名：{goodname}(id{goodid})\n曲目音频直链：{date['AudioUrl']} 点击可试听或下载\n谱师：{owner_name}(id{owner_id})\n难度等级:{levels}\n谱师留言：{date['GoodsIntro']}\n标签：{date['TagList']}\n购买所需金币：{date['PriceSale']}({date['ExpireUnitTypeText']})"
    endmsg = headpic + sendmsg
    await sec_music_id.finish(Message(endmsg))

@sec_music.handle()
async def get_qrcode(bot: Bot, event: Event):
    getmsg_ = str(event.get_message())
    getmsg = getmsg_.replace('/wlf sec', '', 1)
    User_info_headers = {}
    # User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers[
        "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    # ia = str(input('a'))
    try:
        rea = requests.get(
            url=f'https://dancedemo.shenghuayule.com/Dance/api/Goods/GetGoodsMusic?page=1&pagesize=10&tag=&language=&orderby=1&ordertype=1&keyword={getmsg}',
            headers=User_info_headers, stream=True, verify=False).text
        date_ = json.loads(rea)
        datea = date_['List']
        list_long = len(datea)
    except Exception as ss:
        await sec_music.finish(Message(f'[ERROR]api无返回，请尝试重新登录\n{ss}'))
    if list_long == 0:
        await sec_music.finish(Message(f'搜索{getmsg}无结果哦！'))
    elif list_long == 10:
        await sec_music.finish(Message(f'{getmsg}返回结果太多啦！或许可以试试把搜索词更加精准些(RETURN_MAX=8)'))
    ata = f'[CQ:at,qq={event.get_user_id()}]\n'
    sendmsg = ata + '搜索结果(GET_RETURN):\n'
    for date in datea:
        owner_name = date['OwnerName']
        owner_id = date['OwnerID']
        goodid = date['MusicID']
        goodname = date['GoodsName']
        levels = ''
        for level in date['LevelList']:
            levels += f"{level['MusicLevel']}/"
        sendmsg += f"\n曲名：{goodname}(id{goodid})\n谱师：{owner_name}(id{owner_id})\n难度等级:{levels}\n"
    sendmsg += '\n谱面详细信息查询请发送:/wlf secid[谱面id]来查询\n例：/wlf secid1510'
    await sec_music.finish(Message(sendmsg))

@dumpdata.handle()
async def get_qrcode(bot: Bot, event: Event):
    User_qq = int(event.get_user_id())
    if User_qq != 1259891410:
        pass
    else:
        rd = open(user_file,'rb')
        dumpd = pickle.load(rd)
        await dumpdata.send(Message(f'try'))
        await dumpdata.finish(Message(f'{dumpd}'))

@User_Output.handle()
async def get_user(bot: Bot, event: Event):
    User_qq = int(event.get_user_id())
    counter_n = open(user_file, 'rb')
    counter_dict = pickle.load(counter_n)
    try:
        user_id = counter_dict[f'{User_qq}_id']
        user_token = counter_dict[f'{User_qq}_token']
        print(user_id)
        print(user_token)
    except KeyError:
        await User_Output.finish(Message(f'你还没有绑定哦！请先发送/help 查看舞立方模块绑定账号指令'))
    User_Info_Url = f"https://dancedemo.shenghuayule.com/Dance/api/User/GetInfo?userId={user_id}"
    User_info_headers = {}
    User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {user_token}"
    try:
        User_info_response_dic = requests.get(
            url=User_Info_Url,
            headers=User_info_headers, stream=True, verify=False).text
        User_info_response = json.loads(User_info_response_dic)
    except Exception as ss:
        await User_Output.finish(Message(f'[ERROR]api无返回，请尝试重新登录\n{ss}'))
    User_id = User_info_response['UserID']
    User_Name = User_info_response['UserName']
    Music_Speed = User_info_response['MusicSpeed']
    Music_Score = User_info_response['MusicScore']
    Rank_Nation = User_info_response['RankNation']
    Combo_Percent = User_info_response['ComboPercent']
    Lv_ratio = User_info_response['LvRatio']
    Team_Id = User_info_response['TeamID']
    Team_Name = User_info_response['TeamName']
    msg1 = f'[CQ:at,qq={event.get_user_id()}]\n'
    msg2 = f"[CQ:image,file={User_info_response['HeadimgURL']}]"
    msg3 = f'User-INFO\n你的舞立方ID是-{User_id}\n机台昵称为-{User_Name}\n音符流速为{Music_Speed}速！\n积分有{Music_Score}！\n全国排名{Rank_Nation}!太强了\n全连率:{Combo_Percent}\n战力值有{Lv_ratio}点！\n你加入了{Team_Name}战队！(战队ID是{Team_Id})\nTip:如果反馈的不是您的账号信息，请晚些时候再自行私聊bot绑定'
    msg = msg2 + msg1 + msg3
    await User_Output.finish(Message(f'{msg}'))


@User_info.handle()
async def get_qrcode(bot: Bot, event: Event):
    User_qq = int(event.get_user_id())
    ids_dic = ["yyQ6VxqMeIKJDzVmQuHtNAUGxHAgSxmR",
               "yyQ6VxqMeIL2hceWzZtdqsJxNf/hHSzH",
               "yyQ6VxqMeIL2hceWzZtdqtGq81Ru8pIE",
               "yyQ6VxqMeILLsdiEbWkbSnddhlyVGcNa",
               "yyQ6VxqMeILneEzfVyXPFVCZoOuXSoH3"]
    if not os.path.exists(path):
        os.makedirs(path)
        aa = open(user_file, 'w')
        print(f'当前无匹配路径，已自动创建目录{aa}')
        counters = {}
        counters['counter'] = 0
        pickle.dump(counters, open(user_file, 'wb'))
    counter_n = open(user_file,'rb')
    counter_dict = pickle.load(counter_n)
    counters = counter_dict['counter']
    if int(counters) > 4:
        counters = 0
    counter_dict[f'{User_qq}_ids'] = ids_dic[int(counters)]
    id = counter_dict[f'{User_qq}_ids']
    get_url = f"https://dancedemo.shenghuayule.com/Dance/api/Common/GetQrCode?id={id}"
    get_return = requests.get(url=get_url, headers=get_headers).text
    json_dic = json.loads(get_return)
    qrcode_url = json_dic['QrcodeUrl']
    qrcode = f'[CQ:image,file={qrcode_url}]'
    msg11 = f'[CQ:at,qq={event.get_user_id()}]\n'
    msg22 = f"{qrcode}\n请在120秒内完成扫码登录\n并在扫码结束后发送:\n/wlf bindsec\n来保存身份令牌（token)后续只需要输入/wlf命令即可直接查询无需重复登录"
    msgg = msg11 + msg22
    counter_dict["counter"] = int(counters) + 1
    pickle.dump(counter_dict,open(user_file, 'wb'))
    counter_n.close()
    await User_info.send(Message(msgg))
    await User_info.finish(Message('一定要记得扫码完后先发/wlf bindsec哦！！'))

@bindsec.handle()
async def get_token(bot: Bot, event: Event):
    User_qq = int(event.get_user_id())
    counter_n = open(user_file,'rb')
    counter_dict = pickle.load(counter_n)
    id = counter_dict[f'{User_qq}_ids']
    post_body = {'client_type': 'qrcode', 'grant_type': 'client_credentials', 'client_id': id}
    Return_Token_url = 'https://dancedemo.shenghuayule.com/Dance/token'
    User_token_response_dic = requests.post(url=Return_Token_url, headers=get_headers, data=post_body).text
    User_token_response = json.loads(User_token_response_dic)
    User_Info_Url = f"https://dancedemo.shenghuayule.com/Dance/api/User/GetInfo?userId={User_token_response['userId']}"
    User_info_headers = {}
    counter_dict[f'{User_qq}_token'] = User_token_response['access_token']
    counter_dict[f'{User_qq}_id'] = User_token_response['userId']
    pickle.dump(counter_dict,open(user_file,'wb'))
    User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {User_token_response['access_token']}"
    try:
        User_info_response_dic = requests.get(
            url=User_Info_Url,
            headers=User_info_headers, stream=True, verify=False).text
        User_info_response = json.loads(User_info_response_dic)
    except Exception as ss:
        await bindsec.finish(Message(f'[ERROR]api无返回，请尝试重新登录\n{ss}'))
    User_id = User_info_response['UserID']
    User_Name = User_info_response['UserName']
    Music_Speed = User_info_response['MusicSpeed']
    Music_Score = User_info_response['MusicScore']
    Rank_Nation = User_info_response['RankNation']
    Combo_Percent = User_info_response['ComboPercent']
    Lv_ratio = User_info_response['LvRatio']
    Team_Id = User_info_response['TeamID']
    Team_Name = User_info_response['TeamName']
    msg1 = f'[CQ:at,qq={event.get_user_id()}]\n'
    msg2 = f"[CQ:image,file={User_info_response['HeadimgURL']}]"
    msg3 = f'User-INFO\n你的舞立方ID是-{User_id}\n机台昵称为-{User_Name}\n音符流速为{Music_Speed}速！\n积分有{Music_Score}！\n全国排名{Rank_Nation}!太强了\n全连率:{Combo_Percent}\n战力值有{Lv_ratio}点！\n你加入了{Team_Name}战队！(战队ID是{Team_Id})\nTip:如果反馈的不是您的账号信息，请晚些时候再自行私聊bot绑定'
    msg = msg2 + msg1 + msg3
    await bindsec.finish(Message(f'{msg}'))

@best.handle()
async def get_best(bot: Bot, event: Event):
    ops = []
    count = []
    User_qq = int(event.get_user_id())
    counter_n = open(user_file, 'rb')
    counter_dict = pickle.load(counter_n)
    try:
        user_id = counter_dict[f'{User_qq}_id']
        user_token = counter_dict[f'{User_qq}_token']
        print(user_id)
        print(user_token)
    except KeyError:
        await best.finish(Message(f'你还没有绑定哦！请先发送/help 查看舞立方模块绑定账号指令'))
    User_info_headers = {}
    # User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {user_token}"
    return_score_dict = []
    urls = ['https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=2&musicIDList=&machineType=0','https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=3&musicIDList=&machineType=0','https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=4&musicIDList=&machineType=0','https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=5&musicIDList=&machineType=0','https://dancedemo.shenghuayule.com/Dance/api/User/GetMyRank?musicIndex=6&musicIDList=&machineType=0']
    for get_type_url in urls:
        try:
            rea = requests.get(url=get_type_url, headers=User_info_headers, stream=True, verify=False).text
            return_score_dict.extend(json.loads(rea))
        except Exception as ss:
            await best.finish(Message(f'[ERROR]api无返回，请尝试重新登录\n{ss}'))
    for s in return_score_dict:
        if s['LvLength'] > 1:
            for an in range(s['LvLength']):
                op = {}
                op['Name'] = s['Name']
                op['lvIndex'] = s['lvIndex']
                op['Time'] = [s['Time'][an]]
                op['ComCount'] = [s['ComCount'][an]]
                op['MissCount'] = s['MissCount'][an]
                op['Time'] = [s['Time'][an]]
                op['Score'] = [s['Score'][an]]
                op['PercentScore'] = [s['PercentScore'][an]]
                op['MusicRank'] = [s['MusicRank'][an]]
                op['LvRecord'] = [s['LvRecord'][an]]
                ops.append(op)
            count.append(s)
    for co in count:
       return_score_dict.remove(co)
    return_score_dict.extend(ops)
    for coa in range(len(return_score_dict)):
        rankmaxa = return_score_dict[coa]['MusicRank'][0]+2
        rankmax = rankmaxa*100
        bfb = float(return_score_dict[coa]['PercentScore'][0]) / 100
        return_score_dict[coa]['RankScore'] = round(rankmax*bfb,2)
    for a in range(0,len(return_score_dict)-1):
        for b in range(0,len(return_score_dict)-1-a):
            if return_score_dict[b]['RankScore'] < return_score_dict[b+1]['RankScore']:
                return_score_dict[b],return_score_dict[b+1] = return_score_dict[b+1],return_score_dict[b]
    tophow = 1
    tophow2 = 1
    atry = 0
    send_end = []
    send_ena = ''
    User_info_headers = {}
    User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {user_token}"
    User_info_response_dic = requests.get(
            url=f'https://dancedemo.shenghuayule.com/Dance/api/User/GetInfo?userId={user_id}',
            headers=User_info_headers, stream=True, verify=False).text
    User_info_response = json.loads(User_info_response_dic)
    User_id = User_info_response['UserID']
    User_Name = User_info_response['UserName']
    Music_Speed = User_info_response['MusicSpeed']
    Music_Score = User_info_response['MusicScore']
    Rank_Nation = User_info_response['RankNation']
    Combo_Percent = User_info_response['ComboPercent']
    Lv_ratio = User_info_response['LvRatio']
    Team_Id = User_info_response['TeamID']
    Team_Name = User_info_response['TeamName']
    msg1 = f'[CQ:at,qq={event.get_user_id()}]\n'
    msg2 = f"[CQ:image,file={User_info_response['HeadimgURL']}]"
    msg3 = f'User-INFO\n你的舞立方ID是-{User_id}\n机台昵称为-{User_Name}\n音符流速为{Music_Speed}速！\n积分有{Music_Score}！\n全国排名{Rank_Nation}!太强了\n全连率:{Combo_Percent}\n战力值有{Lv_ratio}点！\n你加入了{Team_Name}战队！(战队ID是{Team_Id})\nTip:如果反馈的不是您的账号信息，请晚些时候再自行私聊bot绑定'
    msg = msg2 + msg1 + msg3
    send_end.extend(
        [

            MessageSegment.node_custom(
                user_id=2710022737,
                nickname="奶茶酱-AqualiteBot",
                content=Message(f'{msg}')
            )
        ]
    )
    for skp in return_score_dict:
        if tophow > 25:
            await best.send(Message('[INFO]舞立方-Best返回结果处理完毕，正在整合合并消息..'))
            break
        else:
            atry = 1
            headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{skp['lvIndex']}.jpg"
            headpic_ = f"C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{skp['lvIndex']}.jpg"
            if not os.path.exists(headpic_):
                headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/picnotfound.jpg"
            send_ena += f"#{tophow}\n{skp['Name']}（{skp['MusicRank'][0]}）\nID:{skp['lvIndex']}准确率：{skp['PercentScore'][0]}价值战力分：{skp['RankScore']}\n\n"
            tophow += 1
    send_end.extend(
                [
                    MessageSegment.node_custom(
                        user_id=2710022737,
                        nickname="奶茶酱-AqualiteBot",
                        content=Message(f'{send_ena}')
                    )
                ]
            )
    for sk in return_score_dict:
        if tophow2 > 25:
            break
        else:
            headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
            headpic_ = f"C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/{sk['lvIndex']}.jpg"
            if not os.path.exists(headpic_):
                headpic = f"file:///C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/DanceCube/jpg/jpg/picnotfound.jpg"
            score_msg = f"#{tophow2}\n曲名：{sk['Name']}\n(难度：{sk['MusicRank']})\n谱面ID:{sk['lvIndex']}\n总得分：{sk['Score']}\n最大连击:{sk['ComCount']}\nMiss数:{sk['MissCount']}\nACC/准确率：{sk['PercentScore']}\n全国排名：{sk['LvRecord']}({sk['Time']})\n价值战力分：{sk['RankScore']}"
            atry = 1
            tophow2 += 1
            send_end.extend(
                    [
                        MessageSegment.node_custom(
                            user_id=2710022737,
                            nickname="奶茶酱-AqualiteBot",
                            content=Message(f'[CQ:image,file={headpic}]\n{score_msg}')
                        )
                    ]
                )
    if atry == 1:
        await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
        await best.finish()
    await best.finish(Message(f"[Error]未知错误，定位于\n@best.handle()\nasync def get_best(bot: Bot, event: Event)\n请截图联系开发者(QQ1259891410)"))