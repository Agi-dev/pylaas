import abc


class DateInterface(abc.ABC):

    # day number
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    @staticmethod
    @abc.abstractstaticmethod
    def previous_weekday(d, seeking_day):
        """
        Determine the first previous weekday from a date

        Args:
            d (obj:`Arrow`): arrow date to search from
            seeking_day (int):  seeking day num (use Date.MON, Date.TUE ...)

        Returns:
            Arrow: date to previous seeking day
        """
        pass

    @staticmethod
    @abc.abstractstaticmethod
    def next_weekday(d, seeking_day):
        """
        Determine the first next weekday from a date

        Args:
            d (obj:`Arrow`): arrow date to search from
            seeking_day (int):  seeking day num (use Date.MON, Date.TUE ...)

        Returns:
            Arrow: date to previous seeking day
        """