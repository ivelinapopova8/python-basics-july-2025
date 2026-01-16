min_walking = int(input())
num_walks = int(input())
calories = int(input())

NEED_BURN = 0.5 * calories

burn_calories = (min_walking * 5) * num_walks

if burn_calories >= NEED_BURN:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")