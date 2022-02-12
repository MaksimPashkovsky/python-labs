def rank(l: list, rost: int):
    return len([a for a in l if a >= rost]) + 1


print(rank([165, 163, 160, 160, 157, 157, 155, 154], 160))
