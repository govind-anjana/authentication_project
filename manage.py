#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    project_root = Path(__file__).resolve().parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it is installed and available "
            "in the active environment, and that the project root is on the "
            "PYTHONPATH."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
