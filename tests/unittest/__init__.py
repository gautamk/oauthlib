import sys

try:
    # check the system path first
    from unittest2 import *
except ImportError:
    if sys.version_info >= (2, 7):
        # unittest2 features are native in Python 2.7
        from unittest import *
    else:
        raise

if sys.version_info.minor == 1:
    TestCase.assertIsInstance = lambda self, obj, cls: self.assertTrue(isinstance(obj, cls))
