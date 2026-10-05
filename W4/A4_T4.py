print("Program starting.")
word_count = 0
char_count = 0

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    word_count += 1
    char_count += len(word)

print(f"You inserted:\n- {word_count} words\n- {char_count} characters")
print("Program ending.")