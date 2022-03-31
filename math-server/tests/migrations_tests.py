from pytest_alembic import create_alembic_fixture, tests

alembic = create_alembic_fixture({"file": "alembic.ini"})


def test_upgrade(alembic):
    tests.test_upgrade(alembic)


def test_up_down_cons(alembic):
    tests.test_up_down_consistency(alembic)


def test_single_head_revision(alembic):
    tests.test_single_head_revision(alembic)
