from base64 import b64decode
from json import dumps
from unittest import (
    main,
    TestCase,
    )
from unittest.mock import (
    MagicMock,
    patch,
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

    def test_handle_request(self):
        f = Feedbin('jsmith@example.com','secret')
        f._makeRequest = MagicMock(name="_makeRequest")
        with patch('feedbin.feedbin.urlopen') as mock:
            mock_response = MagicMock(name="response")
            mock_response.read.return_value = dumps({'foo': ['bar']})
            mock.return_value = mock_response
            data = f._handleRequest('entries', {'fizz': 'buzz'})
        f._makeRequest.assert_called_with('entries', {'fizz': 'buzz'})
        self.assertDictEqual({'foo': ['bar']}, data)
        

if __name__ == '__main__':
    main() 
