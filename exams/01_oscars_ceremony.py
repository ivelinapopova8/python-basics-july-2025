rent = int(input())

statuets = 0.7 * rent
ketaring = 0.85*statuets
songs = ketaring / 2
sum = rent + statuets + ketaring + songs
print(f"{sum:.2f}")