search_word_count = input('Enter the word: ')
file = open("file function theory.txt", "r")
read_data = file.read()
word_count = read_data.lower().count(search_word_count)
print(f"The word '{search_word_count}' appeared {word_count} times.")
