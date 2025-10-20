#!/usr/bin/env python3

# Word frequency exercise
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

# This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True


def get_sentence():
    # Prompt the user and validate the sentence
    user_sentence = input("Enter a sentence: ")

    while is_sentence(user_sentence) == False:
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")

    return user_sentence


def calculate_frequencies(user_sentence):
    # Step 1: Split into words
    list1 = user_sentence.split()

    # Step 2: Clean each word (remove punctuation + lowercase)
    for i in range(len(list1)):
        list1[i] = re.sub(r'[^\w]', '', list1[i])  # remove punctuation
        list1[i] = list1[i].lower()                # make lowercase

    # Step 3: Create two lists
    words = []   # unique words
    freqs = []   # word counts

    # Step 4: Count words using for...else
    for word in list1:
        for j in range(len(words)):
            if words[j] == word:
                freqs[j] += 1
                break
        else:
            words.append(word)
            freqs.append(1)

    return words, freqs


def print_frequencies(words, freqs):
    # Step 5: Print results (kept identical to original)
    for i in range(len(words)):
        print(words[i], ":", freqs[i])


def main():
    # Control the overall program flow
    user_sentence = get_sentence()
    words, freqs = calculate_frequencies(user_sentence)
    print_frequencies(words, freqs)

# calls main
main()
