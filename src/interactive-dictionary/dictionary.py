from builtins import str
from difflib import get_close_matches
import json


def find_in_dict(keyword):
    
    if keyword.lower() in dict:
        return dict[keyword.lower()]
    elif keyword.title() in dict:
        return dict[keyword.title()]
    elif keyword.upper():
        return dict[keyword.upper()]
    else:
        return KeyError


def find_most_similar_word(keyword):
    similar_words = get_close_matches(keyword, keys, 3, 0.6)
    return similar_words[0] if len(similar_words) > 0 else None


def find_keyword(keyword):
    try:
        found_word = find_in_dict(keyword)
        print("\n")
        for word in found_word:
            print("* %s \n" % word)
    except KeyError:
        print("Sorry, the given word couldn't be found in the dictionary.")
        suggestion = find_most_similar_word(keyword)
        if suggestion != None:
            suggestion_response = input(suggestion_question % suggestion)
            if (suggestion_response == 'y' or suggestion_response == 'Y'):
                print(dict[suggestion])
            

with open("data.json") as dict_file:
    dict = json.load(dict_file)
    keys = dict.keys()
                
suggestion_question = "Did you meant %s instead? Enter y if Yes, n if No:  "

keyword = input("Enter the word to search:  ")

if len(keyword) == 0:
    print("The keyword cannot be empty.")
else:
    find_keyword(keyword)
