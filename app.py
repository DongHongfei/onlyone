#!/usr/bin/env python3
from flask import Flask
from flask import request
import datetime
# import sqlite3
# import time
# import date



app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

@app.route('/api/v1/music', methods=['GET'])
def getMusic():
    # 2015-09-26 男孩别哭-海龟先生
    # 2015-09-27 九月-许巍
    # 2015-09-28 回来-指南针
    # 2015-09-29 饿狼传说-张学友
    # 2015-10-03 一个人-玲凯/吴青峰

    now = datetime.date.today().strftime("%Y-%m-%d")
    if now == '2015-10-05':
        name = "没有人像我一样-龙宽九段";
        picUrl = "http://p4.music.126.net/URpfuCcFX9QE26UAnZl3nw==/68169720925571.jpg"
        url = "http://m2.music.126.net/pRAbB3ULXQWOhwxOX6u9Cg==/1119302837083616.mp3"
    elif now == '2015-10-06':
        name = "你的背包-丽江小倩"
        picUrl = "http://p4.music.126.net/PPwLHrZ7RRFsnEmObmU3AQ==/5869193069226226.jpg"
        url = "http://m2.music.126.net/lAKhuR_7jkBWNL5YpNWeXA==/8900546626964174.mp3"
    elif now == '2015-10-07':
        name = "关忆北-宋冬野"
        picUrl = "http://p4.music.126.net/mPlr0GoQU2Wl_aZzIgIJ6A==/1984618488161733.jpg"
        url = "http://m2.music.126.net/o9EeErLrcN-uW-ogDRmJ3g==/5847202836624568.mp3"
    elif now == '2015-10-10':
        name = "Don't Break My Heart-窦唯"
        picUrl = "http://p4.music.126.net/KLkcYXJpVzH_9AreV--Cdg==/31885837217563.jpg"
        url = "http://m2.music.126.net/e0r4q80SPA5yXEMvV4am7A==/1106108697551466.mp3"
    elif now == '2015-10-11':
        name = "新房客-王菲"
        picUrl = "http://p4.music.126.net/4yDIpCMllhrRUFjE1pi7Bw==/50577534889997.jpg"
        url = "http://m2.music.126.net/3VsnsMVtyk0fUluMZ-x1TQ==/1157785744056740.mp3"
    elif now == '2015-10-12':
        name = "立秋-筠子"
        picUrl = "http://p3.music.126.net/xYTPXlkkP-QTsbT7WSmTkQ==/835628837110140.jpg"
        url = "http://m2.music.126.net/o9EeErLrcN-uW-ogDRmJ3g==/5847202836624568.mp3"
    elif now == '2015-10-13':
        name = "关忆北-宋冬野"
        picUrl = "http://p4.music.126.net/mPlr0GoQU2Wl_aZzIgIJ6A==/1984618488161733.jpg"
        url = "http://m2.music.126.net/o9EeErLrcN-uW-ogDRmJ3g==/5847202836624568.mp3"
    elif now == '2015-10-14':
        name = "丢-布衣乐队"
        picUrl = "http://p3.music.126.net/M9sYBSiFkH3WMrBBTWupAw==/3121513511336820.jpg"
        url = "http://m2.music.126.net/h4CcEI2XELCm3leKerMrKg==/1989016534680963.mp3"
    elif now == '2015-11-01':
        name = "怎么说我不爱你-萧敬腾"
        picUrl = "http://p4.music.126.net/kM0bdmhoJwtjx6PV5A3T1A==/91259465118157.jpg"
        url = "http://m2.music.126.net/wywdTcFevEagyJqlmJ9wNg==/3290838302033348.mp3"
    elif now == '2015-11-02':
        name = "倔强的青春-鸿水"
        picUrl = "http://p4.music.126.net/FUCuUujisZUUBuhAOuINEg==/5994537395235983.jpg"
        url = "http://m2.music.126.net/DtSFrw8thQruPl-ybmIGTw==/5974746185933269.mp3"
    elif now == '2015-11-03':
        name = "勿忘心安-张杰"
        picUrl = "http://p3.music.126.net/_3rFFR1Mv663xtSIO_mvEA==/119846767433726.jpg"
        url = "http://m2.music.126.net/WO6QEqFtgO47BNuzQ4u7ow==/5801023348300892.mp3"
    else:
        name = "给郁结的诗-小安"
        picUrl = "http://p3.music.126.net/esFr50QMkuZuC5AcOKo8tw==/97856534884250.jpg"
        url = "http://m2.music.126.net/gFswvDGmLVWh7tKnqoakAg==/1998912139326550.mp3"
    return '{"name":"'+name+'","picUrl":"'+picUrl+'","url":"'+url+'"}'


if __name__ == '__main__':
    app.run()
