def count_words(text):
    """
    Accepts text as a parameter, and returns a dictionary of the word lengths in it.

    Args:
    - text (str): A string of text to be processed.

    Returns:
    - (dict): A dictionary containing word-count pairs, where each word is a key and its value
    is the length of the word.
    """
    # In order to clean the text from non-letter characters
    text = ''.join(ch for ch in text if ch.isalpha() or ch.isspace())
    words_and_lengths = {word: len(word) for word in text.split()}
    return words_and_lengths


print(count_words(text="""
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""))
