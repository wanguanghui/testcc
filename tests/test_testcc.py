#!/usr/bin/env python
"""Tests for `testcc` package."""

import pytest
from click.testing import CliRunner

from testcc import cli, calculations


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    del response


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'testcc' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_add():
    a = 1
    b = 2
    assert 3 == calculations.add(a, b)


def test_subtract():
    a = 1.0
    b = 2.0
    assert -1.0 == calculations.subtract(a, b)

def test_multiply():
    a = 2.0
    b = 5.0
    assert 10.0 == calculations.multiply(a, b)


def test_divide():
    a = 3
    b = 2
    assert 1.5 == calculations.divide(a, b)


def test_divide_zero():
    a = 3
    b = 0
    try:
        calculations.divide(a, b)
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)
