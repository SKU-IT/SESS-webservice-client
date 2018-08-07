import zeep


class SESS():
    """SESS web-service"""
    def __init__(self, username, password):
        super(SESS, self).__init__()
        self.username = username
        self.password = password
