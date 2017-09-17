class Transaction(object):
    def __init__(self, message, signed, double_signed, from_user, to_user):
        self.message = message
        self.signed = signed
        self.double_signed = double_signed
        self.from_user = from_user
        self.to_user = to_user

    def __repr__(self):
        return 'Transaction(%s, %s, %s, %s, %s)' % (self.message,
                                                    self.signed,
                                                    self.double_signed,
                                                    self.from_user,
                                                    self.to_user)

    def to_tuple(self):
        return self.message, self.signed, self.double_signed, self.from_user, self.to_user
