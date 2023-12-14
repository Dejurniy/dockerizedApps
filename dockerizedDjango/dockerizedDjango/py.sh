#!/bin/bash

# Makes the structure of tables.
python manage.py makemigrations

# Creates the structure.
python manage.py migrate

# Runs the django server (0.0.0.0 means its accessible from all hosts).
python manage.py runserver 0.0.0.0:8000
