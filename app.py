#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

@app.route('/api/v1/music', methods=['GET'])
def signin_form():
    return '{"picUrl":"http://p4.music.126.net/qLBbX25yQf_z_bIVqW8FxQ==/5507453743656093.jpg","url":"http://thirdyires.imusicapp.cn/res/thirdparty/2044/mp3/00/00/14/2044000014010800.mp3"}'

if __name__ == '__main__':
    app.run()
