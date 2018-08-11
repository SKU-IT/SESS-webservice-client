from sess import Gate


class PersonalInfo(Gate):
    """Students personal info web service"""
    def __init__(self, username, password, sep_part='&', sep_line=';', sep_field='|'):
        super(PersonalInfo, self).__init__('PersonalInfo', username, password, 'StdService',
                                           sep_part='&', sep_line='\n', sep_field=',')

    def get_list(self, count, start=0):
        """Return count numbers of last created list starting from start."""
        res = self.web_service.get_list(count, start)
        return ['', res[1]][int(res[0]) > 0]
