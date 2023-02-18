from flask import Flask, jsonify, request
import requests


# creating a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):

        testData = {
            "data1": "D1",
            "data2": "D2",
            "data3": "D3",
            "data4": 1,
            "data5": 2,
            "data6": 3
        }

        data = requests.get(
            'https://api.thingspeak.com/channels/1832660/feeds.json').json()['feeds']
        length_of_Data = len(data)
        return jsonify({'data': data[length_of_Data-1], 'testdata': testData})


# driver function
if __name__ == '__main__':
    app.run(debug=True)
