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
        return_dict["Accestoken"] = self.access_token
        return_dict["Entitlements"] = self.entitlement
        return_dict["Userid"] = self.Sub
        return_dict["Region"] = self.Region
        return_dict["Name"] = self.Name + '#' + self.Tag
        return return_dict
def token(username,password):
    user = Auth(username, password)
    user.auth()
    result = user.get_userdata()
    pickle.dump(result,open('token.pickle','wb'))
    return result
def getshop():
    try:
        result = pickle.load(open('token.pickle','rb'))
    except FileNotFoundError:
        result = token('MilkTea2373','Nchgg2681964553')
    url_shop = f"https://pd.ap.a.pvp.net/store/v2/storefront/{result['Userid']}"
    headers = OrderedDict({"User-Agent": "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)",
                                           "Accept-Language": "en-US,en;q=0.9", "Accept": "application/json, text/plain, */*"})
    base_headers = {
            'User-Agent': "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)", 'Authorization': f"Bearer {result['Accestoken']}", 'X-Riot-Entitlements-JWT': result['Entitlements'],}
    headers.update(base_headers)
    hexget = json.loads(requests.get(url=url_shop,headers=headers).text)
    try:
        if hexget['httpStatus'] == 400:
            result = token('MilkTea2373','Nchgg2681964553')
            url_shop = f"https://pd.ap.a.pvp.net/store/v2/storefront/{result['Userid']}"
            headers = OrderedDict({"User-Agent": "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)",
                                           "Accept-Language": "en-US,en;q=0.9", "Accept": "application/json, text/plain, */*"})
            base_headers = {
            'User-Agent': "RiotClient/58.0.0.4640299.4552318 %s (Windows;10;;Professional, x64)", 'Authorization': f"Bearer {result['Accestoken']}", 'X-Riot-Entitlements-JWT': result['Entitlements'],}
            headers.update(base_headers)
            return requests.get(url=url_shop,headers=headers).text
    except KeyError:
        return hexget
shopdata_dict = getshop()
wepdict = pickle.load(open('weapon_data.pickle','rb'))
today_weapons = shopdata_dict["SkinsPanelLayout"]["SingleItemOffers"]
today_cost = shopdata_dict["SkinsPanelLayout"]["SingleItemStoreOffers"]
def update_skins_data():
    wepdict = json.loads(requests.get('https://valorant-api.com/v1/weapons?language=zh-TW').text)
    with open('weapon_data.pickle','wb') as s:
        pickle.dump(wepdict,s)
def secdict(today_weapons):
    count = 0
    for a in wepdict['data']:
        if a['uuid'] == today_weapons:
            return a
        else:
            print(wepdict['data'][count])
            for b in wepdict['data'][count]['skins']:
                for c in b['levels']:
                    if c['uuid'] == today_weapons:
                        return c
        count += 1
today_count = 0
sendstr = f'Valorant:Shop()\n----OUTPUT------\n'
for i in today_weapons:
    only_weapon_dict = secdict(i)
    sendstr += f"武器：{only_weapon_dict['displayName']}\n[CQ:image,file={only_weapon_dict['displayIcon']}]\n预览视频:{only_weapon_dict['streamedVideo']}\n售价:{today_cost[today_count]['Cost'].values()}\n-----我是分割线喵-----\n"
    today_count += 1
print(sendstr)
input()
