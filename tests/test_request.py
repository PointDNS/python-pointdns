from pointdns.helpers import request
import unittest2
from httmock import urlmatch, HTTMock


class RequestTests(unittest2.TestCase):

    def test_https_post_request(self):

        @urlmatch(netloc=r'pointhq\.com', scheme='https',
                  method='post', path='/')
        def response_content(url, request):
            return {'status_code': 200,
                    'content': b'OK'}

        with HTTMock(response_content):
            r = request('post', '/', ('john', 'secret-key'), scheme='https')
            self.assertTrue(r.status == 200)
            self.assertTrue(r.content == 'OK')

    def test_http_get_request(self):

        @urlmatch(netloc=r'pointhq\.com', scheme='http',
                  method='get', path='/')
        def response_content(url, request):
            return {'status_code': 200,
                    'content': b'OK'}

        with HTTMock(response_content):
            r = request('get', '/', ('john', 'secret-key'), scheme='http')
            self.assertTrue(r.status == 200)
            self.assertTrue(r.content == 'OK')
