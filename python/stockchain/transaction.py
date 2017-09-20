class Transaction(object):
    def __init__(self, message, signed, double_signed, from_user, to_user):
        self.message = message
        self.signed = signed
        self.double_signed = double_signed
        self.from_user = from_user
        self.to_user = to_user

    def __repr__(self):
        return '!'.join(map(str, [self.message,
                                  self.signed,
                                  self.double_signed,
                                  self.from_user,
                                  self.to_user]))

    def to_tuple(self):
        return self.message, self.signed, self.double_signed, self.from_user, self.to_user

    @staticmethod
    def parse(trans):
        action, stock, amount, price, created, expires = trans.split('!')[:6]
        message = '!'.join([action, stock, amount, price, created, expires])
        signed, double_signed, from_user, to_user = trans.split('!')[6:]
        return Transaction(message, signed, double_signed, from_user, to_user)
