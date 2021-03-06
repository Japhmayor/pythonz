import os

import pytest
from pytest_djangoapp import configure_djangoapp_plugin

# Используем имитатор вместо uwsgi.
os.environ['UWSGICONF_FORCE_STUB'] = '1'

pytest_plugins = configure_djangoapp_plugin(
    settings='pythonz.settings.env_testing',
    admin_contrib=True,
    migrate=False,
)

from django.conf import settings


@pytest.fixture
def robot(user_create):
    """Возвращает объект пользовтеля-робота (суперпользователь)."""
    yield user_create(attributes={'id': settings.ROBOT_USER_ID}, superuser=True)


@pytest.fixture
def mock_get_location(monkeypatch):
    monkeypatch.setattr(
        'pythonz.apps.models.place.get_location_data', lambda location_name: {})
