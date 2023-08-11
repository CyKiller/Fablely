## test_utils.py

import unittest
import logging
import os
import tempfile
from fablely.utils import setup_logger, print_progress, safe_cast

class TestUtils(unittest.TestCase):
    ## Test setup_logger function
    def test_setup_logger(self):
        log_file = tempfile.mktemp()
        logger = setup_logger('test_logger', log_file)
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.name, 'test_logger')
        self.assertEqual(logger.level, logging.INFO)
        logger.info('Test log message')
        with open(log_file, 'r') as f:
            log_content = f.read()
        self.assertIn('Test log message', log_content)
        os.remove(log_file)

    ## Test print_progress function
    def test_print_progress(self):
        # As this function prints to stdout, we can't directly test its output.
        # But we can at least ensure it doesn't raise any exceptions.
        try:
            print_progress(50, 100, 'Progress:', 'Complete', 1, 100, '█')
        except Exception as e:
            self.fail(f'print_progress raised {type(e).__name__} unexpectedly!')

    ## Test safe_cast function
    def test_safe_cast(self):
        self.assertEqual(safe_cast('123', int), 123)
        self.assertEqual(safe_cast('123.45', float), 123.45)
        self.assertEqual(safe_cast('abc', int, -1), -1)
        self.assertEqual(safe_cast('abc', float, -1.0), -1.0)
        self.assertEqual(safe_cast(None, int, -1), -1)
        self.assertEqual(safe_cast(None, float, -1.0), -1.0)

if __name__ == '__main__':
    unittest.main()
