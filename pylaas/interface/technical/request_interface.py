import abc

from pylaas.models.technical.request.response import Response


class RequestInterface(abc.ABC):

    @abc.abstractstaticmethod
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

    @abc.abstractstaticmethod
    def reset_session(self) -> None:
        """
        Reset session
        Returns:
            None
        """

    @abc.abstractstaticmethod
    def get(self, url, **kwargs) -> Response:
        """
        Sends a GET request.
        Args:
            url (str): full url if no session else complete url part
            **kwargs:  Optional arguments that ``request`` takes.

        Returns:
            Response
        """
