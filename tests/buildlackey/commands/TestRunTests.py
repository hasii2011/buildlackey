
from click.testing import CliRunner
from click.testing import Result

from buildlackey import Commands
from buildlackey import __version__ as version


def testRunTestVersion():
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(Commands.unittests, ['--version'])

    assert result.exit_code == 0
    # noinspection SpellCheckingInspection
    assert result.output == f'unittests version {version}\n'


if __name__ == '__main__':
    testRunTestVersion()
