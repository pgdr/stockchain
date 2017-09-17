#!/usr/bin/env python
from __future__ import print_function

import rsa
from base64 import b64encode, b64decode
from datetime import datetime as dt
from datetime import timedelta as td



def verify(msg, signed, user):
    try:
        return rsa.verify(msg, b64decode(signed), user.public)
    except Exception as err:
        if 'Verification failed' == err.message:
            print('%s did not sign "%s"' % (user.name, msg))
        else:
            print(err.message)
        return False


def verify_transaction(transaction):
    message, signed, double_signed, from_user, to_user = transaction.to_tuple()
    msg = message.to_string()
    assert verify(msg, signed, from_user)
    assert verify(signed, double_signed, to_user)

    action, stock, amount, price, exp = message.to_tuple()
    print('User %s: %s' % (from_user.name, action))
    print('User %s %d %s for total price %.3f (exp=%s)' % (to_user.name, amount, stock, (amount*price), exp))
