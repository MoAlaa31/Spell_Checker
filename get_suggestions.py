from difflib import SequenceMatcher
from puble_sort import bublesort

def get_suggestions(misspilled, dictionary,n):
    """Determine the percentage of similarity between words and return dictionary its keys the misspelled words
    and the values are the suggestion words
    """
    suggestions = {}
    s = SequenceMatcher()
    for word in misspilled:
        result = []
        s.set_seq1(word)
        for w in dictionary:
            s.set_seq2(w)

            if s.real_quick_ratio() >= .50 and \
                    s.quick_ratio() >= .60 and \
                    s.ratio() >= .70:
                result.append((s.ratio(), w))
        result = bublesort(result)
        suggestions[word] = result
    return suggestions
