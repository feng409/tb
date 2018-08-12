import re


class A:
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print(self)
        super(A, self).__init__()


A({'a': 1})
