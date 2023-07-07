from pathlib import Path
from unittest import TestSuite
from unittest import main as unitTestMain

from os import environ as osEnviron

from click import ClickException
from hasiihelper.UnitTestBase import UnitTestBase

from buildlackey.Environment import Environment


class TestEnvironmentBase(UnitTestBase):

    TEST_PROJECTS_BASE: str = 'unitTestProjectsBase'

    def setUp(self):
        super().setUp()
        tmpDir: str = '/tmp'
        tmpProjectsBase: Path = Path(tmpDir) / Path(TestEnvironmentBase.TEST_PROJECTS_BASE)
        tmpProjectsBase.mkdir(exist_ok=True)

        self._tmpProjectsBase: Path = tmpProjectsBase

    def tearDown(self):
        super().tearDown()

    def testNoProjectsBaseSet(self):
        try:
            del osEnviron[Environment.ENV_PROJECTS_BASE]
        except KeyError:
            pass    # May or may not exist;  don't care

        self.assertRaises(ClickException, lambda: self._noProjectBase())

    def testNoProjectSet(self):
        osEnviron[Environment.ENV_PROJECTS_BASE] = str(self._tmpProjectsBase)   # Set the base
        try:
            del osEnviron[Environment.ENV_PROJECT]
        except KeyError:
            pass    # May or may not exist;  don't care

        self.assertRaises(ClickException, lambda: self._noProjectBase())

    def _noProjectBase(self):
        # noinspection PyUnusedLocal
        eb: Environment = Environment()


def suite() -> TestSuite:
    """
    """
    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    # testSuite.addTest(unittest.makeSuite(TestEnvironmentBase))
    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestEnvironmentBase))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
