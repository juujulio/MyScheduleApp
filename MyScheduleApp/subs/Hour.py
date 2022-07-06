def treat_format(hour, minutes):
    if type(hour) != int:
        raise Exception("Please choose a valid hour (0 ~ 23h).")
    if hour < 0 or hour > 23:
        raise Exception("Please choose a valid hour (0 ~ 23h).")
    if type(minutes) != int:
        raise Exception("Please choose a valid number for minutes (0 ~ 59min).")
    if minutes < 0 or minutes > 59:
        raise Exception("Please choose a valid number for minutes (0 ~ 59min).")
    else:
        print("Correct Hour")
    pass


class Hour:
    def __init__(self, hour, minutes):
        self.__hour = hour
        self.__minutes = minutes
        treat_format(self.__hour, self.__minutes)
        pass

    def get_hour(self):
        hour = str(self.__hour) + ":" + str(self.__minutes)
        return hour
