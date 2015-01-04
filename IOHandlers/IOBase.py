''' 
    Base class for Input/Output handlers.
    All IO Handlers should implement IOBase through Subclassing.
'''

import abc

class IOBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def messageIn(self):
        """receive user input via the IO protocol."""
        return

    @abc.abstractclassmethod
    def messageOut(self):
        """send user input via the IO protocol."""
        return
