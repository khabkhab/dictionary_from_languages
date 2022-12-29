from googletrans import Translator
import pandas as pd
import string
import fpdf


# opens the text file

def read_file(name):
    with open(name, 'r', encoding='utf8') as file:
        for line in file:
            line = exclude_characters(line)
            words = line.split(" ")
            for word in words:
                word = word.lower()
                if word not in dictionary:
                    dictionary[word] = 0
                dictionary[word] += 1


# exceptions from the text
def exclude_characters(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line

# sort the dictionary

# identifies how many words to return

def number_of_words():
    restrictred_list = []
    for item in dictionary:
        restrictred_list.append(item) 
    return restrictred_list[:length]


# add translations with respect to language
def translate_the_top(w, language):
    translate = Translator()
    translated_word = translate.translate(w, dest=language)
    return translated_word


# create dataframe from two lists: top_lenght and translated version
def create_the_dataframe():
    df = pd.DataFrame(list(zip(number_of_words(), [translate_the_top(the_word, language).text for the_word in number_of_words()])), columns=['Original Top', 'Translated Top'])
    return df

# save df as pdf file without first column (numbered rows) !!!!not finished
def create_pdf(dataframe):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    pdf.cell()
    pdf.output(f"List of top {length} words in the {name_of_file} with tranlsation to {language}", "F")
    
#
dictionary = {}
name_of_file = input("Please write the name of the file: ")
length = int(input("How many words do you want to extract from the text?: "))
language = input("Which language do you want to translate the top words to?: ").lower()

read_file(name_of_file)
create_pdf(create_the_dataframe())