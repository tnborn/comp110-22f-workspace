"""EX01 - Chardle - Wordle."""
__author__ = "730563181"


original_word: str = input("Enter a 5-character word: ")
if len(original_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character_one: str = input("Enter a single character: ")
if len(character_one) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character_one + " in " + original_word)
if character_one == original_word[0]:
    print(character_one + " found at index 0")
if character_one == original_word[1]:
    print(character_one + " found at index 1")
if character_one == original_word[2]:
    print(character_one + " found at index 2")
if character_one == original_word[3]:
    print(character_one + " found at index 3")
if character_one == original_word[4]:
    print(character_one + " found at index 4")

counter = 0
for c in original_word:
    if c == character_one:
        counter += 1
if counter >= 2:
    print(counter, "instances of " + character_one + " found in " + original_word)
if counter == 1:
    print(counter, "instance of " + character_one + " found in " + original_word)
if counter == 0: 
    print("No instances of " + character_one + " found in " + original_word)