from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
"""Root of the repository."""

CONFIG_ENV_FILE = REPO_ROOT / "{{cookiecutter.project_repository_name}}.env"
"""The `.env` file containing relevant configuration."""

DATA_FOLDER = REPO_ROOT / "data"
"""Folder containing all project data"""

RAW_DATA_FOLDER = DATA_FOLDER / "raw"
"""Folder containing raw data."""

PROCESSED_DATA_FOLDER = DATA_FOLDER / "processed"
"""Folder containing processed / intermediate data created by this project."""

OUTPUT_DATA_FOLDER = DATA_FOLDER / "output"
"""Folder containing output data as a result of this project's functionality."""
