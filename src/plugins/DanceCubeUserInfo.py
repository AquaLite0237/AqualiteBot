import asyncio
import requests
import json
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import os

User_info = on_keyword({'/wlf bind', '.wlf bind', '/w bind'}, priority=2)
User_Output = on_keyword({'/w', '/wlf', '.wlf'}, priority=5)
restart_counter = on_keyword({'/wlf restart_counter'},priority=1)

@restart_counter.handle()
async def restart(bot: Bot, event: Event):
    if int(event.get_user_id()) != 1259891410:
        await restart_counter.finish(Message('User_Error:您无权使用counter_restart命令'))
    else:
        lineup_to_files = open(
            'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\DanceCube\\counter.json', 'w')
        restart_dic = {}
        restart_dic['counter'] = '0'
        restart_tofile = json.dump(restart_dic)
        lineup_to_files.write(restart_tofile)
        lineup_to_files.close()
        await restart_counter.finish(Message('已将counter.json重置!'))

@User_info.handle()
async def get_qrcode(bot: Bot, event: Event):
    lineup_file = open(
        'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\DanceCube\\counter.json','r')
    lineup_to_file = open(
        'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\DanceCube\\counter.json', 'w')
    lineup_dic = json.load(lineup_file)
    lineup = lineup_dic['counter']
    await User_info.send(Message('已申请绑定QRCODE，请等待反馈二维码，如果当前有人在扫码请晚些时候绑定，以免造成混绑（即为自己绑定了别人的号），开发者仅准备了5个可用机台TOKEN，故不足以支撑太多人同时绑定，我也不知道令牌什么时候会失效，如果/wlf没反馈就是token失效，重新绑定即可!'))
    User_qq = int(event.get_user_id())
    ids_dic = ["yyQ6VxqMeIKJDzVmQuHtNAUGxHAgSxmR",
               "yyQ6VxqMeIL2hceWzZtdqsJxNf/hHSzH",
               "yyQ6VxqMeIL2hceWzZtdqtGq81Ru8pIE",
               "yyQ6VxqMeILLsdiEbWkbSnddhlyVGcNa",
               "yyQ6VxqMeILneEzfVyXPFVCZoOuXSoH3"]
    id_dic = {}
    if lineup == 4:
        id_dic[int(event.get_user_id())] = ids_dic[4]
        lineup_dic['counter'] = 0
        counter_to_file1 = json.dumps(lineup_dic)
        lineup_to_file.write(counter_to_file1)
        lineup_file.close()
        lineup_to_file.close()
    else:
        id_dic[int(event.get_user_id())] = ids_dic[lineup]
        lineup_to_data = lineup + 1
        lineup_dic['counter'] = lineup_to_data
        counter_to_file = json.dumps(lineup_dic)
        lineup_to_file.write(counter_to_file)
        lineup_file.close()
        lineup_to_file.close()
    id = id_dic[int(event.get_user_id())]
    get_url = f"https://dancedemo.shenghuayule.com/Dance/api/Common/GetQrCode?id={id}"
    get_return = requests.get(url=get_url, headers=get_headers).text
    json_dic = json.loads(get_return)
    qrcode_url = json_dic['QrcodeUrl']
    qrcode = f'[CQ:image,file={qrcode_url}]'
    msg11 = f'[CQ:at,qq={event.get_user_id()}]\n'
    msg22 = f"{qrcode}\n请在30秒内完成扫码登录，扫码完成后也请等待30秒反馈结果，后续只需要输入/wlf命令即可直接查询无需重复登录"
    msgg = msg11 + msg22
    await User_info.send(
        Message(msgg))
    post_body = {'client_type': 'qrcode', 'grant_type': 'client_credentials', 'client_id': id}
    wrrts = open(
        'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\DanceCube\\User_IDTOKEN.json',
        'w')
    wrrts_dic = {}
    wrrts_dic[f'{User_qq}_token'] = '0'
    wrrts_dic[f'{User_qq}_id'] = '0'
    wrrts_json = json.dumps(wrrts_dic)
    wrrts.write(wrrts_json)
    wrrts.close()
    await asyncio.sleep(40)
    Return_Token_url = 'https://dancedemo.shenghuayule.com/Dance/token'
    User_token_response_dic = requests.post(url=Return_Token_url, headers=get_headers, data=post_body).text
    User_token_response = json.loads(User_token_response_dic)
    User_Info_Url = f"https://dancedemo.shenghuayule.com/Dance/api/User/GetInfo?userId={User_token_response['userId']}"
    User_info_headers = {}
    wrts = open(
        'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\DanceCube\\User_IDTOKEN.json',
        'r')
    wrts_dic = json.load(wrts)
    User_TokentoFile = wrts_dic
    User_TokentoFile[f'{User_qq}_token'] = User_token_response['access_token']
    User_TokentoFile[f'{User_qq}_id'] = User_token_response['userId']
    User_file_json = json.dumps(User_TokentoFile)
    wrt = open(
        'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\DanceCube\\User_IDTOKEN.json',
        'w')
    wrt.write(User_file_json)
    wrt.close()
    wrts.close()
    User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {User_token_response['access_token']}"
    User_info_response_dic = requests.get(url=User_Info_Url, headers=User_info_headers).text
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
    msg3 = f'User-INFO\n你的舞立方ID是{User_id}\n机台昵称是{User_Name}！\n音符流速为{Music_Speed}速哦！\n积分有{Music_Score}！\n全国排名{Rank_Nation}!太强了\n全连率:{Combo_Percent}\n战力值有{Lv_ratio}点！\n你加入了{Team_Name}战队！(战队ID是{Team_Id})\nTip:如果反馈的不是您的账号信息，请晚些时候再自行私聊bot绑定'
    msg = msg2 + msg1 + msg3
    lineup -= 1
    await User_info.finish(Message(f'{msg}'))


@User_Output.handle()
async def info(bot: Bot, event: Event):
    wrt = open(
        'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\DanceCube\\User_IDTOKEN.json', 'r')
    User_file_dict = json.load(wrt)
    User_qq = int(event.get_user_id())
    UserId = User_file_dict[f'{User_qq}_id']
    UserToken = User_file_dict[f'{User_qq}_token']
    User_Info_Url = f"https://dancedemo.shenghuayule.com/Dance/api/User/GetInfo?userId={UserId}"
    User_info_headers = {}
    User_info_headers["Connection"] = "Keep-Alive"
    User_info_headers[
        "user-agent"] = "Mozilla/5.0 (Linux; Android 8.1.0; V1818T Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/28.0)"
    User_info_headers["Content-Type"] = "application/json;charset=UTF-8"
    User_info_headers["Authorization"] = f"Bearer {UserToken}"
    User_info_response_dic = requests.get(url=User_Info_Url, headers=User_info_headers).text
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
    msg3 = f'User-INFO\n你的舞立方ID是{User_id}\n机台昵称是{User_Name}！\n音符流速为{Music_Speed}速哦！\n积分有{Music_Score}！\n全国排名{Rank_Nation}!太强了\n全连率:{Combo_Percent}\n战力值有{Lv_ratio}点！\n你加入了{Team_Name}战队！(战队ID是{Team_Id})'
    msg = msg2 + msg1 + msg3
    await User_info.finish(Message(f'{msg}'))


get_headers = {
    'User-Agent': "Mozilla/5.0 (Windows  NT 10.0; Win64; x64)pyh AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 'content-type': 'application/x-www-form-urlencoded'"
}
