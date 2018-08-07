from sys import stderr
from hashlib import md5

import zeep

DEBUG = True


class SESS():
    """SESS web-service"""
    WSDL = 'https://sess.sku.ac.ir/sess/WebServices/%s.asmx?WSDL'

    def __init__(self, username, password, web_service='StdService', delimiter='&'):
        super(SESS, self).__init__()
        self.username = username
        self.password = md5(password.encode('utf-8')).hexdigest()
        self.web_service = web_service
        self.delimiter = delimiter
        self.cleint = zeep.Client(self.WSDL % self.web_service)
        self.token = self._call('GetKey', UserId=self.username)[0]

    def call(self, service, *args, **kwargs):
        """Call API's 'service' method with given arguments."""
        res = self._call(service, UserId=self.username,
                         Pass=md5((self.token + self.password).encode('utf-8')).hexdigest(), *args, **kwargs)
        self.token = res[0]
        return res[1:]

    def _call(self, service, *args, **kwargs):
        res = self.cleint.service[service](*args, **kwargs).split(self.delimiter)
        if DEBUG:
            print('%s.%s(%s%s): %s' % (
                self.web_service,
                service,
                ('%s' % (args,))[1:-1],
                ', '.join(['%s=%s' % (key, value) for key, value in kwargs.items()]),
                res
            ), file=stderr)
        if res[0] == '000':
            return res[1:]
        else:
            raise RuntimeError('API Err %s\n%s' % tuple(res))
