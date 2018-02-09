import json


class Response:
    """Request Response Model"""

    def __init__(self, response=None, success=None, content=None, status_code=None):
        """
        Args:
            response (requests.Response)
        """
        if response is not None:
            if response.ok:
                try:
                    self._content = self._convert_json(response.content)
                except ValueError:
                    self._content = response.content
            else:
                self._content = response.reason

            self._success = response.ok
            self._status_code = response.status_code
        else:
            self._success = success
            self._status_code = status_code
            self._content = self._convert_json(content)

    @property
    def content(self):
        """dict: response content"""
        return self._content

    @property
    def success(self):
        """bool: request succeeded ?"""
        return self._success

    @property
    def status_code(self):
        """int: status code"""
        return self._status_code

    @staticmethod
    def _convert_json(content):
        """
        convert content if is json
        Args:
            content (str):

        Returns:
            str
        """
        try:
            return json.loads(content)
        except ValueError:
            return content
