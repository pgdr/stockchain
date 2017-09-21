from sys import stderr
from json import dumps

from .util import sha

class Chain(object):

    def __init__(self, problem='0000'):
        self.problem = problem
        self.genesis = Block.mine(0, 'genesis', self.problem)
        self.chain = [self.genesis]

    def __len__(self):
        return len(self.chain)

    def __getitem__(self, i):
        return self.chain[i]


    @property
    def messages(self):
        return [block.msg for block in self.chain if block.pre]  # skips genesis

    @property
    def valid(self):
        for i in range(len(self)-1):
            if self[i].hash() != self[i+1].pre:
                return False
        return True

    def __str__(self):
        size = len(self)
        s = ''
        s += '\n\n=========== BLOCKCHAIN, size=%d =============' % size
        for b in self:
            s += str(b)
            s += '\n'
        s += '============================================\n'
        s += 'Chain %s' % 'valid' if self.valid else 'invalid!'
        return s

    def append(self, obj):
        pre = self[-1].hash()
        self.chain.append(Block.mine(pre, repr(obj), self.problem))



class Block(object):

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
