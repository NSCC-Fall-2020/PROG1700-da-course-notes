
import pytest
import nbimporter

from unit_testing import *


def test_add():
    try:
        # test that 1 + 2 = 3
        assert add(1,2) == 3

        # test that 2 + 3 = 5
        assert add(2,3) == 5

        # test that 0 + 0 = 0
        assert add(0,0) == 0
    except NameError:
        pytest.fail("I couldn't find the 'add' function.", False)