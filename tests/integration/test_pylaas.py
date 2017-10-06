import pytest

from pylaas.pylaas import Pylaas


class TestPylaas:
    """
    Pylaas Tests Suite
    """

    """
    __new__
    """

    def test_new_raise_TypeError(self):
        """Test unique instance creation"""
        with pytest.raises(TypeError):
            Pylaas()

    """
    init
    """

    def test_init_success(self):
        Pylaas.init()
        assert 'services' in Pylaas.get_container().get_definitions()
