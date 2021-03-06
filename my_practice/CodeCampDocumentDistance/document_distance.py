'''
    Document Distance - A detailed description is given in the PDF
'''
import math
def build_dict(dict1):
    '''
    buid a dictionary from a list
    '''
    dictionary = {}
    dict1 = ''.join(e for e in dict1 if e.isalpha() or e == ' ')
    list_words = dict1.lower().split(" ")
    stop_words = load_stopwords("stopwords.txt")
    for word in list_words:
        length = len(word)
        if word not in stop_words and length > 0:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return dictionary

def built_common_dict(dict1, dict2):
    '''
    Buid a common dictionary from two dictionaries
    '''
    common_dict = {}
    for key in dict1:
        if key in dict2:
            common_dict[key] = [dict1[key], dict2[key]]
    return common_dict

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    numerator = 0
    denominator1 = 0
    denominator2 = 0

    dictionary1 = build_dict(dict1)
    dictionary2 = build_dict(dict2)
    common_dict = built_common_dict(dictionary1, dictionary2)
    for key in dictionary1:
        if key not in common_dict:
            common_dict[key] = [dictionary1[key], 0]
    for key in dictionary2:
        if key not in common_dict:
            common_dict[key] = [0, dictionary2[key]]
    for value in common_dict.values():
        numerator += value[0] * value[1]
        denominator1 += value[0] ** 2
        denominator2 += value[1] ** 2
    denominator = (math.sqrt(denominator1) * math.sqrt(denominator2))
    if denominator == 0:
        return 0.0
    return numerator / denominator



def load_stopwords(name_file):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(name_file, 'r') as name_file:
        for line in name_file:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
