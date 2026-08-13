📄 Sentence Processing Pipeline
A simple Python program that demonstrates function chaining, string processing, and basic error handling.
The program takes a sentence from the user, converts it to lowercase, removes punctuation, splits it into words, counts them, and displays the final word count.

🚀 Features
User input handling

Lowercasing text

Removing punctuation

Splitting text into words

Counting words manually

Function‑to‑function pipeline (each function calls the next)

Basic assertions and try/except blocks for safety

🧠 How It Works
The program follows a linear pipeline:

take_input()

Gets a sentence from the user

Passes it to lower_sentence()

lower_sentence()

Converts the sentence to lowercase

Passes it to remove_punctuation()

remove_punctuation()

Removes common punctuation characters

Passes cleaned text to split_words()

split_words()

Splits the cleaned sentence into a list of words

Passes the list to count_words()

count_words()

Counts the number of words manually

Passes the count to display_result()

display_result()

Prints the final word count
