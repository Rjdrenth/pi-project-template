"""
This script is used to verify whether the virtual environment was properly initialised and made available in Jupyter
Notebooks.
"""


def say_hello():
    """
    Print a message to indicate that the virtual environment has been correctly initialised.
    """
    print(
        "Hello! The {{cookiecutter.python_package_name}} project and its virtual environment appears to have been properly initialised!"
    )


if __name__ == "__main__":
    say_hello()
