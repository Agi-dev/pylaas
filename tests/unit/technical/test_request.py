from pylaas_core.abstract.abstract_service_unit_test import AbstractServiceUnitTest
from pylaas.technical.request import Request
from pylaas import Debug


class TestRequest(AbstractServiceUnitTest):
    """
    Request Tests Suite
    """
    _service_id = 'request'

    def s(self):
        """
            return date service from container
        Returns:
            Request
        """
        return self._service
