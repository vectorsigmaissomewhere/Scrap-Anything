import os
import sys

PWD = os.getcwd()
DJANGO_PROJECT = os.environ.get("DJANGO_PROJECT") or "home"
DJANGO_ROOT_DIR = os.environ.get("DJANGO_ROOT_DIR") or "home"

# Add the parent directory of `home` to sys.path
project_root = os.path.dirname(os.path.abspath(PWD))
sys.path.append(project_root)

PROJ_MISSING_MSG = """Set an environment variable:
`DJANGO_PROJECT=your_project_name`
or call:
`init_django(project_name=your_project_name)`
"""

def init_django(project_name=None):
    if not project_name:
        raise ValueError(PROJ_MISSING_MSG)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.home.settings")
    import django
    django.setup()

