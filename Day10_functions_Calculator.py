# Functions return something

def is_leap_year(year: int):
    """"
    This function calculates the Leap year input is year and output is Boolean
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Call your function with hard coded values
print(is_leap_year(1989))
