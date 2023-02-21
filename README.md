# π Python Project Template


![](https://img.shields.io/badge/π__project__template-1.0.0-green)

The current version of the π project template is `1.0.0`

## TLDR

If you've done this before:

```shell
cookiecutter --overwrite-if-exists git+ssh://git@github.com/Rjdrenth/pi-project-template.git
```


## About the project template

This is an opinionated project template for:

- Python-based (Data Science) projects that need to be deployed
- Windows / Unix / WSL-based development
- Deployments using Docker

It assumes the user attempts to write proper python code and/or applications which may or may not:

- be used in Jupyter notebooks
- be used in a Docker environment
- be published to Pypi or a private package repository

## Project tools

This Python project template features the following project tools:

- [Poetry](https://python-poetry.org/) for virtual environment & dependency management.
- [Pre-commit](https://pre-commit.com/) to enforce code guidelines and keep a clean repository with every commit.
- A [Jupyter](https://jupyter.org/) notebook template.
- A [Task](https://taskfile.dev) Taskfile (which is a cross-platform Make alternative) to run tasks to make life easier.
- A [Docker](https://www.docker.com/)-based development environment for Windows users working on Linux projects.
- Simple testing using [Pytest](https://pytest.org).
- Version management using [bump2version](https://github.com/c4urself/bump2version)
- Test coverage calculation using the `pytest` and `coverage` libraries.

- Supports publishing a package to and installing packages from various public or private repositories. See [/docs/configuring_artifact_repositories.md](/{{cookiecutter.project_repository_name}}/docs/configuring_artifact_repositories.md) for instructions:

  - [PyPI](https://pypi.org/)
  - [Google Artifact Registry](https://cloud.google.com/artifact-registry)

For a detailed description of each of these tools, read [/docs/project_tools.md](/docs/project_tools.md).

## Prerequisites

This project template assumes you have the following software installed on your system:

- [Python](https://www.python.org/)
- [git](https://git-scm.com/)
- [cookiecutter](https://github.com/audreyfeldroy/cookiecutter-pypackage) python package
- [Poetry](https://python-poetry.org/docs/#installation/)
- [Task](https://taskfile.dev/installation/)
- [Docker](https://docs.docker.com/engine/install/) - Optional

Installation instructions can be found at [/docs/prerequisites_installation_instructions.md](/docs/prerequisites_installation_instructions.md).


## Using the project template for new projects

**>>>The information below is useful for starting a new project. In order to update an old project with the latest-and-greatest project structure, check out [Updating existing projects to new project structure](#updating-existing-projects-to-new-project-structure)<<<**

If you're starting a new project, perform the following steps:

- Create a new repository in your git repository provider of choice, e.g. github, gitlab or bitbucket.  
- Clone the repository of your project to your local disk.

- Next, initialiase your new project using the cookiecutter project template, by executing the following command *in the same directory into which you cloned the repository, not yet in the repository root*:
  ```shell
  cookiecutter --overwrite-if-exists git+ssh://git@github.com/Rjdrenth/pi-project-template.git
  ```

  **Note:** If you are prompted with the following question `You've downloaded /home/<user>/.cookiecutters/pi-project-template before. Is it okay to delete and re-download it? [yes]:` press `enter` or type `yes` and press `enter` in order to get the latest version of the project template.

### Parameters

The following parameters can be set during project initialisation:

 - **project_repository_name** - The name of the repository root folder, same as the repository name in your git repository provider.
 - **python_package_name** - The name your python package will receive, i.e. the name you will use then you `import` (sub-)packages of your project. E.g. `from python_package_name.config import paths`
 - **minimum_python_version** - The minimum python version your project requires.

### Initialising your project

Initialising your project for development includes:
- Install the Poetry virtual environment
- Registering the virtual environment as a Jupyter kernel, in case you're working with notebooks
- Installing pre-commit, to ensure consistent coding style

This is performed automatically and is as simple as running the following command *within your project folder, the repository root*:

```shell
task initialise-project
```

Follow the instructions in your new project's readme to initialise your project for development.

## Updating existing projects to new project structure

In order to update an older project based on this project template so it uses the latest changes and improvements, run the following command in your own project:

```shell
task update-project-template
```

This should update all relevant files.

Do note that it does this by overwriting any and all changes you have made to the files that are supplied by default with the project template if they have been updated. Most notably you will have to manually inspect the following files so you don't delete anything accidentally:

- `README.md`
- `pyproject.toml`


### Acknowledgements

Thanks to:

- [Mediquest](https://home.mediquest.nl/) for allowing me to create an open source version of the project template I developed during my employment with them.
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) for providing an excellent project template framework
- [TezRomacH's python project template](https://github.com/TezRomacH/python-package-template) for inspiration, which might be an even better fit for you, depending on your needs.

### License

The π Python Project Template is available under the MIT license. See the [LICENSE](/LICENSE) file for more info.
