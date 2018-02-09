import requests
import validators
from pylaas_core.abstract.abstract_service import AbstractService
from pylaas.interface.technical.request_interface import RequestInterface
from pylaas.models.technical.request.response import Response


class Request(AbstractService, RequestInterface):
    """Service Request"""
    _session = None
    _url = None

    def init_session(self, url, auth=None, headers=None) -> None:
        """
        Initialize session
        Args:
            url (str): base url for request
            auth (tuple): credentials (<login>, <password>)
            headers (dict): headers

        Returns:
            None
        """
        if not validators.url(url):
            raise RuntimeError("Invalid url '{}'".format(url))

        self.reset_session()
        self._session = requests.session()
        if auth is not None:
            self._session.auth = auth
        if headers is not None:
            self._session.headers = headers
        self._url = url

    def reset_session(self) -> None:
        """
        Reset session
        Returns:
            None
        """
        self._url = None
        self._session = None

    def get(self, url, **kwargs) -> Response:
        """
        Sends a GET request.
        Args:
            url (str): full url if no session else complete url part
            **kwargs:  Optional arguments that ``request`` takes.

        Returns:
            Response
        """
        try:
            if self._session is not None:
                response = self._session.get('{}{}'.format(self._url, url))
            else:
                response = requests.get(url, **kwargs)
            return self._format_response(response)
        except requests.exceptions.ConnectTimeout:
            return Response(success=False, content='Service unavailable', status_code=503)

    @staticmethod
    def _format_response(response):
        """

        Args:
            response (requests.Response):

        Returns:
            Response
        """
        return Response(response)
