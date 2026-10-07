#!/usr/bin/env python
import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line

# Configura o Django de forma inline e dinâmica
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="django-insecure-key-gestor-estudos",
        ROOT_URLCONF="manage",
        ALLOWED_HOSTS=["*"],
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "estudos",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "db.sqlite3",
            }
        },
        MIDDLEWARE=[
            "django.middleware.common.CommonMiddleware",
        ],
        MIGRATION_MODULES={
            "estudos": None,
        }
    )

from django.urls import path
import estudos

urlpatterns = [
    path("", estudos.listar_topicos, name="listar_topicos"),
    path("criar/", estudos.criar_topico, name="criar_topico"),
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)