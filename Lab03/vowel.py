def main():
    text = input('Enter a string: ')
    vowels = "aeiou"

    # Loop through vowels and count each one
    total_vowels = 0
    for vowel in vowels:
        count = count_letter(text, vowel)
        print(f"The number of '{vowel}'s is: {count}")
        total_vowels += count

    # Print the total number of vowels
    print(f"The total number of vowels is: {total_vowels}")


def count_letter(text, letter):
    counter = 0
    for let in text.lower():
        if let == letter:
            counter += 1
    return counter


if __name__ == '__main__':
    main()
