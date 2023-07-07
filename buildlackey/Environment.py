
from logging import Logger
from logging import getLogger

from os import chdir

from os import environ as osEnvironment
from os import sep as osSep

from click import ClickException
from click import clear
from click import secho


class Environment:
    """

    """
    ENV_PROJECTS_BASE: str = 'PROJECTS_BASE'
    ENV_PROJECT:       str = 'PROJECT'

    def __init__(self):

        self.ebLogger: Logger = getLogger(__name__)

        self._projectsBase:     str = ''
        self._projectDirectory: str = ''

        try:
            self._projectsBase = osEnvironment[Environment.ENV_PROJECTS_BASE]
        except KeyError:
            raise ClickException('Project Base not set')
        try:
            self._projectDirectory = osEnvironment[Environment.ENV_PROJECT]
        except KeyError:
            raise ClickException(f'Project Directory not set')

        clear()
        secho(f'projects_base={self._projectsBase}', color=True, reverse=True)
        secho(f'project={self._projectDirectory}', color=True, reverse=True)
        secho('')

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

    def _changeToProjectRoot(self):

        fullPath: str = f'{self._projectsBase}{osSep}{self._projectDirectory}'
        chdir(fullPath)
