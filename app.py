#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '{"picUrl":"http://p4.music.126.net/boJMW-80CcGhrPIG7Nsaow==/82463372095702.jpg?param=34x34","url":"http://m2.music.126.net/li9U8WUTYs0MityAeW9zsQ==/1130297953361132.mp3"}'

@app.route('/api/v1/music', methods=['GET'])
def signin_form():
    return '{"picUrl":"http://p4.music.126.net/boJMW-80CcGhrPIG7Nsaow==/82463372095702.jpg?param=34x34","url":"http://m2.music.126.net/li9U8WUTYs0MityAeW9zsQ==/1130297953361132.mp3"}'

if __name__ == '__main__':
    app.run()
