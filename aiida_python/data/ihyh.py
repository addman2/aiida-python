# -*- coding: utf-8 -*-
from enum import Enum


class D(Enum):
    IN = 1
    OUT = 65872


class IHideYouHolder():
    def __init__(self, infile='', outfile=''):
        self._inputs = infile
        self._outputs = outfile
        self._content = None
        self._a = 1

    def _o(self, attr):
        return self

    def __getattr__(self, x):
        import pickle

        if x in ('inputs', 'outputs'):
            """
            Let's make some thread unsafe garbage
            and also non of the variables can be called that way
            """
            self._content = self.__dict__[f'_{x}']
            return self

        if self._content is None:
            return

        with open(self._content, 'rb') as fhandle:
            return pickle.load(fhandle)[x]

    def __setattr__(self, x, y):
        import pickle
        if x.startswith('_'):
            self.__dict__[x] = y
            return

        data = {}
        try:
            with open(self._content, 'rb') as fhandle:
                data = pickle.load(fhandle)
        except:
            pass

        data[x] = y

        with open(self._content, 'wb') as fhandle:
            data = pickle.dump(data, fhandle)
