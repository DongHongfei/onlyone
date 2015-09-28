#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

@app.route('/api/v1/music', methods=['GET'])
def signin_form():
    return '{"picUrl":"http://p4.music.126.net/ZKChSpAz_3ObVWFlu-0jQQ==/120946279069890.jpg","url":"http://m2.music.126.net/zdQsjFiPMADeMck58AVSLA==/1238050092909830.mp3"}'

if __name__ == '__main__':
    app.run()
