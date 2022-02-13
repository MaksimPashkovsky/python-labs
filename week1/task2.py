def years_difference(date1: str, date2: str):
    return abs(int(date1.split('/')[0]) - int(date2.split('/')[0]))


print(years_difference("1997/10/10", "2015/10/10"))
