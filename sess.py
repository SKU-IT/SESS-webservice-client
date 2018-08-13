import csv
from hashlib import md5
from io import StringIO
from math import ceil
from sys import stderr

import zeep

DEBUG = True


class WebService():
    """SESS web-service"""
    WSDL = 'https://sess.sku.ac.ir/sess/WebServices/%s.asmx?WSDL'

    def __init__(self, username, password, web_service, delimiter='&'):
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

    def login(self, gate):
        """Login with a special gate.

        List of available gates should be provided by IT center.
        """
        self.call('Login', Gate=gate)

    def set_list(self, condition):
        """Create a list based on condition return length of it.

        Created list is stored in server itself until next login.
        Condition should not include control characters.
        """
        return self.call('SetList', Condition=condition)[0]

    def get_list(self, count, start=0):
        """Return count numbers of last created list starting from start."""
        return self.call('GetList', Start=start, Count=count)


class Gate():
    """SESS web-service gate"""
    def __init__(self, gate, username, password, web_service_name, sep_part='&', sep_line=';', sep_field='|'):
        self.sep_part = sep_part
        self.sep_line = sep_line
        self.sep_field = sep_field
        self.web_service = WebService(username, password, web_service_name)
        self.web_service.login(gate)

    def set_list(self, condition):
        """Create a list based on condition return length of it.

        Created list is stored in server itself until next login.
        Condition should not include control characters.
        """
        return self.web_service.set_list(condition)

    def get_list(self, count, start=0):
        """Return count numbers of last created list starting from start."""
        return self.web_service.get_list(count, start)


class CSVGate(Gate):
    """SESS CSV-like web-service gate"""
    def __init__(self, gate, username, password, web_service_name, bucket_length=100):
        super(CSVGate, self).__init__(gate, username, password, web_service_name,
                                      sep_part='&', sep_line='\n', sep_field=',')
        self.bucket_length = bucket_length
        self.headers = []

    def get_data(self, condition, max_length=None):
        """Get info of students matching condition.

        Set max_length to None to get all rows.
        """
        length = self.web_service.set_list(condition)
        if max_length:
            length = max_length
        res_str = ''
        for i in range(ceil(length / self.bucket_length)):
            bucket_length = self.bucket_length
            if (i + 1) * self.bucket_length > length:
                bucket_length = length - i * self.bucket_length
            res = self.web_service.get_list(bucket_length, start=i * self.bucket_length)
            res_str += ['', res[1]][int(res[0]) > 0]
        return list(csv.DictReader(StringIO(res_str, self.sep_line), fieldnames=self.headers))
