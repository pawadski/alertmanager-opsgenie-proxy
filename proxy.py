#!/usr/local/env python3.5
from sanic import Sanic
import requests, json
from sanic.response import json, text

apiurl = 'https://api.opsgenie.com/v2/alerts'

proxy = Sanic()

def makeOpsgenieStuff(data):
    output = data
    for line in data['description'].splitlines():
        if line.startswith(' - opsgenie_'):
            _, info = line.split('_', 1)
            info, injectThis = info.split(' = ', 1)
            output[info] = injectThis

    return data

@proxy.route('/v2/alerts', methods=['POST'])
async def passThisToOpsGenie(request):
    headers = {
        'authorization': request.headers['authorization'],
        'content-type': 'application/json'
    }

    handle = requests.post(apiurl,
        json=makeOpsgenieStuff(request.json),
        headers=headers
    )

    return text(handle.text, status=handle.status_code)

if __name__ == '__main__':
    proxy.run(host='0.0.0.0', port=9095)
