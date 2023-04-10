from read_dictionary import dictionary
from get_misspelled import get_misspelled
from get_suggestions import get_suggestions
from print_result import print_result
from remove_punctuation import remove_punctuation
from under_line import under_line
from add_to_dictionary import add_to_dictionary

print('********* Welcome to spell checker program *********\n')

my_dictionary = dictionary()  # list of dictionary words

word=input('add your word to dict  ')
text = input('Type your text to be checked: ')
N=input('Please enter the number of suggestions  ')
my_dictionary = add_to_dictionary(my_dictionary,word)
#first requirement
b=int(N)
text = text.lower().split()  # list of text words
text = remove_punctuation(text)
misspelled_words = get_misspelled(text, my_dictionary)
under_line(text, misspelled_words)
suggestions = get_suggestions(misspelled_words, my_dictionary,b)
print_result(suggestions, misspelled_words)
