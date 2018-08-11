import csv
from io import StringIO
from math import ceil

from sess import Gate


class PersonalInfo(Gate):
    """Students personal info web service"""
    def __init__(self, username, password, sep_line='\n', sep_field=','):
        super(PersonalInfo, self).__init__('PersonalInfo', username, password, 'StdService',
                                           sep_part='&', sep_line='\n', sep_field=',')
        self.bucket_length = 100
        self.headers = ['SID', 'FieldName', 'Email', 'FirstName', 'LastName']
        self.sep_line = sep_line
        self.sep_field = sep_field

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
