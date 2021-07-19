# bnb-cookiecutter-example-test [![v0.1.0](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/bnbalsamo/bnb-cookiecutter-example-test/releases)

[![CI](https://github.com/bnbalsamo/bnb-cookiecutter-example-test/workflows/CI/badge.svg?branch=main)](https://github.com/bnbalsamo/bnb-cookiecutter-example-test/actions)
[![Coverage](https://codecov.io/gh/bnbalsamo/bnb-cookiecutter-example-test/branch/main/graph/badge.svg)](https://codecov.io/gh/bnbalsamo/bnb-cookiecutter-example-test/)
[![Documentation Status](https://readthedocs.org/projects/bnb-cookiecutter-example-test/badge/?version=latest)](http://bnb-cookiecutter-example-test.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/bnbalsamo/bnb-cookiecutter-example-test/shield.svg)](https://pyup.io/repos/github/bnbalsamo/bnb-cookiecutter-example-test/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A project.

See the full documentation at https://bnb-cookiecutter-example-test.readthedocs.io

# Installation

This project is currently only installable via development tooling.

- Install [poetry](https://python-poetry.org/)
- ```$ git clone https://github.com/bnbalsamo/bnb-cookiecutter-example-test.git```
- ```$ cd bnb-cookiecutter-example-test```
- ```$ poetry install --no-dev```

# Development

To install + configure a development environment...

- Install [poetry](https://python-poetry.org/)
- Clone the repository
    - `git clone git@github.com:bnbalsamo/bnb-cookiecutter-example-test.git`
- `cd` into the project directory
    - `cd bnb-cookiecutter-example-test`
- Install the project and development dependencies with poetry
    - `poetry install -E docs -E tests`
- Activate the project's virtual environment in your current shell
    - `poetry shell`
- Install the pre-commit hooks
    - `pre-commit install --install-hooks`

Development tasks are available via the `tasks.py` [invoke](http://www.pyinvoke.org/)
script. After installation you can view the help via `inv --list`

## Running Tests
```
$ inv run.tests
```

## Running autoformatters
```
$ inv run.autoformatters
```

## Upgrading Dependencies
```
$ poetry update
```

# Author
First Last <you@provider.com>

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage) v0.45.0_
