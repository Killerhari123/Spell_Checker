import nltk
import difflib

# Download the NLTK words corpus if not already downloaded.
nltk.download('words')

# Load a set of English words from the NLTK corpus.
english_words = set(nltk.corpus.words.words())

def correct_word(word):
    """
    Check if a word is spelled correctly.
    If not, use difflib to suggest the closest match.
    """
    # Check if the word (in lowercase) is in our dictionary.
    if word.lower() in english_words:
        return word  # Word is correct.
    
    # Use difflib to find close matches in our dictionary.
    # The cutoff value (0.8) defines how close a match should be.
    matches = difflib.get_close_matches(word.lower(), english_words, n=1, cutoff=0.7)
    
    if matches:
        # Return the suggested correction (first close match).
        return matches[0]
    else:
        # If no close match is found, return the original word.
        return word

def spell_check_sentence(sentence):
    """
    Spell-checks a sentence word-by-word.
    Returns a new sentence with corrected words.
    """
    # Split the sentence into words.
    words = sentence.split()
    # Correct each word using our helper function.
    corrected_words = [correct_word(word) for word in words]
    # Join the corrected words back into a single string.
    return ' '.join(corrected_words)

if __name__ == '__main__':
    # Get a sentence input from the user.
    sentence = input("Enter a sentence: ")
    # Obtain the spell-checked sentence.
    corrected_sentence = spell_check_sentence(sentence)
    print("Corrected sentence:", corrected_sentence)
