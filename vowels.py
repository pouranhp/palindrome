def is_vowel(char):
    vowels = "aeiou"
    return char in vowels


def count_pronunciations(word):
    count = 1

    for i in range(len(word)):
        current_char = word[i]

        if is_vowel(current_char):
            count *= 2

    return count


def main():
    word = input().strip()
    result = count_pronunciations(word)
    print(result)


if __name__ == "__main__":
    main()
