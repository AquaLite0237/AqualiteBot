from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.adapters.onebot.v11.message import Message
import json
import pickle
import ssl
from typing import Any
from collections import OrderedDict
import requests
from requests.adapters import HTTPAdapter
import pandas
from re import compile
from colorama import Fore
import time
import datetime as datetime
import os
PATH = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\'
if not os.path.exists(PATH):
    os.makedirs(PATH)
userdict_pathh = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICTaddpath.pickle'
if not os.path.exists(PATH):
    default = {}
    pickle.dump(default,open(userdict_pathh,'wb'))


CIPHERS = [
    'ECDHE-ECDSA-AES128-GCM-SHA256',
    'ECDHE-ECDSA-CHACHA20-POLY1305',
    'ECDHE-RSA-AES128-GCM-SHA256',
    'ECDHE-RSA-CHACHA20-POLY1305',
    'ECDHE+AES128',
    'RSA+AES128',
    'ECDHE+AES256',
    'RSA+AES256',
    'ECDHE+3DES',
    'RSA+3DES'
]


class URLS:
    AUTH_URL = "https://auth.riotgames.com/api/v1/authorization"
    REGION_URL = 'https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant'
    VERIFED_URL = "https://email-verification.riotgames.com/api/v1/account/status"
    ENTITLEMENT_URL = 'https://entitlements.auth.riotgames.com/api/token/v1'
    USERINFO_URL = "https://auth.riotgames.com/userinfo"


class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *a: Any, **k: Any) -> None:
        c = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        c.set_ciphers(':'.join(CIPHERS))
        k['ssl_context'] = c
        return super(SSLAdapter, self).init_poolmanager(*a, **k)


class Auth:
    def __init__(self, username, password, session=None):
        self.username = username
        self.password = password
        self.session = requests.Session() if not session else session
        self.session.headers = OrderedDict({"User-Agent": "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)",
                                           "Accept-Language": "en-US,en;q=0.9", "Accept": "application/json, text/plain, */*"})
        self.session.mount('https://', SSLAdapter())
        self.authed = False
        self.MFA = False
        self.remember = False

    def auth(self, MFACode=''):
        tokens = self.authorize(MFACode)
        if 'x' in tokens:
            return
        self.authed = True
        self.access_token = tokens[0]
        self.id_token = tokens[1]

        self.base_headers = {
            'User-Agent': "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)", 'Authorization': f'Bearer {self.access_token}', }
        self.session.headers.update(self.base_headers)

        self.entitlement = self.get_entitlement_token()
        self.emailverifed = self.get_emailverifed()

        userinfo = self.get_userinfo()
        self.Sub = userinfo[0]
        self.Name = userinfo[1]
        self.Tag = userinfo[2]
        self.creationdata = userinfo[3]
        self.typeban = userinfo[4]
        self.Region_headers = {'Content-Type': 'application/json',
                               'Authorization': f'Bearer {self.access_token}'}
        self.session.headers.update(self.Region_headers)
        self.Region = self.get_Region()
        # self.p = self.print()

    def authorize(self, MFACode=''):
        data = {"acr_values": "urn:riot:bronze", "claims": "", "client_id": "riot-client", "nonce": "oYnVwCSrlS5IHKh7iI16oQ",
                "redirect_uri": "http://localhost/redirect", "response_type": "token id_token", "scope": "openid link ban lol_region", }
        data2 = {"language": "en_US", "password": self.password,
                 "remember": "true", "type": "auth", "username": self.username, }

        r = self.session.post(url=URLS.AUTH_URL, json=data)

        r = self.session.put(url=URLS.AUTH_URL, json=data2)
        data = r.json()
        if "access_token" in r.text:
            pattern = compile(
                'access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
            data = pattern.findall(data['response']['parameters']['uri'])[0]
            token = data[0]
            token_id = data[1]
            return [token, token_id]

        elif "auth_failure" in r.text:
            print(
                F"{Fore.RED}[NOT EXIST] {Fore.RESET} {self.username}:{self.password}")
            return "x"

        elif 'rate_limited' in r.text:
            print(
                F"{Fore.YELLOW}[RATE] {Fore.RESET} {self.username}:{self.password}")
            time.sleep(40)
            return 'x'
        elif self.MFA:
            # ver_code = input(F'{Fore.GREEN}2FA Auth Enabled{Fore.RESET}. Enter the verification code: \n')
            if __name__ == '__main__':
                ver_code = input('Please input your ver code: ')
            else:
                ver_code = MFACode
            authdata = {
                'type': 'multifactor',
                'code': ver_code,
                "rememberDevice": self.remember,
            }
            r = self.session.put(url=URLS.AUTH_URL, json=authdata)
            data = r.json()
            if "access_token" in r.text:
                pattern = compile(
                    'access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
                data = pattern.findall(
                    data['response']['parameters']['uri'])[0]
                token = data[0]
                token_id = data[1]
                return [token, token_id]

            elif "auth_failure" in r.text:
                # banned (?)
                print(
                    F"{Fore.RED}[ERROR] {Fore.RESET} {self.username}:{self.password}")
            else:
                print(
                    F"{Fore.RED}[ERROR] {Fore.RESET} {self.username}:{self.password}")
        else:
            self.MFA = True
            return 'x'

    def get_entitlement_token(self):
        r = self.session.post(URLS.ENTITLEMENT_URL, json={})
        entitlement = r.json()['entitlements_token']
        return entitlement

    def get_emailverifed(self):
        r = self.session.get(url=URLS.VERIFED_URL, json={})
        Emailverifed = r.json()["emailVerified"]
        return Emailverifed

    def get_userinfo(self):
        r = self.session.get(url=URLS.USERINFO_URL, json={})
        data = r.json()
        Sub = data['sub']
        data1 = data['acct']
        Name = data1['game_name']
        Tag = data1['tag_line']
        time4 = data1['created_at']
        time4 = int(time4)
        Createdat = pandas.to_datetime(time4, unit='ms')
        str(Createdat)
        data2 = data['ban']
        data3 = data2['restrictions']
        typeban = None
        if data3 != []:
            for x in data3:
                type = x['type']
                if type == "TIME_BAN":
                    for y in data3:
                        lol = y['dat']
                        exeperationdate = lol['expirationMillis']
                        time1 = exeperationdate
                        time1 = int(time1)
                        Exp = pandas.to_datetime(
                            time1, unit='ms', errors="ignore")
                        str(Exp)
                    typeban = "TIME_BAN"
                if type == "PERMANENT_BAN":
                    typeban = "PERMANENT_BAN"
        if data3 == [] or "PBE_LOGIN_TIME_BAN" in data3 or "LEGACY_BAN" in data3:
            typeban = "None"
        return [Sub, Name, Tag, Createdat, typeban]

    def get_Region(self):
        json = {"id_token": self.id_token}
        r = self.session.put(
            'https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant', json=json)
        data = r.json()
        Region = data['affinities']['live']
        return Region

    def get_userdata(self):
        return_dict = {}
        try:
            return_dict["Accestoken"] = self.access_token
            return_dict["Entitlements"] = self.entitlement
            return_dict["Userid"] = self.Sub
            return_dict["Region"] = self.Region
            return_dict["Name"] = self.Name + '#' + self.Tag
            return return_dict
        except:
            return False
def token(user):
    userdict_path = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICT.pickle'
    userdict = pickle.load(open(userdict_path,'rb'))
    username = userdict[user][0]
    password = userdict[user][1]
    users = Auth(username, password)
    users.auth()
    result = users.get_userdata()
    if result == False:
        return False
    val_path = "C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/Valroant/" + str(user) + '.pickle'
    pickle.dump(result,open(val_path,'wb'))
    return result
def getshop(user):
    result = []
    try:
        val_path = "C:/Users/Administrator/Desktop/MilkTea237/MilkTea237/data/Aqualite/Valroant/" + str(user) + '.pickle'
        result.append(pickle.load(open(val_path,'rb')))
    except FileNotFoundError:
        result.append(token(user))
    try:
        dictadd = pickle.load(open(f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICTaddpath.pickle','rb'))
        dictadd[user]
    except:
        pass
    """ if result == False:
        return False """
    return_list = []
    for result in result:
        url_shop = f"https://pd.ap.a.pvp.net/store/v2/storefront/{result['Userid']}"
        headers = OrderedDict({"User-Agent": "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)",
                                           "Accept-Language": "en-US,en;q=0.9", "Accept": "application/json, text/plain, */*"})
        base_headers = {
            'User-Agent': "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)", 'Authorization': f"Bearer {result['Accestoken']}", 'X-Riot-Entitlements-JWT': result['Entitlements'],}
        headers.update(base_headers)
        hexget = json.loads(requests.get(url=url_shop,headers=headers).text)
        try:
            if hexget['httpStatus'] == 400:
                result = token(user)
                url_shop = f"https://pd.ap.a.pvp.net/store/v2/storefront/{result['Userid']}"
                headers = OrderedDict({"User-Agent": "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)",
                                           "Accept-Language": "en-US,en;q=0.9", "Accept": "application/json, text/plain, */*"})
                base_headers = {
                'User-Agent': "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)", 'Authorization': f"Bearer {result['Accestoken']}", 'X-Riot-Entitlements-JWT': result['Entitlements'],}
                headers.update(base_headers)
                return_list.append(json.loads(requests.get(url=url_shop,headers=headers).text))
        except KeyError:
            return_list.append(hexget)
    return return_list
def update_skins_data():
    wepdict = json.loads(requests.get('https://valorant-api.com/v1/weapons?language=zh-TW').text)
    aofile = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\weapon_data.pickle'
    with open(aofile,'wb') as s:
        pickle.dump(wepdict,s)
    return True
def secdict(today_weapons):
    aofile = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\weapon_data.pickle'
    wepdict = pickle.load(open(aofile,'rb'))
    count = 0
    for a in wepdict['data']:
        if a['uuid'] == today_weapons:
            return a
        else:
            for b in wepdict['data'][count]['skins']:
                for c in b['levels']:
                    if c['uuid'] == today_weapons:
                        return c
        count += 1
#--------------------------------BOT------------------------------
update_data = on_command('/valorant update_data',aliases={'/v upd','/val update_data'})
getvalshop = on_command('/val shop',aliases={'/v shop','瓦商店','/valorant shop'})
valbind = on_command('/valbind')
valadd = on_command('/valadd')
valclear = on_command("/val clear")
load_data = on_command('/val loaddata')
@update_data.handle()
async def cbreply(bot: Bot, event: Event):
    user = int(event.get_user_id())
    if user == 1259891410:
        pass
    else:
        await update_data.finish(f'[ERROR]{user}无权使用PLUGIN:Valorant:MASTER-COMMAND</valorant update_data>')
    if update_skins_data():
        await update_data.finish(Message('瓦数据包更新完成拉'))
@load_data.handle()
async def cbreply(bot: Bot, event: Event):
    user = int(event.get_user_id())
    if user == 1259891410:
        pass
    else:
        await load_data.finish(f'[ERROR]{user}无权使用PLUGIN:Valorant:MASTER-COMMAND</val loaddata>')
    userdict_pathold = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICT.pickle'
    olddict = pickle.load(open(userdict_pathold,'rb'))
    await load_data.finish(Message(str(olddict)))
@valbind.handle()
async def cbreply(bot: Bot, event: Event):
    user = int(event.get_user_id())
    userdict_pathold = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICT.pickle'
    userdict_path = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICT.pickle'
    inputdata = str(event.get_message()).replace('/valbind','') + '#'
    datalist = []
    strapd = ''
    for t in inputdata:
        if t == '#':
            datalist.append(strapd.replace('#','',1))
            strapd = ''
        strapd += t
    dicts = {}
    olddict = pickle.load(open(userdict_pathold,'rb'))
    dicts.update(olddict)
    dicts[user] = datalist
    senddict = {}
    senddict[user] = datalist
    pickle.dump(dicts,open(userdict_path,'wb'))
    await valbind.finish(Message(f"{senddict}\n绑定成功~"))
@valadd.handle()
async def cbreply(bot: Bot, event: Event):
    user = int(event.get_user_id())
    userdict_pathold = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICTaddpath.pickle'
    userdict_path = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICTaddpath.pickle'
    inputdata = str(event.get_message()).replace('/valadd','') + '#'
    datalist = []
    strapd = ''
    for t in inputdata:
        if t == '#':
            datalist.append(strapd.replace('#','',1))
            strapd = ''
        strapd += t
    dicts = {}
    olddict = pickle.load(open(userdict_pathold,'rb'))
    dicts.update(olddict)
    dicts[user] = datalist
    pickle.dump(dicts,open(userdict_path,'wb'))
    await valbind.finish(Message(f"{dicts}\n账号添加成功~"))
@getvalshop.handle()
async def cbreply(bot: Bot, event: Event):
    user = int(event.get_user_id())
    send_end = []
    try:
        dicta = pickle.load(open('C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\Valroant\\USERDICT.pickle','rb'))
        dicta[user]
    except KeyError:
        await getvalshop.finish(Message('你还没有绑定账号哦！请发送/help后进入帮助文档，自行翻阅Valorant模块绑定指令~'))
    await getvalshop.send(Message('收到请求啦，请稍后...\n若超过30秒无响应请联系开发者1259891410排查问题喵\n如果你绑定了更多账号，则等待时间请乘以绑定个数'))
    shopdata_dict = getshop(user)
    for shopdata_dict in shopdata_dict:
        if shopdata_dict == False:
            send_end.extend(
                [
                    MessageSegment.node_custom(
                        user_id=2710022737,
                        nickname="奶茶酱-AqualiteBot",
                        content=Message('[ERROR]登录失败啦...可能是因为账号密码错误或账号开启了二次验证，请前往Riot关闭二次验证')
                    )
                ]
            )
            continue
        today_weapons = shopdata_dict["SkinsPanelLayout"]["SingleItemOffers"]
        today_cost = shopdata_dict["SkinsPanelLayout"]["SingleItemStoreOffers"]
        today = datetime.date.today()
        sendstr = f'Valorant:Shop({today})\n----OUTPUT------\n'
        today_count = 0
        for i in today_weapons:
            only_weapon_dict = secdict(i)
            sendstr += f"武器：{only_weapon_dict['displayName']}\n[CQ:image,file={only_weapon_dict['displayIcon']}]\n预览视频:{only_weapon_dict['streamedVideo']}\n售价:{today_cost[today_count]['Cost'].values()}\n-----我是分割线喵-----\n"
            today_count += 1
        send_end.extend(
                [
                    MessageSegment.node_custom(
                        user_id=2710022737,
                        nickname="奶茶酱-AqualiteBot",
                        content=Message(sendstr)
                    )
                ]
            )
    await bot.send_group_forward_msg(group_id=event.group_id, messages=send_end)
    await getvalshop.finish()