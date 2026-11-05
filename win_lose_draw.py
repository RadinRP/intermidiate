def score (team):
    count = 0
    for scores in team:
        if scores == "w":
            count += 3
        elif scores == "d":
            count += 1
    return count