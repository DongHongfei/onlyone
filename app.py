#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

@app.route('/api/v1/music', methods=['GET'])
def signin_form():
    return '{"picUrl":"http://p3.music.126.net/tOhom1sERa_KgoA78Pqa1Q==/2423323627633522.jpg","url":"http://m2.music.126.net/JNMhi2SCp9ief3mHmKqMjA==/3294136836885992.mp3"}'

if __name__ == '__main__':
    app.run()
