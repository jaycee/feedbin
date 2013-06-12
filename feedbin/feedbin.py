from base64 import b64encode

class Feedbin:
   
    def __init__(self, user, password):
        auth_string = 'Basic %s' % self._gen_b64_data(user, password)
        self._auth_string = auth_string.encode('utf-8')

    def _gen_b64_data(self, user, password):
        auth_string = '%s:%s' % (user, password)
        auth_string = b64encode(auth_string.encode('utf-8'))
        return auth_string.decode('utf-8')
