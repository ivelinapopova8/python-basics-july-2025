start_letter = input()
end_letter = input()
skip_letter = input()

count = 0

start = ord(start_letter)
end = ord(end_letter)
skip = ord(skip_letter)

for letter_1 in range(start, end + 1):
    if letter_1 == skip:
        continue

    for letter_2 in range(start, end + 1):
        if letter_2 == skip:
            continue

        for letter_3 in range(start, end + 1):
            if letter_3 == skip:
                continue


            print(chr(letter_1) + chr(letter_2) + chr(letter_3), end = " ")
            count += 1
print(count)

