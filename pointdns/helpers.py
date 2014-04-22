import json
import requests


class Response(object):

    def __init__(self, status, content=''):
        self.status = status
        self.content = content


def request_http(method, url, auth, data=None, query_data=None):
    return request(method, url, auth, data, query_data, scheme='http')


def request(method, url, auth, data=None, query_data=None, scheme='https'):

    if data is not None:
        data = json.dumps(data)
    url = '%s://pointhq.com%s' % (scheme, url)
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }
    r = getattr(requests, method)(
        url, auth=auth, params=query_data, data=data, headers=headers)

    return Response(r.status_code, r.text)
