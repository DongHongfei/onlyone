#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

@app.route('/api/v1/music', methods=['GET'])
def signin_form():
    return '{"picUrl":"http://p3.music.126.net/h_NkuFQf_IbEqnCjjgnOSw==/31885837217550.jpg","url":"http://m2.music.126.net/TRzcBB-BcpdXiEZEhbz3iw==/1218258883584418.mp3"}'

if __name__ == '__main__':
    app.run()
