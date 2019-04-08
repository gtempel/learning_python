#! /usr/bin/env python3

import functools

def count_words(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


def my_map_reduce(documents):
    # for each document generate a map of the word frequencies as a dictionary,
    # thus we're going to get a set of dictionaries
    counts = map(count_words, documents)

    # combine each of those dictionaries into a single
    total_counts = functools.reduce(combine_counts, counts)
    print(f"counts across the documents -> {total_counts}")


def main():
    documents = [
        'It was the best of times, it was the worst of times',
        'I went to the wodds because I wished to live deliberately',
        'Friend, Romans, Countrymen, lend me your ears; I come to bury Caesar, not praise him',
        'I do not like green eggs and ham. I do not like them, Sam-I-Am.'
    ]
    my_map_reduce(documents)

if __name__ == '__main__':
    main()
