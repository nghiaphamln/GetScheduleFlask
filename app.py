import json
from flask import Flask, jsonify
import getSchedule
import connectDB
app = Flask(__name__)


@app.route('/getInformation/<fb_id>')
def Information(fb_id):
    user = connectDB.getMSSV(fb_id)
    return getSchedule.getInformation(user)


@app.route('/getSchedule/<fb_id>')
def Schedule(fb_id):
    user = connectDB.getMSSV(fb_id)
    res = {
        'messages': [
            {
                'text': getSchedule.getSchedule(user)
            }
        ]
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run()
