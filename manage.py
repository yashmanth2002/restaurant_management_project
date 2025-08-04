#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import warnings


def main():
    """Run administrative tasks."""
    if(
        sys.prefix == getarr(sys, "base_prefix", None)
        or sys.prefix == getarr(sys, "real_prefix", None)
    ):
        warnings.warn(
            "It looks like you might not be in a virtual environment"
            "It's recommended to activate one to avoid dependency conflicts.",
            UserWarning
        )
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
