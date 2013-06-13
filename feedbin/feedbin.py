from base64 import b64encode
from json import loads 
from urllib.parse import (
    urlencode,
    urljoin,
    )
from urllib.request import (
    Request,
    urlopen,
    )

class Feedbin:
    
    apiURL = 'http://api.feedbin.me/v2/'

    def __init__(self, user, password):
        auth_string = 'Basic %s' % self._gen_b64_data(user, password)
        self._auth_string = auth_string.encode('utf-8')

    def _gen_b64_data(self, user, password):
        auth_string = '%s:%s' % (user, password)
        auth_string = b64encode(auth_string.encode('utf-8'))
        return auth_string.decode('utf-8')

    def _makeRequest(self, resource, params=None):
        resource += '.json'
        url = urljoin(self.apiURL, resource)
        if params:
            url = "%s?%s" % (url, urlencode(params))
        req = Request(url)
        req.add_header('Authorization', self._auth_string)
        return req

    def _handleRequest(self, resource, params=None):
        req = self._makeRequest(resource, params)
        data = urlopen(req).read()
        return loads(data)
