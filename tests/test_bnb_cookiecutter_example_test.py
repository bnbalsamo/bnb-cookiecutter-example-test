"""Tests for bnb-cookiecutter-example-test."""
import pytest

import bnb_cookiecutter_example_test


def test_version_available() -> None:
    """Test the version dunder is available on the module."""
    version_attr = getattr(bnb_cookiecutter_example_test, "__version__", None)
    assert version_attr is not None


if __name__ == "__main__":
    pytest.main()
