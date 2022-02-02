# Remove_Ngram_Duplicates

I once had this as an interview question: remove a duplicate n-gram in a range of len > 1 < 5 from a string.

It is a common problem with the output from LLMs/transformer models such as GPT-2.

So for example: "I love you I love you so much right now" - should be - "I love you so much right now"

A hashing algorithm would definitely be faster that this NLTK n-gram-based solution, so I will provide that as a future solution (e.g. Rabin-Karp rolling hash function). But this gets the job done.
