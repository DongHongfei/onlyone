#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

@app.route('/api/v1/music', methods=['GET'])
def signin_form():
    return '{"picUrl":"http://p3.music.126.net/ugqgjlAdvXPgX4FGFo2eXw==/75866302334121.jpg","url":"http://m2.music.126.net/oZn_gq3WK9amlixhhk1l7g==/1213860837072515.mp3"}'

if __name__ == '__main__':
    app.run()
