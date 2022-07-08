import sys
import time
import requests
import random
import os
import threading

# 获取环境变量
env_dist = os.environ
_Cookie = env_dist.get("ksreadCookie")
_userid = env_dist.get("userid")

fast_mode = False
# fast_mode = True

Agent = 'Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.494 (rel;r) Mobile Safari/537.36 Yoda/2.8.3-rc1 ksNebula/10.4.10.3430 OS_PRO_BIT/64 MAX_PHY_MEM/7611 AZPREFIX/yz ICFO/0 StatusHT/32 TitleHT/44 AliBaichuan(2014_0_23537706@baichuan_h5_0.1.1/10.4.10.3430) AllowKsCallApp NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn evaSupported/false CT/0'


# 交流群 481276206
# 获取账号信息
def getInformation(cookie):
    url = "https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/basicInfo"
    headers = {'User-Agent': Agent, 'Accept': '*/*', "Connection": "close", 'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': cookie}
    rsp = requests.get(url=url, headers=headers).json()
    if rsp['result'] == 1:
        return str(rsp['data']['userData']['nickname'])
    else:
        print('获取账号信息错误！')
        print('错误信息: ' + str(rsp))


# 交流群 481276206
# 获取图书列表
def get_book_list(cookie):
    name = threading.current_thread().name
    url = "https://webapp.kuaishou.com/rest/r/novel/novel-list"
    data = {"DIANZHONG": random.randint(2, 10) * 10}
    headers = {
        "Host": "webapp.kuaishou.com",
        "Connection": "close",
        "Accept": "application/json",
        "User-Agent": Agent,
        "Content-Type": "application/json",
        "Origin": "https://webapp.kuaishou.com",
        "X-Requested-With": "com.kuaishou.nebula",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://webapp.kuaishou.com/activity/nebula/novelList?layoutType=4&bizContainer=ad",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }
    rsp = requests.post(url=url, headers=headers, json=data).json()
    if rsp["result"] == 1:
        return rsp["data"]
    else:
        print("账号：" + name + " 获取图书列表失败")
        print('错误信息: ' + str(rsp))


# 交流群 481276206
def red_book_pre(book_id, chapter_id, userid):
    url = "https://ksapi.zuanqianyi.com/api/v1/event/request_id"
    headers = {
        "Host": "ksapi.zuanqianyi.com",
        "accept": "application/json, text/plain, */*",
        "userid": userid,
        "user-agent": Agent,
        "content-type": "application/json",
        "origin": "https://lyzs.zuanqianyi.com",
        "x-requested-with": "com.kuaishou.nebula",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://lyzs.zuanqianyi.com/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {"type": 3, "book_id": book_id, "chapter_id": chapter_id}
    rsp = requests.post(url=url, headers=headers, json=data).json()


# 交流群 481276206
# 获取图书内容
def get_book_content(book_id, is_first: bool, chapter_id, userid):
    name = threading.current_thread().name
    url = "https://ksapi.zuanqianyi.com/api/v1/book/chapter"
    headers = {
        "Host": "ksapi.zuanqianyi.com",
        "accept": "application/json, text/plain, */*",
        "userid": userid,
        "user-agent": Agent,
        "content-type": "application/json",
        "origin": "https://lyzs.zuanqianyi.com",
        "x-requested-with": "com.kuaishou.nebula",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://lyzs.zuanqianyi.com/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {"is_first": 1, "book_id": book_id, "chapter_id": ""}
    if not is_first:
        data = {"book_id": book_id, "chapter_id": chapter_id}
    rsp = requests.post(url=url, headers=headers, json=data).json()
    if rsp["code"] == 0:
        return rsp["data"]
    else:
        print("账号：" + name + " 获取图书内容失败!")
        print('错误信息: ' + str(rsp))


# 交流群 481276206
def start_book_status(book_id, chapter_id, userid):
    name = threading.current_thread().name
    url = "https://ksapi.zuanqianyi.com/api/v1/book/task"
    headers = {
        "Host": "ksapi.zuanqianyi.com",
        "accept": "application/json, text/plain, */*",
        "userid": userid,
        "user-agent": Agent,
        "origin": "https://lyzs.zuanqianyi.com",
        "x-requested-with": "com.kuaishou.nebula",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://lyzs.zuanqianyi.com/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    params = {"book_id": book_id, "chapter_id": chapter_id}
    rsp = requests.get(url=url, headers=headers, params=params).json()
    if rsp["code"] == 0:
        return rsp["data"]["taskStatus"]
    else:
        print("账号：" + name + " 开始读书任务失败！")
        print('错误信息: ' + str(rsp))


# 交流群 481276206
# 读书进度上报
def book_event(body, userid):
    url = "https://ksapi.zuanqianyi.com/api/v1/event/push"
    headers = {
        "Host": "ksapi.zuanqianyi.com",
        "accept": "application/json, text/plain, */*",
        "userid": userid,
        "user-agent": Agent,
        "content-type": "application/json",
        "origin": "https://lyzs.zuanqianyi.com",
        "x-requested-with": "com.kuaishou.nebula",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://lyzs.zuanqianyi.com/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    rsp = requests.post(url=url, headers=headers, json=body).json()
    return rsp["code"]


# 交流群 481276206
# 阅读时间检查
def book_box_check(cookie):
    name = threading.current_thread().name
    url = "https://webapp.kuaishou.com/rest/r/novel/read-reward/info"
    headers = {
        "Host": "webapp.kuaishou.com",
        "Connection": "close",
        "Accept": "application/json",
        "User-Agent": Agent,
        "X-Requested-With": "com.kuaishou.nebula",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://webapp.kuaishou.com/activity/nebula/novelList?layoutType=4&bizContainer=ad",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }
    rsp = requests.get(url=url, headers=headers).json()
    if rsp["result"] == 1:
        data = rsp["data"]
        if data["buttonState"] == 0:
            book_box_open(cookie, data["readRewardConfigId"])


# 交流群 481276206
# 阅读时间奖励
def book_box_open(cookie, param):
    name = threading.current_thread().name
    url = "https://webapp.kuaishou.com/rest/r/novel/read-reward?readRewardConfigId=" + param
    headers = {
        "Host": "webapp.kuaishou.com",
        "Connection": "close",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.494 (rel;r) Mobile Safari/537.36 Yoda/2.8.3-rc1 ksNebula/10.4.10.3430 OS_PRO_BIT/64 MAX_PHY_MEM/7611 AZPREFIX/zw ICFO/0 StatusHT/32 TitleHT/44 AliBaichuan(2014_0_23537706@baichuan_h5_0.1.1/10.4.10.3430) AllowKsCallApp NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn evaSupported/false CT/0",
        "Origin": "https://webapp.kuaishou.com",
        "X-Requested-With": "com.kuaishou.nebula",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://webapp.kuaishou.com/activity/nebula/novelList?layoutType=4&bizContainer=ad",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }
    rsp = requests.post(url=url, headers=headers).json()
    if rsp["result"] == 1:
        data = rsp["data"]
        print("账号：" + name + " 获得阅读激励 " + str(data["coin"]) + " 个金币")
    else:
        print("账号：" + name + " 请求阅读时间奖励错误")
        print('错误信息: ' + str(rsp))


# 交流群 481276206
def book_read_reward(cookie):
    name = threading.current_thread().name
    url = "https://webapp.kuaishou.com/rest/r/novel/read-reward/info"
    headers = {
        "Host": "webapp.kuaishou.com",
        "Connection": "close",
        "Accept": "application/json",
        "User-Agent": Agent,
        "X-Requested-With": "com.kuaishou.nebula",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://webapp.kuaishou.com/activity/nebula/novelList?layoutType=4&bizContainer=ad",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }
    rsp = requests.get(url=url, headers=headers).json()
    if rsp["result"] == 1:
        print("账号：" + name + " 阅读获得金币 [" + str(rsp["data"]["coin"]) + "] 个")


# 交流群 481276206
# 读书任务总入口
def book(cookie, userid):
    name = threading.current_thread().name
    book_list = get_book_list(cookie)
    book_box_check(cookie)
    if type(book_list) == dict:
        book_list = book_list["novelInfos"]
        book = book_list[0]
        if book["taskState"] == "COMPLETE":
            global read_status
            read_status = 1
            print("账号：" + name + " 今日阅读任务已完成")
            return
        for b in range(len(book_list)):
            if int(book_list[b]["coin"]) > int(book["coin"]):
                book = book_list[b]
        start_sb = book["url"].find("bookId=")
        end = book["url"].find("&", start_sb + 7)
        book_id = book["url"][start_sb + 7: end]
        if_first = True
        # curChapter = 0
        # if book["curChapter"] != 0:
        #     if_first = False
        #     curChapter = book["curChapter"]
        content = get_book_content(book_id, if_first, "", userid)
        # 章节百分比
        chapter_percent = content["chapter_percent"]
        # 章节总字数
        chapter_word_count = content["chapter_word_count"]

        idx = content["idx"]
        # 本章id
        chapter_id = content["id"]
        # 下一章id
        next_id = content["next_id"]
        # 开始阅读时间
        if fast_mode:
            start_time = int(round(time.time() * 1000))
        else:
            start_time = int(round(time.time() * 1000)) - random.randint(5, 15) * 1000
        times = 0
        read_time = 0
        # 获取随机数增加百分比
        ran = random.randint(20, 40)
        start = int(time.time())
        body = {"book_id": book_id, "request_id": ""}
        i = 1
        print("账号：" + name + " 开始阅读: " + book["novelName"])
        while 1 == 1:
            times += 1
            book_box_check(cookie)
            red_book_pre(book_id, chapter_id, userid)
            i += 1
            if time.time() - start > (35 * 60):
                break
            read_time += random.randint(5, 15)
            if fast_mode:
                if times >= 20:
                    break
            else:
                time.sleep(28)
            body["chapter_id"] = chapter_id
            body["start_time"] = start_time
            body["event_type"] = 2
            body["read_time"] = read_time
            body["idx"] = idx
            if int(chapter_percent) + ran >= 100:
                body["chapter_percent"] = 100
                body["word_count"] = chapter_word_count
                chapter_id = next_id
                content = get_book_content(book_id, not if_first, next_id, userid)
                print("账号：" + name + " 开始阅读: " + book["novelName"] + " " + content["name"])
                # 章节百分比
                chapter_percent = 0
                # 章节总字数
                chapter_word_count = content["chapter_word_count"]

                idx = content["idx"]
                # 下一章id
                next_id = content["next_id"]
                # 开始阅读时间
                if fast_mode:
                    start_time = int(round(time.time() * 1000))
                else:
                    start_time = int(round(time.time() * 1000)) - random.randint(5, 15) * 1000
                read_time = 0
            else:
                body["chapter_percent"] = int(chapter_percent) + ran
                chapter_percent = body["chapter_percent"]
                body["word_count"] = round(int(chapter_word_count) / 100 * body["chapter_percent"])
            # 获取随机数增加百分比
            ran = random.randint(20, 40)
            code = book_event(body, userid)
            if code != 0:
                print("账号：" + name + " 阅读进度上报失败")


# 交流群 481276206
class BookThread(threading.Thread):
    def __init__(self, thread_id, name, cookie, userid):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.cookie = cookie
        self.userid = userid

    def run(self):
        print("账号：" + self.name + " 开始阅读")
        book(self.cookie, self.userid)
        print("账号：" + self.name + " 结束阅读")


# 交流群 481276206
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    cookies = _Cookie.split('&')
    userids = _userid.split('&')
    if len(cookies) != len(userids):
        print("cookie数量和userid数量不匹配！")
        sys.exit()
    for index, ck in enumerate(cookies):
        name = getInformation(ck)
        book_thread = BookThread(index, name, ck, userids[index])
        book_thread.start()
