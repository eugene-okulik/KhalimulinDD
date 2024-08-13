text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel.\n "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

list1 = text.split()
result = []

for individual_words in list1:
    if individual_words[-1] in ".,":
        cleaned_word = individual_words[:-1]
        result.append(cleaned_word + "ing" + individual_words[-1])
    else:
        result.append(individual_words + "ing")

print(" ".join(result))
