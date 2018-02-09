from pylaas_core.abstract.abstract_service_integration_test import AbstractServiceIntegrationTest
from pylaas.technical.request import Request
from pylaas import Debug
import pytest
import requests


class TestRequest(AbstractServiceIntegrationTest):
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

    """
    init_session
    """
    def test_init_session_with_invalid_url_raise(self):
        with pytest.raises(RuntimeError, match="Invalid url 'http//foobar.d'"):
            self.s().init_session('http//foobar.d')

    def test_init_session_success(self):
        self.s().init_session('http://url.com', headers={'x-test': 'true'})
        assert isinstance(self.s()._session, requests.Session)
        assert self.s()._url == 'http://url.com'

    """
    reset_session
    """
    def test_reset_session_success(self):
        self.s().init_session('http://url.com')
        self.s().reset_session()
        assert self.s()._session is None
        assert self.s()._url is None
    """
    get
    """
    def test_get_failed(self):
        actual = self.s().get('http://httpbin.org/post').__dict__
        self.assert_equals_resultset(actual)

    def test_get_success_return_dict(self):
        actual = self.s().get('http://httpbin.org/get').__dict__
        actual['_content']['headers']['User-Agent'] = "pytest-user_agent"
        actual['_content']['origin'] = "pytest"
        self.assert_equals_resultset(actual)

    def test_get_with_timeout_return_503(self):
        actual = self.s().get('https://httpbin.org/delay/3', timeout=0.001).__dict__
        self.assert_equals_resultset(actual)

    def test_get_with_session_and_auth_success(self):
        self.s().init_session('http://httpbin.org/', auth=('anUser', 'aPassword'))
        actual = self.s().get('/basic-auth/anUser/aPassword').__dict__
        self.assert_equals_resultset(actual)