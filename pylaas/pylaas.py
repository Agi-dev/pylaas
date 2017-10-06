"""
Pylaas

Examples:
    import pylaas
    Pylaas.init()

"""
import inspect
import os
from pylaas_core.pylaas_core import PylaasCore


class Pylaas(PylaasCore):
    """
    Pylaas Library as a service
    """

    @classmethod
    def init(cls):
        """
        init Pylaas

        """
        current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        super()._init("{}/../conf/definitions.yml".format(current_path))
