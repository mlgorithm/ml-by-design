from collections import Counter


def unigram_counts(sentence):
    return Counter(sentence.split())


def bigram_counts(sentence):
    tokens = sentence.split()
    return Counter(zip(tokens, tokens[1:]))


def main():
    sentence_a = "dog bites man"
    sentence_b = "man bites dog"

    print("Sentence A:", sentence_a)
    print("Sentence B:", sentence_b)
    print()

    print("Unigram counts")
    print("  A:", dict(unigram_counts(sentence_a)))
    print("  B:", dict(unigram_counts(sentence_b)))
    print()

    print("Bigram counts")
    print("  A:", dict(bigram_counts(sentence_a)))
    print("  B:", dict(bigram_counts(sentence_b)))
    print()

    same_unigrams = unigram_counts(sentence_a) == unigram_counts(sentence_b)
    same_bigrams = bigram_counts(sentence_a) == bigram_counts(sentence_b)
    print(f"Same unigram representation? {same_unigrams}")
    print(f"Same bigram representation? {same_bigrams}")


if __name__ == "__main__":
    main()
