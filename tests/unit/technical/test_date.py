import arrow
import tests.unit.bootstrap
from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas.technical.date import Date

from pylaas.pylaas import Pylaas


class TestDate(AbstractTestCase):
    """Test Lib Date Suite"""

    def setup_method(self, method):
        TestDate._service = Pylaas.get_service('date')

    @staticmethod
    def s():
        """
            return date service from container
        Returns:
            Date
        """
        return TestDate._service

    """
    previous_weekday
    """

    def test_previous_weekday_with_date_equals_seeking_day(self):
        actual = self.s().previous_weekday(arrow.get('2017-10-04'), Date.WED)
        expected = arrow.get('2017-10-04')
        assert expected == actual

    def test_previous_weekday_with_date_after_seeking_day(self):
        actual = self.s().previous_weekday(arrow.get('2017-10-06'), Date.WED)
        expected = arrow.get('2017-10-04')
        assert expected == actual

    def test_previous_weekday_with_date_before_seeking_day(self):
        actual = self.s().previous_weekday(arrow.get('2017-10-03'), Date.WED)
        expected = arrow.get('2017-09-27')
        assert expected == actual

    """
    next_weekday
    """

    def test_next_weekday_with_date_equals_seeking_day(self):
        actual = self.s().next_weekday(arrow.get('2017-10-04'), Date.WED)
        expected = arrow.get('2017-10-04')
        assert expected == actual

    def test_next_weekday_with_date_after_seeking_day(self):
        actual = self.s().next_weekday(arrow.get('2017-10-06'), Date.WED)
        expected = arrow.get('2017-10-11')
        assert expected == actual

    def test_next_weekday_with_date_before_seeking_day(self):
        actual = self.s().next_weekday(arrow.get('2017-10-03'), Date.WED)
        expected = arrow.get('2017-10-04')
        assert expected == actual
