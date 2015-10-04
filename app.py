#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

@app.route('/api/v1/music', methods=['GET'])
def signin_form():
    return '{"picUrl":"http://p4.music.126.net/URpfuCcFX9QE26UAnZl3nw==/68169720925571.jpg","url":"http://m2.music.126.net/pRAbB3ULXQWOhwxOX6u9Cg==/1119302837083616.mp3"}'

if __name__ == '__main__':
    app.run()
