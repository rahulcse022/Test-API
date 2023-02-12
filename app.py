from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):

        data = {
            "data1": "D1",
            "data2": "D2",
            "data3": "D3",
            "data4": 1,
            "data5": 2,
            "data6": 3
        }
        return jsonify(data)


@app.route('/home/<int:num>', methods=['GET'])
def disp(num):

    return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
