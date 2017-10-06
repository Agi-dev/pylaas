import copy

from pylaas.interface.technical.date_interface import DateInterface


class Date(DateInterface):
    """Service Date"""

    # day number
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

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
