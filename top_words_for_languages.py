from googletrans import Translator
import googletrans
import pandas as pd
import string
from pathlib import Path 


# opens the text file

def read_file(name):
    with open(name, 'r', encoding='utf8') as file:
        for line in file:
            line = exclude_characters(line)
            words = line.split(" ")
            for word in words:
                word = word.capitalize()
                if word not in dictionary and word != "\n": 
                    dictionary[word] = 0
                elif word != "\n":
                    dictionary[word] += 1


# exceptions from the text
def exclude_characters(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line

# converts language value to language key, i.e., english to en, spanish to es, etc
def language_keys(lang):
    for key, val in googletrans.LANGUAGES.items():
        if val == lang.lower():
            return key
# identifies how many words to return

def number_of_words():
    restrictred_list = []
    for item in dictionary:
        restrictred_list.append(item) 
    return restrictred_list[:length]


# add translations with respect to language
def translate_the_top(w, language):
    translate = Translator()
    translated_word = translate.translate(w, dest=language_keys(language))
    return translated_word


# create dataframe from two lists: top_lenght and translated version
def create_the_dataframe():
    df = pd.DataFrame(list(zip(number_of_words(), [translate_the_top(the_word, language).text for the_word in number_of_words()])), columns=['Original Top', 'Translated Top'])
    # res = {number_of_words()[0]: [translate_the_top(the_word, language).text for the_word in number_of_words()][i] for i in range(len(number_of_words()))}
    return df

# save df as csv file without first column (numbered rows) !!!!not finished

def data_to_csv(df):
    filepath = Path(f'Top {length} words with translation to {language}.csv')
    df.to_csv(filepath)
# detect language function
dictionary = {}
name_of_file = input("Please write the name of the file: ")
length = int(input("How many words do you want to extract from the text?: "))
language = input("Which language do you want to translate the top words to?: ").lower()
read_file(name_of_file)
# print(create_the_dataframe()[:15])
data_to_csv(create_the_dataframe())
