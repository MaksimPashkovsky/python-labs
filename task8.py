from collections import namedtuple


def days_till_dayoff(current_day: str):
    Day = namedtuple('day', 'name, is_dayoff')

    days = [Day('понедельник', False),
            Day('вторник', False),
            Day('среда', False),
            Day('четверг', False),
            Day('пятница', False),
            Day('суббота', True),
            Day('воскресенье', True)]
    index = days.index(next(filter(lambda x: x.name == current_day.lower(), days)))

    counter = 1
    while True:
        index = (index + 1) % len(days)
        if days[index].is_dayoff:
            return counter
        counter += 1


print(days_till_dayoff(input()))
