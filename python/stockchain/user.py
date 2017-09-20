import util

class User(object):
    def __init__(self, name='', keysize=1024):
        self.name = name
        self.__pub, self.__priv = util.generate(keysize=keysize)

    def sign(self, msg):
        return util.encode(msg, self.__priv)

    @property
    def public(self):
        return self.__pub

    @property
    def short(self):
        return '%s:%s' % (util.sha(str(self.public.n)), self.public.e)

    def __repr__(self):
        #return 'User: %s, (%s)' % (self.name, self.public)
        #def __str__(self):
        return 'User(%s/%s)' % (self.short, self.name)
