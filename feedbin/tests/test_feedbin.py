from base64 import b64decode
from unittest import (
    main,
    TestCase,
    )

from feedbin.feedbin import Feedbin

class FeedBinTestCase(TestCase):

    def test_init(self):
        f = Feedbin('jsmith@example.com','secret')
        scheme, auth_string = f._auth_string.split()
        self.assertEqual(b'Basic', scheme)
        self.assertEqual(b'jsmith@example.com:secret', b64decode(auth_string))

    def test_requests_have_auth_header(self):
        f = Feedbin('jsmith@example.com','secret')
        req = f._makeRequest('entries')
        self.assertIn('Authorization', req.headers.keys())

    def test_requests_without_params(self):
        f = Feedbin('jsmith@example.com','secret')
        req = f._makeRequest('entries')
        self.assertEqual(
            'http://api.feedbin.me/v2/entries.json',
            req.get_full_url())

    def test_requests_with_params(self):
        f = Feedbin('jsmith@example.com','secret')
        req = f._makeRequest('entries', {'foo': 'bar'})
        self.assertEqual(
            'http://api.feedbin.me/v2/entries.json?foo=bar',
            req.get_full_url())

if __name__ == '__main__':
    main() 
