letter_count = {}
letters_dict = []

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
       # print(file_contents)

main()

def convert_text():
    with open("books/frankenstein.txt") as f:
        words = f.read()
        string = words.split()
        return len(string)

total = convert_text()

def count_text():
    with open("books/frankenstein.txt") as f:
        letters = f.read()
        lower_letters = letters.lower()
    for letter in lower_letters:
        if letter.isalpha() == True:
            if letter in letter_count:
                letter_count[letter] += 1
            if letter not in letter_count:
                letter_count[letter] = 1
    for letter, count in letter_count.items():
        letters_dict.append({"letter": letter,"count": count})

characters = count_text()

def sort_dict(dict):
    return dict["count"]

letters_dict.sort(reverse=True, key=sort_dict)

print("--- Begin report of books/frenakenstein.txt ---")
print(f"{total} words found in the document")
for item in letters_dict:
    print(f"The '{item['letter']}' character was found {item['count']} times")
print("--- End report ---")