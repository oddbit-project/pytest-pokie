import sys
import pytest
import os

_pokie_di = None
_pokie_di_const = {
    'DI_CONFIG': 'config',
    'DI_FLASK': 'app',
    'DI_APP': 'main',
    'DI_DB': 'db'
}


def pytest_configure():
    global _pokie_di

    # attempt to extract Flask application from the main namespace
    pokie_ns = os.getenv('POKIE_NAMESPACE', '__main__')
    pokie_app = os.getenv('POKIE_APP', 'app')

    # validate namespace
    if pokie_ns not in sys.modules.keys():
        raise RuntimeError("Error: cannot find pokie namespace '{}'".format(pokie_ns))
    app = getattr(sys.modules[pokie_ns], pokie_app)

    # validate object
    if app is None:
        raise RuntimeError("Error: cannot find flask object '{}' in namespace '{}'".format(pokie_app, pokie_ns))
    _pokie_di = app.di


@pytest.fixture(scope="session", autouse=True)
def pokie_app():
    global _pokie_di
    yield _pokie_di.get(_pokie_di_const['DI_APP'])


@pytest.fixture(scope="session", autouse=True)
def pokie_flask():
    global _pokie_di
    yield _pokie_di.get(_pokie_di_const['DI_FLASK'])


@pytest.fixture(scope="session", autouse=True)
def pokie_di():
    global _pokie_di
    yield _pokie_di


@pytest.fixture(scope="session", autouse=True)
def pokie_config():
    global _pokie_di
    yield _pokie_di.get(_pokie_di_const['DI_CONFIG'])


@pytest.fixture(scope="session", autouse=True)
def pokie_db():
    global _pokie_di
    yield _pokie_di.get(_pokie_di_const['DI_DB'])


@pytest.fixture(scope="session", autouse=True)
def pokie_client():
    yield _pokie_di.get(_pokie_di_const['DI_FLASK']).test_client()
