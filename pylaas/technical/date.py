import copy

from pylaas_core.abstract.abstract_service import AbstractService

from pylaas.interface.technical.date_interface import DateInterface


class Date(AbstractService, DateInterface):
    """Service Date"""

    @staticmethod
    def previous_weekday(d, seeking_day):
        """
        Determine the first previous weekday from a date

        Args:
            d (obj:`Arrow`): arrow date to search from
            seeking_day (int):  seeking day num (use Date.MON, Date.TUE ...)

        Returns:
            Arrow: date to previous seeking day
        """
        current_day = int(d.format('d'))
        previous_date = copy.copy(d)

        if current_day == seeking_day:
            return d
        if current_day > seeking_day:
            nb_day = seeking_day - current_day
        else:
            nb_day = seeking_day - current_day - 7

        return previous_date.shift(days=nb_day)

    @staticmethod
    def next_weekday(d, seeking_day):
        """
        Determine the first next weekday from a date

        Args:
            d (obj:`Arrow`): arrow date to search from
            seeking_day (int):  seeking day num (use Date.MON, Date.TUE ...)

        Returns:
            Arrow: date to previous seeking day
        """
        current_day = int(d.format('d'))
        next_date = copy.copy(d)

        if current_day == seeking_day:
            return d
        if current_day < seeking_day:
            nb_day = seeking_day - current_day
        else:
            nb_day = seeking_day - current_day + 7

        return next_date.shift(days=nb_day)
