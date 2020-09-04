from flask import Flask, jsonify
from module.bypasscaptcha import GetCookies
from module.getdata import getInformation, getSchedule

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to my API'

@app.route('/getInformation/<user>')
def Information(user):
    res = {
        'messages': [
            {
                'text': getInformation(user)
            }
        ]
    }
    return jsonify(res)

@app.route('/getSchedule/<user>')
def Schedule(user):
    res = {
        'messages': [
            {
                'text': getSchedule(user)
            }
        ]
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run()
