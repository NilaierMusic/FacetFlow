import unittest
from ascii_runner import AsciiTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.')
    AsciiTestRunner(verbosity=0).run(suite)