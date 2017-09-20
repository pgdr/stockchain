from datetime import datetime as dt
from datetime import timedelta as td

import rsa

from hashlib import sha256
from base64 import b64encode, b64decode


def sha(obj, size=12):
    return sha256(obj).hexdigest()[:size]

def encode(msg, priv, method='SHA-256'):
    return b64encode(rsa.sign(sha(msg), priv, method))

def generate(keysize=1024):
    return rsa.newkeys(keysize)

def verify(msg, signed, user):
    try:
        return rsa.verify(sha(msg), b64decode(signed), user.public)
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

    action, stock, amount, price, exp, cre = message.to_tuple()
    print('User %s: %s' % (from_user.name, action))
    print('User %s %d %s for total price %.3f (cre=%s, exp=%s)' % (to_user.name,
                                                                   amount,
                                                                   stock,
                                                                   (amount*price),
                                                                   cre,
                                                                   exp))

def now_and_later(days=0, hours=0, minutes=0, seconds=0):
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError('Expiration cannot be in the past!')
    if days + hours + minutes + seconds == 0:
        raise ValueError('Expiration must be in the future.')
    now = dt.now()
    later = now + td(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return now, later

def time_to_str(t):
    return dt.strftime(t, '%Y-%m-%dT%H:%M:%S')

def parse_time(s):
    return dt.strptime(s, '%Y-%m-%dT%H:%M:%S')
