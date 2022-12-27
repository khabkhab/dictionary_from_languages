


# opens the text file

def read_file(name):
    with open(name, 'r', encoding='utf8') as file:
        text = file.read()
        return text

# split text file

def devided_text(text):
    return text.split()

# exceptions from the text
def exclude_exceptions():
    print 
    
# counts the words

dictionary = {}
def create_dic(text):
    global dictionary
    for item in devided_text(text):
        dictionary.update({item:text.count(item)})
# sort the dictionary

def sort_dic(dictionary):
    sorted_dic = sorted(dictionary.items(), key = lambda item: item[1], reverse = True)
    return sorted_dic



# identifies how many words to return

def number_of_words():
    restrictred_list = []
    for item in sort_dic(dictionary)[:length]:
        restrictred_list.append(item)
    return restrictred_list


# convert list to dictionary


# add translations with respect to language

# save as pdf file

#
name_of_file = input("Please write the name of the file: ")
length = int(input("How many words do you want to extract from the text?: "))
create_dic(read_file(name_of_file))
print(number_of_words())