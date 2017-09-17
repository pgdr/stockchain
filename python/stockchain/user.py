#!/usr/bin/env python

import rsa
from base64 import b64encode, b64decode

class User(object):
    def __init__(self, name='', keysize=1024): # set to 2048
        self.name = name
        self.pub, self.priv = self.generate(keysize)

    @staticmethod
    def generate(keysize):
        return rsa.newkeys(keysize)

    def sign(self, msg, method='SHA-512'):
        return b64encode(rsa.sign(msg, self.priv, method))

    @property
    def public(self):
        return self.pub

    def __repr__(self):
        return 'User: %s, (%s)' % (self.name, self.pub)
