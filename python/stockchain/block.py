from sys import stderr
from json import dumps

from .util import sha

class Block:

    def __init__(self, pre, msg, nonce, pfx):
        self.pre = pre
        self.msg = msg
        self.nonce = nonce
        self.pfx = pfx

    def content(self):
        return {'pre' : self.pre,
                'msg'  : self.msg,
                'nonce': self.nonce,
                'pfx'  : self.pfx}

    @classmethod
    def mine(cls, pre, msg, pfx):
        b = Block(pre, msg, 0, pfx)
        b.remine()
        return b

    def remine(self):
        for i in range(10**7):
            self.nonce = i
            if self.is_valid():
                return True
        return False

    def hash(self):
        return sha(repr(self))

    def is_valid(self):
        return self.pfx == self.hash()[:len(self.pfx)]

    def __str__(self):
        d = self.content().copy()
        d['sha'] = self.hash()
        d['ok'] = 'valid' if self.is_valid() else 'invalid!'
        return dumps(d, indent=4, sort_keys=True)

    def __repr__(self):
        return repr(self.content())



def collect_messages(chain):
    return [block.msg for block in chain if block.pre]  # skips genesis


def chain_valid(chain):
    for i in range(len(chain)-1):
        if chain[i].hash() != chain[i+1].pre:
            return False
    return True

def print_chain(chain):
    size = len(chain)
    print('\n\n=========== BLOCKCHAIN, size=%d =============' % size)
    for b in chain:
        print(b)
        print('\n')
    print('============================================\n')
    print('Chain %s' % 'valid' if chain_valid(chain) else 'invalid!')
