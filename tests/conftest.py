import pytest
import os
from .utils import UtilActions
from .seeder import Seeder


def pytest_generate_tests(metafunc):
    os.environ["DATABASE_URL"] = "postgresql://postgres@localhost/gsevpt_tests"


@pytest.fixture
def app():
    from project import app

    app.config["TESTING"] = True
    app.testing = True

    return app


@pytest.fixture
def db(app):
    from project import db
    from project.init_data import create_initial_data

    with app.app_context():
        db.drop_all()
        db.create_all()
        create_initial_data()

    return db


@pytest.fixture
def client(app, db):
    return app.test_client()


@pytest.fixture
def utils(client, app):
    return UtilActions(client, app)


@pytest.fixture
def seeder(app, db):
    return Seeder(app, db)
