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

treat_format(24, 26.2)