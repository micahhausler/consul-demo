import json
from time import sleep

import requests
from flask import Flask
app = Flask(__name__)

BASE_CONSUL_URL = 'http://consul1:8500'

PORT = 8080

@app.route('/')
def home():
    return 'Hello World!'


@app.route('/health')
def hello_world():
    data = {
        'status': 'healthy'
    }
    return json.dumps(data)


def register():
    url = BASE_CONSUL_URL + '/v1/agent/service/register'
    data = {
        'name': 'Python App',
        'address': 'app1',
        'check': {
            'http': 'http://app1:{port}/health'.format(port=PORT),
            'interval': '10s'
        }
    }
    res = requests.put(
        url,
        data=json.dumps(data)
    )
    return res.text


if __name__ == '__main__':
    sleep(8)
    print(register())
    app.debug = True
    app.run(host="0.0.0.0", port=PORT)
