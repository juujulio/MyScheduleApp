class Event:
    """
        A class that instance an event in a day.
        This class is the basic structure for build an event and fix it in a day

    """

    def __init__(self, date, hour, title):
        """
        :param date: Date
        :param hour: Hour
        :param title: String
        """
        self.__date = date
        self.__hour = hour
        self.__title = title
        pass

    def get_date(self):
        print(self.__date)
        return self.__date
        pass

    def get_hour(self):
        print(self.__date)
        return self.__hour
        pass
