
from logging import Logger
from logging import getLogger

from os import environ as osEnvironment

from buildlackey.Environment import Environment


class EnvironmentBase:
    """

    """
    def __init__(self):

        self.ebLogger: Logger = getLogger(__name__)

        self._projectsBase:     str = ''
        self._projectDirectory: str = ''

        try:
            self._projectsBase = osEnvironment[Environment.ENV_PROJECTS_BASE]
        except KeyError:
            self.ebLogger.error(f'Project Base not set')
        try:
            self._projectDirectory = osEnvironment[Environment.ENV_PROJECT]
        except KeyError:
            self.ebLogger.error(f'Project Directory not set')

    @property
    def projectsBase(self) -> str:
        return self._projectsBase

    @property
    def projectDirectory(self) -> str:
        return self._projectDirectory

    @property
    def validProjectsBase(self) -> bool:
        if self._projectsBase == '':
            return False
        else:
            return True

    def validProjectDirectory(self) -> bool:
        if self._projectDirectory == '':
            return False
        else:
            return True
