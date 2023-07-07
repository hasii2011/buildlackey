
import logging
import logging.config

from importlib.resources import files
from importlib.abc import Traversable

from json import load as jsonLoad

from os import chdir

from os import sep as osSep
from os import system as osSystem

from pathlib import Path

from click import argument
from click import option
from click import clear
from click import command
from click import secho
from click import version_option

from buildlackey import __version__ as version

from buildlackey.Environment import Environment
from buildlackey.commands.Cleanup import Cleanup
from buildlackey.commands.RunMypy import RunMypy
from buildlackey.commands.RunTests import RunTests

# noinspection SpellCheckingInspection
BUILD_WHEEL:   str = 'python -m build --sdist --wheel'

PROJECTS_BASE: str = 'PROJECTS_BASE'
PROJECT:       str = 'PROJECT'

RESOURCES_PACKAGE_NAME:       str = 'buildlackey.resources'
JSON_LOGGING_CONFIG_FILENAME: str = "loggingConfiguration.json"

STATUS_NO_SUCH_PATH:                 int = 23
STATUS_UNIT_TEST_FAILED:             int = 77
STATUS_MISSING_ENVIRONMENT_VARIABLE: int = 42

MESSAGE_MISSING_ENVIRONMENT_VARIABLE: str = 'Missing an environment variable'
WARNING_OPTION_HELP:                  str = 'Use this option to control Python warnings'


def changeToProjectRoot(projectsBase: str, project: str):

    fullPath: str = f'{projectsBase}{osSep}{project}'
    chdir(fullPath)


def doCommandStart(projects_base: str, project: str):
    setUpLogging()
    clear()
    secho(f'{projects_base=}', color=True, reverse=True)
    secho(f'{project=}', color=True, reverse=True)
    secho('')
    changeToProjectRoot(projectsBase=projects_base, project=project)


def setUpLogging():
    """
    """
    traversable: Traversable = files(RESOURCES_PACKAGE_NAME) / JSON_LOGGING_CONFIG_FILENAME

    loggingConfigFilename: str = str(traversable)

    with open(loggingConfigFilename, 'r') as loggingConfigurationFile:
        configurationDictionary = jsonLoad(loggingConfigurationFile)

    logging.config.dictConfig(configurationDictionary)
    logging.logProcesses = False
    logging.logThreads = False


@command()
@version_option(version=f'{version}', message='%(prog)s version %(version)s')
@option('--input-file', '-i', required=False,   help='Use input file to list the unit tests to execute')
@option('--warning',    '-w', required=False,   help=WARNING_OPTION_HELP)
def runtests(input_file: str, warning: str):
    """
    \b
    Runs the unit tests for the project specified by the environment variables listed below;
    \b
    Use the -i/--input-file option to list a set of module names to execute as your
    unit tests

    Legal values for -w/--warning are:

    \b
        default
        error
        always
        module
        once
        ignore
    \b
    Environment Variables

        PROJECTS_BASE -  The local directory where the python projects are based
        PROJECT       -  The name of the project;  It should be a directory name

    \b
    By default, buildlackey runs the module named tests.TestAll

    """

    setUpLogging()
    runTests: RunTests = RunTests(inputFile=input_file, warning=warning)

    runTests.execute()


@command()
@version_option(version=f'{version}', message='%(prog)s version %(version)s')
def cleanup():
    """
    \b
    Clean the build artifacts for the project specified by the following environment variables
    \b
        PROJECTS_BASE -  The local directory where the python projects are based
        PROJECT       -  The name of the project;  It should be a directory name
    """
    setUpLogging()
    clean: Cleanup = Cleanup()

    clean.execute()


@command()
@version_option(version=f'{version}', message='%(prog)s version %(version)s')
def runmypy():
    """
    \b
    Runs the mypy checks for the project specified by the following environment variables
    \b
        PROJECTS_BASE -  The local directory where the python projects are based
        PROJECT       -  The name of the project;  It should be a directory name
    """
    runMyPy: RunMypy = RunMypy()
    runMyPy.execute()


@command()
@version_option(version=f'{version}', message='%(prog)s version %(version)s')
@option('--input-file', '-i', required=False,   help='Use input file to specify a set of commands to execute')
def deploy(input_file: str):
    """
    \b
    Creates the deployable for the project specified by the environment variables listed below
    \b
    Use the -i/--input-file option to specify a set of custom commands to execute to build
    your deployable

    Environment Variables
    \b
        PROJECTS_BASE -  The local directory where the python projects are based
        PROJECT       -  The name of the project;  It should be a directory name

    """
    setUpLogging()
    envBase: Environment = Environment()
    if envBase.validProjectsBase is True and envBase.validProjectDirectory() is True:
        changeToProjectRoot(projectsBase=envBase.projectsBase, project=envBase.projectDirectory)
    else:
        secho(f'{MESSAGE_MISSING_ENVIRONMENT_VARIABLE}')
        exit(STATUS_MISSING_ENVIRONMENT_VARIABLE)

    doCommandStart(envBase.projectsBase, envBase.projectDirectory)

    if input_file is None:
        secho(f'{BUILD_WHEEL}')
        status: int = osSystem(BUILD_WHEEL)
        secho(f'{status=}')

        CHECK_PACKAGE: str = 'twine check dist/*'
        secho(f'{CHECK_PACKAGE}')
        status = osSystem(CHECK_PACKAGE)
        secho(f'{status=}')
    else:
        path: Path = Path(input_file)
        if path.exists() is True:
            with path.open(mode='r') as fd:
                cmd: str = fd.readline()
                while cmd != '':
                    secho(f'{cmd}')
                    status = osSystem(f'{cmd}')
                    if status != 0:
                        exit(status)
                    cmd = fd.readline()
        else:
            secho(f'No such file: {input_file}')
            exit(STATUS_NO_SUCH_PATH)


@command()
@version_option(version=f'{version}', message='%(prog)s version %(version)s')
@argument('projects_base', envvar=PROJECTS_BASE)
@argument('project', envvar=PROJECT)
def prodpush(projects_base: str, project: str):
    """
    \b
    Pushes the deployable to pypi.  The project is specified by the following environment variables
    \b
        PROJECTS_BASE -  The local directory where the python projects are based
        PROJECT       -  The name of the project;  It should be a directory name
    """
    doCommandStart(projects_base, project)

    PYPI_PUSH: str = 'twine upload  dist/*'

    secho(f'{PYPI_PUSH}')
    status = osSystem(PYPI_PUSH)
    secho(f'{status=}')


if __name__ == "__main__":

    runtests(['-w', 'module'])
    # cleanup(['--help'])
    # deploy(['--help'])
