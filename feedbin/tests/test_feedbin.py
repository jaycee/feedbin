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

if __name__ == '__main__':
    main() 
