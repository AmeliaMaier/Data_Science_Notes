import time
import unittest
import src.class_being_tested as name_of_class_being_tested

SLOW_TEST_THRESHOLD = 0.1

'''make sure to add the name of the file to your makefile'''

class Test_NameOfMethodBeingTested(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > SLOW_TEST_THRESHOLD:
            print(f'{self.id()}: {round(elapsed,2)}s')

    def test_description_of_test_being_run(self):
        # write in the code to set up expected and found values
        self.assertEqual(expected_value, found_value)
