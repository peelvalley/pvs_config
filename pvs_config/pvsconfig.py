import os
from copy import deepcopy

class PVSConfig():
    def __init__(self, **kwargs):
        self.__kwargs = kwargs
        self.__options = {}

    @property
    def kwargs(self):
        return deepcopy(self.__kwargs)

    def get_option(self, option):
        return self.__kwargs.get(option, os.environ.get(option))
