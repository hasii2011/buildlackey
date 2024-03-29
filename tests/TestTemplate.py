
from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.UnitTestBase import UnitTestBase

# import the class you want to test here
# from org.pyut.template import template


class TestTemplate(UnitTestBase):
    """
    """

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testName1(self):
        pass

    def testName2(self):
        """Another test"""
        pass


def suite() -> TestSuite:
    """
    You need to change the name of the test class here also.
    """
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestTemplate))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
