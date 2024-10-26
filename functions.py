import string

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    return(list(set(lst)))

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    up_count = 0
    low_count = 0

    for char in string:
        if char.islower():
            low_count += 1
        elif char.isupper():
            up_count += 1
    return (f"Uppercase count: {up_count}", f"Lowercase count: {low_count}")

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    return sentence

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """

    sentence = sentence.translate(str.maketrans("", "", string.punctuation)).split(" ")
    new_sentence = []
    for word in sentence:
        if word.isalpha():
            new_sentence.append(word)
    return(len(new_sentence))