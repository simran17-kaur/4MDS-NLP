# LAB 1- Text Processing and Regular Expression
#Date: 19th June, 2025

# Name: Simran Kaur
# Reg.No: 2448051


#Q1

#Installing NLTK, NLTK.book

import nltk # type: ignore
nltk.download()
from nltk.book import * # type: ignore
nltk.download('punkt_tab') #Downloads the 'punkt_tab' tokenizer table used by NLTK for sentence and word tokenization

#Exercise 1- Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).
print(12/(4+1))

#Exercise 2- Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form. That works out to 141167095653376. How many hundred-letter strings are possible?
#The value of 26^100 represents the total number of possible hundred-letter strings using the 26-letter English alphabet.

print("*************************************************************************")


#Q2

from nltk.tokenize import word_tokenize # type: ignore
from nltk import FreqDist # type: ignore

#a- Define a string containing a paragraph as the value.

para="Crochet is a creative, creative, and artistic textile art. Crochet uses a hooked needle, a hooked needle, to loop yarn, loop yarn into fabric. Crochet allows for making items—craftsmanly items, practical items, and handmade items—like clothing, clothing, blankets, and toys. Unlike knitting, crochet uses one hook, one hook, and various stitch patterns. Crochet offers versatility, handicrafts, and ease for beginners and advanced crafters alike. Friendships formed through crochet are long-lasting and warm."


#b-Write a program to print the number of total words and total unique words in the paragraph.

words=word_tokenize(para)
total=len(words)
uniquewords=len(set(words))
print("Total words= ",total)
print("Unique words= ",uniquewords)
#This considers punctuations as seperate strings.


#c-Find the frequency of all words and also display the most and least frequent word.

fdist=FreqDist(words)
print("Word Frequencies: ",fdist)
print(fdist.most_common())

#most frequent word
#get the first tuple i.e. most frequently occurring word and its no of occurrences
most_freq = fdist.most_common(1)[0]    
print("Most Common Word:", most_freq[0], "(", most_freq[1], " times )")

#least frequent word
min_freq= min(fdist.values())
print("Least Common Words: ")
for word in fdist:
    if fdist[word]==min_freq:
        print(word, "(", min_freq, "time(s) )")


#d- Find the longest word in the paragraph.

#Filter out punctuation (keeping only alphabetic tokens)
filtered_words = []
for word in words:
    if word.isalpha():   #checks whether all characters in the word are alphabetic i.e. only letters A-Z or a-z, no numbers, no punctuation, no symbols)
        filtered_words.append(word)

#single longest word        
longest_word=max(filtered_words, key=len)
print("Longest Word: ",longest_word)

#incase of ties i.e there are more than one words with the same length
max_len=max(len(word) for word in filtered_words)
longest_words=[]
for word in words:
    if len(word) == max_len:
        longest_words.append(word)
print("Longest words: ", longest_words)

print("*************************************************************************")


#Q3


#2.1 Write regular expressions for the following languages:

import re
# 1. Set of all alphabetic strings
def is_alphabetic(s):
    return bool(re.fullmatch(r'[A-Za-z]+', s))

# 2. Set of all lowercase alphabetic strings ending in a 'b'
def is_lowercase_ending_b(s):
    return bool(re.fullmatch(r'[a-z]*b', s))

# 3. All strings from {a, b} where each 'a' is surrounded by 'b'
def valid_a_surrounded_by_b(s):
    return bool(re.fullmatch(r'(b+|bab)*', s))

#Test cases
print("Test Cases (2.1)")
print("1. is_alphabetic")
print(is_alphabetic("HelloWorld"))     # True
print(is_alphabetic("Hello123"))       # False
print()

print("2. is_lowercase_ending_b")
print(is_lowercase_ending_b("crabb"))  # True
print(is_lowercase_ending_b("helloB")) # False
print()

print("3. each a is immediately preceded by and immediately followed by a b")
print(valid_a_surrounded_by_b("bab"))      # True
print(valid_a_surrounded_by_b("bbbabbb"))  # True
print(valid_a_surrounded_by_b("ab"))       # False
print(valid_a_surrounded_by_b("ba"))       # False
print()



#2.2

# 1. Two repeated words
def has_repeated_word(s):
    return bool(re.search(r'\b([A-Za-z]+)\b\s+\1\b', s))

# 2. Starts with integer, ends with word
def starts_int_ends_word(s):
    return bool(re.fullmatch(r'\d+.*\b[A-Za-z]+\b', s))

# 3. Contains both 'grotto' and 'raven' as words
def contains_grotto_and_raven(s):
    return bool(re.search(r'(?=.*\bgrotto\b)(?=.*\braven\b)', s, re.IGNORECASE))

# 4. Extract first word of a sentence (with punctuation)
def extract_first_word(sentence):
    match = re.match(r'^["\'(\[]?([A-Z][a-z]+)', sentence)
    return match.group(1) if match else None


#Test cases
print("Test Cases (2.2)")

print("1. has_repeated_word")
print(has_repeated_word("the the bug"))         # True
print(has_repeated_word("Humbert Humbert"))     # True
print(has_repeated_word("big bug"))             # False
print()

print("2. starts_int_ends_word")
print(starts_int_ends_word("2025 summer"))      # True
print(starts_int_ends_word("hello 1234"))       # False
print()

print("3. contains_grotto_and_raven")
print(contains_grotto_and_raven("The raven flew into the grotto."))     # True
print(contains_grotto_and_raven("grottos are near caves with ravens"))  # False (grottos ≠ grotto)
print()

print("4. extract_first_word")
print(extract_first_word('"Humbert Humbert was a man."'))  # Humbert
print(extract_first_word("Once upon a time"))              # Once
print(extract_first_word("(Hello world!)"))                # Hello
print()

print("*************************************************************************")


#ADDITIONAL QUESTIONS

#Practice Q1-Text Normalization
#Perform EDA operation for the text file containing a chapter of a text book or story book.
import nltk # type: ignore
import re     
import string
import matplotlib.pyplot as plt # type: ignore
from nltk.corpus import stopwords # type: ignore
from nltk.tokenize import word_tokenize, sent_tokenize # type: ignore
from nltk.stem import WordNetLemmatizer # type: ignore
from nltk import FreqDist # type: ignore

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

import os

print("Current directory:", os.getcwd())
print("Files in this directory:", os.listdir())

with open("The Last Train.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().lower()

clean_text = re.sub(r"\d+", " ", raw_text).translate(str.maketrans("", "", string.punctuation))
tokens = word_tokenize(clean_text)
stop_set = set(stopwords.words("english"))
tokens = [w for w in tokens if w.isalpha() and w not in stop_set]
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(w) for w in tokens]

sentences = sent_tokenize(raw_text)
num_sentences = len(sentences)
avg_sentence_len = sum(len(word_tokenize(s)) for s in sentences) / num_sentences

fdist = FreqDist(tokens)
vocab = set(tokens)
top10 = fdist.most_common(10)

print("\n—— Text EDA Report ——")
print(f"Total sentences        : {num_sentences}")
print(f"Average sentence length: {avg_sentence_len:.2f} words")
print(f"Total word tokens      : {len(tokens)}")
print(f"Vocabulary size        : {len(vocab)}")
print("Top 10 words           :", top10)

plt.figure(figsize=(10, 4))
fdist.plot(20, title="Top 20 Most Common Words")

word_lengths = [len(w) for w in tokens]
plt.figure(figsize=(8, 4))
plt.hist(word_lengths, bins=range(1, max(word_lengths) + 1), edgecolor="black")
plt.title("Word-Length Distribution")
plt.xlabel("Word length")
plt.ylabel("Frequency")
plt.tight_layout()


print("*************************************************************************")


#Practice 2- From TextBook Exercises: Steve Bird and team
# Load text6 (Chat Corpus)
from nltk.book import text6   # type: ignore


#24-Write expressions for finding all words in text6 that meet the conditions listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].

import nltk    # type: ignore
nltk.download('nltk_data')
nltk.download('gutenberg')
from nltk.book import *   # type: ignore

#a- Words ending in "ize"
words_ending_ize = [w for w in set(text6) if w.endswith("ize")]
print(words_ending_ize)

#b- Words containing the letter "z"
words_with_z = [w for w in set(text6) if "z" in w.lower()]
print(words_with_z)

#c-Words containing the sequence "pt"
words_with_pt = [w for w in set(text6) if "pt" in w.lower()]
print(words_with_pt)

#d-Words in Titlecase (only first letter capitalized)
titlecase_words = [w for w in set(text6) if w.istitle()]
print(titlecase_words)



#25-Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. Now write code to perform the following tasks:

#Define the list
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

#a. Print all words beginning with 'sh'
sh_words = [word for word in sent if word.startswith('sh')]
print("Words beginning with 'sh':", sh_words)

#b. Print all words longer than four characters
long_words = [word for word in sent if len(word) > 4]
print("Words longer than 4 characters:", long_words)



#26-What does the following Python code do? sum(len(w) for w in text1) Can you use it to work out the average word length of a text?
#ANS: It returns the total number of characters in text1, assuming text1 is a list of words.
#Yes. You can compute the average word length as:
text = "Cricket is more than just a game; cricket unites fans across nations. Cricket matches, whether Tests or T20s, bring people together. The spirit of cricket is seen in every thrilling over and strategic play. Cricket, with its rich history and passionate followers, continues to grow in popularity worldwide." 
words = text.split()
# Calculate average word length
avg_word_len = sum(len(w) for w in words) / len(words)
print("Average word length:", avg_word_len)

#27-Define a function called vocab_size(text) that has a single parameter for the text, and which returns the vocabulary size of the text.
def vocab_size(text):
    return len(set(text))
print("Vocabulary Size: ", vocab_size(text))

#28. Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.
def percent(word, text):
    # Normalize case and tokenize
    words = text.lower().split()
    # Remove punctuation from each word
    words = [w.strip(string.punctuation) for w in words]
    # Count occurrences
    word = word.lower()
    return 100 * words.count(word) / len(words)
print("No. of words in text:", len(text.split()))
print("Count of word cricket:", text.lower().count("cricket"))
print("Percentage of occurrences of a particular word: ", percent("Cricket", text))


print("*************************************************************************")