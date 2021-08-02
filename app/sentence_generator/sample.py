import sys
import random
import re

# random.seed(42)

def find_weights(text):
    weights = {}
    size = len(text)
    for word in text:
        if word.lower() not in weights:
            weights[word.lower()] = 1
        else:
            weights[word.lower()] += 1
    for word in weights:
        weights[word.lower()] = weights[word.lower()]/size
    return weights

def find_weights_dict(dict):
    weights = {}
    size = 0
    for elm in dict:
        size += dict[elm]
    for elm in dict:
        weights[elm] = dict[elm]
    for word in weights:
        # try:
        weights[word.lower()] = weights[word.lower()]/size
        # except KeyError:
        #     weights[word.lower()] = 1
    return weights

def find_weights_by_length(dict):
    total_length = 0
    weights = {}

    for elm in dict:
        total_length += len(elm)
    for elm in dict:
        weights[elm] = len(elm)/total_length
        print(weights[elm])

def find_weights_list(text):
    weights = list()
    size = len(text)
    for word in text:
        count = 0
        for word2 in text:
            if(word == word2):
                count += 1
        if((word, count/size) not in weights):
            weights.append((word, count/size))
    return weights

def run_list(weights, number_of_iter):
    results = list()
    for elm in weights:
        results.append((elm[0], elm[1], 0))
    for i in range(int(number_of_iter/len(weights))):
        for elm2 in results:
            if(random.random() < elm2[1]):
                word = elm2[0]
                prob = elm2[1]
                num = elm2[2]
                results.remove(elm2)
                results.append((word, prob, num+1))
    return results

def run(weights, number_of_iter):
    keys_list = list(weights.keys())
    weights_list = list(weights.values())
    results = {}
    for i in range(number_of_iter):
        for key in keys_list:
            if(random.random() < weights[key]):
                if key in results:
                    results[key] += 1
                else:
                    results[key] = 1
    return results

def find_ranges(weights):
    range_temp = 0
    ranges = {}
    for elm in weights.keys():
        ranges[elm] = (range_temp, range_temp+weights[elm])
        range_temp += weights[elm]
    return ranges

def sample_by_frequency(ranges, number_of_iter):
    results = {}
    for i in range(number_of_iter):
        random_num = random.random()
        for elm in ranges:
            if((random_num >= ranges[elm][0]) and (random_num < ranges[elm][1])):
                if elm in results:
                    results[elm] += 1
                else:
                    results[elm] = 1
    return results

def get_sentence(num_of_words):
    with open("sherlock.txt",'r') as file:
        text = file.read()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = text.split()
    ranges = find_ranges(find_weights(text))
    sentence = ""
    for i in range(num_of_words):
        random_num = random.random()
        for elm in ranges:
            if((random_num >= ranges[elm][0]) and (random_num < ranges[elm][1])):
                sentence += elm + " "
    return sentence

if __name__ == '__main__':

    with open(sys.argv[1],'r') as file:
        text = file.read()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = text.split()
    dict = find_weights_by_length(text)
