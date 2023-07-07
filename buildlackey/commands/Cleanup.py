
from logging import Logger
from logging import getLogger

from os import system as osSystem

from click import secho

from buildlackey.Environment import Environment

DELETE_DIST_BUILD:       str = 'rm -rfv dist build'
DELETE_GENERAL_EGG_INFO: str = "find . -type d -name '*'.egg-info -delete"
DELETE_LOG_FILES:        str = 'find . -type f -name "*.log"      -delete'
DELETE_EGGS:             str = 'rm -rfv .eggs'


class Cleanup(Environment):
    
    def __init__(self):
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):

        self._changeToProjectRoot()

        secho(f'{DELETE_DIST_BUILD}')
        status: int = osSystem(DELETE_DIST_BUILD)
        secho(f'{status=}')

        secho(f'{DELETE_GENERAL_EGG_INFO}')
        status = osSystem(DELETE_GENERAL_EGG_INFO)
        secho(f'{status=}')

        secho(f'{DELETE_LOG_FILES}')
        status = osSystem(DELETE_LOG_FILES)
        secho(f'{status=}')

        secho(f'{DELETE_EGGS}')
        status = osSystem(DELETE_EGGS)
        secho(f'{status=}')

        PROJECT_EGG_INFO: str = f'rm -rfv {self._projectDirectory}.egg-info'
        secho(f'{PROJECT_EGG_INFO}')
        status = osSystem(PROJECT_EGG_INFO)
        secho(f'{status=}')
