import os

import dotenv
from {{cookiecutter.python_package_name}}.config import paths

# Load the .dotenv file
dotenv.load_dotenv(paths.CONFIG_ENV_FILE)

DEPLOYMENT_ENV = os.getenv("DEPLOYMENT_ENV", "dev")
"""The selected Deployment type. Must be one of: `["dev", "test", "staging", "production"]`"""
assert DEPLOYMENT_ENV in ["dev", "test", "staging", "production"]
