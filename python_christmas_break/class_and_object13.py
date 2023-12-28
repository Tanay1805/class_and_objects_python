from collections import Counter

def word_frequency(input_text):
    words = input_text.split()

    word_counts = Counter(words)

    sorted_words = sorted(word_counts.items())

    return sorted_words

if __name__ == "__main__":
    input_text = input("Enter the text: ")

    result = word_frequency(input_text)

    print("\nWord Frequency (Alphanumerically Sorted):")
    for word, frequency in result:
        print(f"{word}: {frequency}")
