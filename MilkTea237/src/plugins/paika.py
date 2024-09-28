import pickle
from nonebot.plugin import on_command,on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
import os
import datetime as datetime
import time

checker = on_command('j',aliases={'pk','排卡板'})
countController = on_message(priority=90)
addShop = on_command('/addmai')
global DefaultPath
DefaultPath = f'MilkTea237\\data\\Aqualite\\maimaiPlayerList\\'


class API(object):
    def getPlayerList(groupid):
        global DefaultPath
        try:
            with open(f'{DefaultPath}{groupid}shopList.pickle','rb') as datafile:
                data = pickle.load(datafile)
                print(data)
                datafile.close()
                return_msg = ''
                try:
                    if data['rec_updatetime'] != datetime.date.today():
                        data['recent'] = ['每日自动清卡=0']
                except:
                    pass
                for shop in data['shoplist']:
                    times = shop+'time'
                    print(times)
                    rec_msg = ''
                    counter = 0
                    for cdc in reversed(data['recent']):
                        if cdc[0] == shop:
                            if counter == 5:
                                break
                            rec_msg += cdc.replace(shop,'') + '\n'
                            counter += 1
                    return_msg += f"{shop}：{data[shop]}卡\n{rec_msg}\n更新于：{data[times]}\n-------------\n"
                return {
                    'msg': return_msg,
                    'status':True
                    }
        except Exception as err:
            return {
                'status':False,
                'msg':err
            }
    
    def adminList(groupid):
        global DefaultPath
        try:
            with open(f'{DefaultPath}{groupid}admins.pickle','rb') as datafile:
                data = pickle.load(datafile)
                datafile.close()
                return data
        except FileNotFoundError:
            with open(f'{DefaultPath}{groupid}admins.pickle','wb') as datafile:
                pickle.dump([],datafile)
                datafile.close()
                return []
    
    def todayLog(msg):
        global DefaultPath
        today = datetime.date.today()
    
    def getGroupShop(groupid):
        global DefaultPath
        try:
            with open(f'{DefaultPath}{groupid}shopList.pickle','rb') as read:
                data = pickle.load(read)
                read.close()
                return data
        except:
            with open(f'{DefaultPath}{groupid}shopList.pickle','wb') as read:
                defaultshop = {
                    'shoplist':[]
                }
                pickle.dump(defaultshop,read)
                read.close()
                return defaultshop


@addShop.handle()
async def addshopfunc(bot: Bot, event: GroupMessageEvent):
    '''getAdmin:list = API.adminList(event.group_id)
    userid = int(event.get_user_id())
    for id in getAdmin:
        if id == userid:'''
    user:str = event.get_user_id()
    if user == '1259891410':
        msg = str(event.get_message())
        shop = msg.replace('/addmai','',1)
        groupid = event.group_id
        o_data = API.getGroupShop(groupid)
        with open(f'{DefaultPath}{groupid}shopList.pickle','wb') as new:
            o_data[shop] = 0
            o_data['shoplist'].append(shop)
            o_data[shop+'time'] = time.asctime()
            pickle.dump(o_data,new)
            new.close()


@countController.handle()
async def countCtlfunc(bot: Bot, event: GroupMessageEvent):
    msg = str(event.get_message())
    groupid = event.group_id
    user:str = event.get_user_id()
    shop = msg[0]
    data = API.getGroupShop(groupid)
    try:
        data[shop]
    except:
        await countController.finish()
    data['time'] = time.asctime()
    try:
        data['recent']
    except:
        data['recent'] = []
    if len(msg)<3:
        await countController.finish()
    if msg[1] == '=' or msg[1] == '=':
        countNum = msg.replace(msg[0],'').replace(msg[1],'')
        try:
            int(countNum)
        except Exception as err:
            await countController.finish(Message('[ERROR]键入参数出错？\n示例:偶+1  偶-1  偶=10\n\n{err}'))
        try:
            if data['rec_updatetime'] != datetime.date.today():
                data['recent'] = ['每日自动清卡=0']
        except:
            pass
        data[shop] = countNum
        data[shop+'time'] = time.asctime()
        data['recent'].append(f'{msg[0]}{user}{msg[1]}{countNum}')
        data['recent'] = data['recent']
        data['rec_updatetime'] = datetime.date.today()
        with open(f'{DefaultPath}{groupid}shopList.pickle','wb') as read:
            pickle.dump(data,read)
            read.close()
        await countController.finish(Message(f"修改成功！\n{API.getPlayerList(groupid)['msg']}"))
    elif msg[1] == '+' or msg[1] == '+':
        countNum = msg.replace(msg[0],'').replace(msg[1],'')
        try:
            int(countNum)
        except Exception as err:
            await countController.finish(Message('[ERROR]键入参数出错？\n示例:偶+1  偶-1  偶=10\n\n{err}'))
        try:
            if data['rec_updatetime'] != datetime.date.today():
                data['recent'] = ['每日自动清卡=0']
        except:
            pass
        data[shop] = int(data[shop]) + int(countNum)
        data[shop+'time'] = time.asctime()
        data['recent'].append(f'{msg[0]}{user}{msg[1]}{countNum}')
        data['rec_updatetime'] = datetime.date.today()
        with open(f'{DefaultPath}{groupid}shopList.pickle','wb') as read:
            pickle.dump(data,read)
            read.close()
        await countController.finish(Message(f"修改成功！\n{API.getPlayerList(groupid)['msg']}"))
    elif msg[1] == '-' or msg[1] == '-':
        countNum = msg.replace(msg[0],'').replace(msg[1],'')
        try:
            int(countNum)
        except Exception as err:
            await countController.finish(Message(f'[ERROR]键入参数出错？\n示例:偶+1  偶-1  偶=10\n\n{err}'))
        try:
            if data['rec_updatetime'] != datetime.date.today():
                data['recent'] = ['每日自动清卡=0']
        except:
            pass
        data[shop] = int(data[shop]) - int(countNum)
        data[shop+'time'] = time.asctime()
        data['recent'].append(f'{msg[0]}{user}{msg[1]}{countNum}')
        data['rec_updatetime'] = datetime.date.today()
        with open(f'{DefaultPath}{groupid}shopList.pickle','wb') as read:
            pickle.dump(data,read)
            read.close()
        await countController.finish(Message(f"修改成功！\n{API.getPlayerList(groupid)['msg']}"))
    else:
        await countController.finish()

        
@checker.handle()
async def checkerfunc(bot: Bot, event: GroupMessageEvent):
    paikadata = API.getPlayerList(event.group_id)
    if paikadata['status'] == False:
        await checker.finish(Message(f"[ERROR]{paikadata['msg']}\n请联系开发者1259891410"))
    await checker.finish(Message(f"#群{str(event.group_id)}排卡板#\n{paikadata['msg']}"))


if __name__ == '__main__':
    if not os.path.exists(DefaultPath):
        os.makedirs(DefaultPath)