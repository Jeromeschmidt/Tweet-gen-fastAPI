
from core.sentence_generator.markov_chain import MarkovChain

def build_markov_chain():
    with open("app/core/sentence_generator/sherlock.txt",'r') as file:
        text = file.read()
        text = text.split()

    markovChain = MarkovChain(text)

    return markovChain
