import sys


def clean_text(text):
    """
    remove punctuation form a text
    """

    punctuation = "+.*/?,;\'#"
    for p in punctuation:
        text = text.replace(p, "")
    return text


def tokenize(text):
    """
    Convert text into tokens, return a list of tokens(words)
    """
    return text.split()


# this is error
def tokenize2(text):
    """
    Convert text into tokens, return a list of tokens(words)
    """
    spaces = " "
    words = text.split(spaces)
    return words


def word_freq(words):
    """
    Counts words and return a dictionary of words with their occurrences
    """
    index = {}
    for w in words:
        if w in index:
            index[w] += 1
        else:
            index[w] = 1
    return index


def most_common_word(words_freq_table):
    """
    Counts words and return a dictionary of words with their occurrences
    """
    frequent = ""
    frequency = 0
    for word in words_freq_table:
        if words_freq_table[word] > frequency:
            frequent = word
            frequency = words_freq_table[word]
    return frequent


def read_file(filename):
    """
    Read a text from file
    """
    try:
        fl = open(filename, "r")
    except:
        print("Can't open file ", filename)
        sys.exit()
    # if success
    return fl


def main():
    text = "Surprise steepest recurred landlord mr wandered amounted of. Continuing de"
    text = clean_text(text)
    print(text)

    # tokenize text

    words = tokenize(text)
    print(words)
    words = tokenize2(text)
    print(words)
    words_nb = word_freq(words)
    print(words_nb)
    data = read_file("test/data.txt")
    print(data)
    text = data
    words = tokenize(text)
    print(words)
    word_freq_table = word_freq(words)
    print(word_freq_table)
    freqw = most_common_word(word_freq_table)
    print('most frequent word is: '
          '{}\nthe number of repeat is :{}'.format(freqw, word_freq_table[freqw]))
    return 0


if __name__ == "__main__":
    main()
