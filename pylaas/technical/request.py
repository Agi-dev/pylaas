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
        reset session
        Returns:
            None
        """
        self._url = None
        self._session = None

    def get(self, page, **kwargs) -> Response:
        try:
            if self._session is not None:
                response = self._session.get('{}{}'.format(self._url, page))
            else:
                response = requests.get(page, **kwargs)
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
