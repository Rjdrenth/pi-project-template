from {{cookiecutter.python_package_name}} import __version__


def test_version():
    assert __version__ == "{{cookiecutter.package_version}}"


if __name__ == "__main__":
    from pathlib import Path

    import pytest

    pytest.main([Path(__file__).name])
