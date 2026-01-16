from math import floor

the_most_powerfull_word = ""
the_most_points = 0
vowels = "aeiouyAEIOUY"

while True:
    word = input()
    points = 0

    if word == "End of words":
        break

    for char in word:
        points += ord(char)

    if word[0] in vowels:
        points = points * len(word)
    else:
        points = floor(points / len(word))

    if points > the_most_points:
        the_most_points = points
        the_most_powerfull_word = word

print(f"The most powerful word is {the_most_powerfull_word} - {the_most_points}")


