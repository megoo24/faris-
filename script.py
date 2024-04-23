import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

def read_file_contents(filename):
    """Reads the entire contents of a file and returns it."""
    try:
        with open(filename, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def remove_stop_words(text):
    """Removes stop words from the given text and returns the cleaned text."""
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return filtered_text

def count_word_frequencies(words):
    """Counts the frequency of each word in the list of words and returns a dictionary."""
    return Counter(words)

# Specify the filename
filename = "random_paragraphs.txt"

# Read the contents of the file
file_contents = read_file_contents(filename)

# Remove stop words from the contents
filtered_words = remove_stop_words(file_contents)

# Count the frequency of each word
word_frequencies = count_word_frequencies(filtered_words)

# Print word frequencies
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
