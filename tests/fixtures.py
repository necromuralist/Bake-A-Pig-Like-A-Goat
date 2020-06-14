# pypi

from pytest import fixture


class Katamari:
    """Something to stick things into"""



@fixture
def katamari():
    return Katamari()
