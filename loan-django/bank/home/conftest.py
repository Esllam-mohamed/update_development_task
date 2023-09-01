import pytest
import dj_database_url
from django.conf import settings
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "ATOMIC_REQUEST": True,
        "NAME" : BASE_DIR / 'db.sqlite3'
    }