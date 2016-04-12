#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\zzn\\settings.py");
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zzn.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
