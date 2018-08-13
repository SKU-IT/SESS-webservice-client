from sess import CSVGate


class PersonalInfo(CSVGate):
    """Students personal info web service"""
    def __init__(self, username, password):
        super(PersonalInfo, self).__init__('PersonalInfo', username, password, 'StdService')
        self.headers = [
            'SID',
            'Intrant',
            'FieldName',
            'Level',
            'Email',
            'FirstName',
            'LastName',
            'ExitSemester',
            'CurrentAcadState',
            'NationalCode'
        ]
