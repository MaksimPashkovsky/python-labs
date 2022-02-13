def cat_dog_years(human_years: int):
    years_sum = list(map(lambda x: (15, 15) if x == 1 else (9, 9) if x == 2 else (4, 5), range(1, human_years + 1)))
    return [human_years, *list(map(lambda x: sum(x), list(zip(*years_sum))))]


print(cat_dog_years(3))
