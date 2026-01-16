wins = 0
loses = 0
all_matches = 0

while True:
    name_comp = input()
    if name_comp == "End of tournaments":
        break

    num_matches = int(input())
    all_matches += num_matches

    for match in range(1, num_matches + 1):
        points_desi = int(input())
        points_opp = int(input())

        if points_desi > points_opp:
            wins += 1
            print(f"Game {match} of tournament {name_comp}: win with {points_desi-points_opp} points.")
        else:
            loses += 1
            print(f"Game {match} of tournament {name_comp}: lost with {points_opp-points_desi} points.")

perc_wins = (wins / all_matches) * 100
perc_loses = (loses / all_matches) * 100

print(f"{perc_wins:.2f}% matches win")
print(f"{perc_loses:.2f}% matches lost")