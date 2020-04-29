# pppiv
Poetry Python Path Injector for VSCode

[![Actions Status](https://github.com/ar90n/pppiv/workflows/Python%20package/badge.svg)](https://github.com/ar90n/pppiv/actions)
[![PyPI](https://img.shields.io/pypi/v/pppiv.svg)](https://pypi.python.org/pypi/pppiv)
[![PythonVersions](https://img.shields.io/pypi/pyversions/pppiv.svg)](https://pypi.python.org/pypi/pppiv)

# Install

```
$ poetry add pppiv --dev
```

# Usage

## Visual Studio Code
```
$ poetry run pppiv --target vscode
{
    "python.pythonPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/python",
    "python.formatting.blackPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/black",
    "python.formatting.autopep8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/autopep8",
    "python.formatting.yapfPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/yapf",
    "python.linting.banditPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/bandit",
    "python.linting.flake8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/flake8",
    "python.linting.mypyPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/mypy",
    "python.linting.pycodestylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylamaPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylama",
    "python.linting.pydocstylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylintPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylint",
    "python.sortImports.path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/isort"
}
$ cat .vscode/settings.json
{
    "python.pythonPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/python",
    "python.formatting.blackPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/black",
    "python.formatting.autopep8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/autopep8",
    "python.formatting.yapfPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/yapf",
    "python.linting.banditPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/bandit",
    "python.linting.flake8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/flake8",
    "python.linting.mypyPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/mypy",
    "python.linting.pycodestylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylamaPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylama",
    "python.linting.pydocstylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylintPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylint",
    "python.sortImports.path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/isort"
}
```

## coc.nvim
```
$ poetry run pppiv --target coc
{
    "python.pythonPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/python",
    "python.formatting.blackPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/black",
    "python.formatting.autopep8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/autopep8",
    "python.formatting.yapfPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/yapf",
    "python.linting.banditPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/bandit",
    "python.linting.flake8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/flake8",
    "python.linting.mypyPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/mypy",
    "python.linting.pycodestylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylamaPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylama",
    "python.linting.pydocstylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylintPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylint",
    "python.sortImports.path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/isort"
}
$ cat .vim/coc-settings.json
{
    "python.pythonPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/python",
    "python.formatting.blackPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/black",
    "python.formatting.autopep8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/autopep8",
    "python.formatting.yapfPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/yapf",
    "python.linting.banditPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/bandit",
    "python.linting.flake8Path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/flake8",
    "python.linting.mypyPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/mypy",
    "python.linting.pycodestylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylamaPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylama",
    "python.linting.pydocstylePath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pycodestyle",
    "python.linting.pylintPath": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/pylint",
    "python.sortImports.path": "/home/argon/.xdg/python_3.6_1580776274/pypoetry/virtualenvs/pppiv-DMQSTvHG-py3.6/bin/isort"
}
```

# License
This software is released under the MIT License, see [LICENSE](LICENSE).
