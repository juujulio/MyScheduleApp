from datetime import date

class Timeline:
    """
        A class that instance the timeline to put the events

    """

    def __init__(self):
        self.__current_year = self.__StartPoint('year')
        self.__current_month = self.__StartPoint('month')
        self.__current_day = self.__StartPoint('day')
        print(self.__current_day, self.__current_month, self.__current_year)
        pass

    @staticmethod
    def __StartPoint(control):
        current_date = str(date.today()).split('-')
        if control == 'year':
            return current_date[0]
        if control == 'month':
            return current_date[1]
        if control == 'day':
            return current_date[2]
        pass