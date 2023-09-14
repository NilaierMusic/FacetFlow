import unittest
import shutil

class AsciiTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write('√ [PASS] ')
        self.stream.write(self._center_align(str(test.shortDescription())) + '\n')

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write('× [ERROR] ')
        self.stream.write(self.getDescription(test))
        self.stream.writeln(':')
        self.stream.writeln(self._center_align(self._exc_info_to_string(err, test)))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write('× [FAIL] ')
        self.stream.write(self.getDescription(test))
        self.stream.writeln(':')
        self.stream.writeln(self._center_align(self._exc_info_to_string(err, test)))

    def _center_align(self, string):
        terminal_size = shutil.get_terminal_size((80, 20))
        offset = int(terminal_size.columns / 2)  # adjust offset as required
        return "{:^{}}".format(string, terminal_size.columns - offset)

class AsciiTestRunner(unittest.TextTestRunner):
    resultclass = AsciiTestResult