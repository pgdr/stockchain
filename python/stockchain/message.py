#!/usr/bin/env python
from __future__ import print_function

from datetime import datetime as dt
from datetime import timedelta as td

class Message(object):
    def __init__(self, desc):
        self.action, self.stock, self.amount, self.price, self.exp = desc.split('!')
        self.amount = int(self.amount)
        self.price = float(self.price)

    def to_tuple(self):
        return self.action, self.stock, self.amount, self.price, self.exp

    @staticmethod
    def create_message(action, stock, amount, price, expiration=None):
        if expiration is None:
            expiration = dt.now() + td(hours=1)
        return Message('%s!%s!%d!%.3f!%s' % (action,
                                                 stock,
                                                 amount,
                                                 price,
                                                 expiration))

    def to_string(self):
        return repr(self)

    def __repr__(self):
        return '%s!%s!%d!%.3f!%s' % (self.action,
                                     self.stock,
                                     self.amount,
                                     self.price,
                                     self.exp)
