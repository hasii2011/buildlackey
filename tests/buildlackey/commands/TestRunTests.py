
from click.testing import CliRunner
from click.testing import Result

from buildlackey import Commands
from buildlackey.Version import Version


def testRunTestVersion():
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(Commands.runtests, ['--version'])

    assert result.exit_code == 0
    # noinspection SpellCheckingInspection
    assert result.output == f'runtests version {Version().version}\n'


if __name__ == '__main__':
    testRunTestVersion()
