#!/usr/bin/env python3
from flask import Flask
from flask import request
import datetime
# import time
# import date



app = Flask(__name__)
now = datetime.date.today().strftime("%Y-%m-%d")



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
    else:
        name = "关忆北-宋冬野"
        picUrl = "http://p4.music.126.net/mPlr0GoQU2Wl_aZzIgIJ6A==/1984618488161733.jpg"
        url = "http://m2.music.126.net/o9EeErLrcN-uW-ogDRmJ3g==/5847202836624568.mp3"
    return '{"name":"'+name+'","picUrl":"'+picUrl+'","url":"'+url+'"}'


if __name__ == '__main__':
    app.run()
