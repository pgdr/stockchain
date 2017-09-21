#!/usr/bin/env python
from __future__ import print_function

import util


class Message(object):
    def __init__(self, desc):
        self.action, self.stock, self.amount, self.price, self.cre, self.exp = desc.split('!')
        self.amount = int(self.amount)
        self.price = float(self.price)

    def to_tuple(self):
        return self.action, self.stock, self.amount, self.price, self.cre, self.exp

    @staticmethod
    def create(action, stock, amount, price):
        created, expires =util.now_and_later(hours=1)
        return Message('%s!%s!%d!%.3f!%s!%s' % (action,
                                             stock,
                                             amount,
                                             price,
                                             util.time_to_str(created),
                                             util.time_to_str(expires)))

    def to_string(self):
        return repr(self)

    def __repr__(self):
        return '%s!%s!%d!%.3f!%s!%s' % (self.action,
                                     self.stock,
                                     self.amount,
                                     self.price,
                                     self.cre,
                                     self.exp)
