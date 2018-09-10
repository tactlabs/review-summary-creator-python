#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Feb 27, 2018

Course work: 

@author: raja

Source:
    https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
    https://stackoverflow.com/questions/40325980/how-is-the-vader-compound-polarity-score-calculated-in-python-nltk
    https://stackoverflow.com/questions/tagged/vader
    https://github.com/cjhutto/vaderSentiment
    https://pypi.python.org/pypi/vaderSentiment/0.5
    https://web.stanford.edu/~jurafsky/pubs/neutrality.pdf
    https://stackoverflow.com/questions/370357/python-variable-scope-error
    https://stackoverflow.com/questions/26045779/python-how-to-turn-all-numbers-in-a-list-into-their-negative-counterparts
    http://www.nltk.org/_modules/nltk/sentiment/vader.html
    
    https://github.com/cjhutto/vaderSentiment
    
Cite:
    Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
    Sentiment Analysis of Social Media Text. Eighth International Conference on
    Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
'''

# Import necessary modules
import json
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

EMOTION_METER_PAR = 5
WORD_LENGTH_PAR = 4
LINES_PAR = 5

def get_lines_in_array(filename):    
    with open(filename) as f:
        content = f.readlines()
        
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    
    #print(content)  
    return content

def is_invalid_content(content):
    
    # if only 3 words, ignore it
    if(len(content.split()) < WORD_LENGTH_PAR):
        return True
    
    return False

def sort_dict_reverse(d):
    s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
    
    return s

sid = SentimentIntensityAnalyzer()

def get_negative_meter(sentence):
        
    #print(sentence)

    ss = sid.polarity_scores(sentence)
    
    #print(type(ss['pos']))

    #positive_meter = round((ss['pos'] * 10), 2) 
    negative_meter = round((ss['neg'] * 10), 2)
    
    '''
    for k in sorted(ss):
        #print(ss)
        print('{0}: {1}, '.format(k, ss[k]), end = '')
    '''
    
    #print('positive : {0}, negative : {1}'.format(positive_meter, negative_meter))
    
    #print()
    
    return negative_meter

    
def main():    
    #print(data)
    
    contents = get_lines_in_array('cons.txt')
    
    #print(contents)
    
    neg_meter_dict = {}
    
    lines_counter= 0
    
    total_contents = len(contents)
    for x in range(total_contents):
        
        if(is_invalid_content(contents[x])):
            continue
        
        emotion_meter = get_negative_meter(contents[x])
        
        # if meter is less than 5, ignore them
        if(emotion_meter > EMOTION_METER_PAR):
            continue
        
        neg_meter_dict[contents[x]] = emotion_meter
        
        #print('---')
        #print(contents[x])        
        
    sorted = sort_dict_reverse(neg_meter_dict)    
    #print(neg_meter_dict)
    
    for k, v in sorted:
        lines_counter = lines_counter + 1
        
        if(lines_counter > LINES_PAR):
            continue                

        print(k, v)
    
if __name__ == '__main__':
    main()