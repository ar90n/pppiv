import json

import pppiv


def test_version(chshared_datadir, cli_runner):
    ret = cli_runner.invoke(pppiv.main, [])
    actual = json.loads(ret.output)

    assert 12 == len(actual)
    assert actual["python.pythonPath"].endswith("python")
    assert actual["python.formatting.blackPath"].endswith("black")
    assert actual["python.formatting.autopep8Path"].endswith("autopep8")
    assert actual["python.formatting.yapfPath"].endswith("yapf")
    assert actual["python.linting.banditPath"].endswith("bandit")
    assert actual["python.linting.flake8Path"].endswith("flake8")
    assert actual["python.linting.mypyPath"].endswith("mypy")
    assert actual["python.linting.pycodestylePath"].endswith("pycodestyle")
    assert actual["python.linting.pylamaPath"].endswith("pylama")
    assert actual["python.linting.pydocstylePath"].endswith("pycodestyle")
    assert actual["python.linting.pylintPath"].endswith("pylint")
    assert actual["python.sortImports.path"].endswith("isort")
