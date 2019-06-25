# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:55:38 2019

@author: J554696
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from nltk import word_tokenize
import re
from langdetect import detect
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



def generalize_ratings(df):
    reviews_rating = [1.0 , 2.0 , 3.0 , 4.0 , 5.0]
    temp = []
    for i , row in df.iterrows():
        
        rating = row['reviews.rating']
        
        if rating not in reviews_rating:
            temp.append('T')
        else:
            temp.append('F')
            
    df['Flag'] = temp  
    df.drop(df[df['Flag'] == 'T'].index, axis = 0, inplace = True)
    df.drop('Flag' , axis = 1, inplace = True)
    
    return df

def sentiment(rating):
     
    if rating >=4:
        sent = 'positive'
    else:
        sent = 'negative'
        
    return sent

def import_pos_neg_corpus():
    lexicon_path = "C:\\Users\\J554696\\Desktop\\Sentiment Analysis\\Rahul_Data_exploration\\"
    negative_file = os.path.join(lexicon_path,"neg_words.txt")
    positive_file = os.path.join(lexicon_path,"pos_words.txt")
    
    negative_corpus = [word.strip('\n') for word in open(negative_file).readlines()]
    positive_corpus = [word.strip('\n') for word in open(positive_file).readlines()]
    
    return negative_corpus , positive_corpus

def tokenize(text):
    temp= []
    lemmatizer = WordNetLemmatizer()  
    word_list = word_tokenize(text)
    for word in word_list:
        temp.append(lemmatizer.lemmatize(word))
    return temp

def find_count(token):
    token =  [word.lower() for word in token ]
    negative_corpus , positive_corpus = import_pos_neg_corpus()
    negative_words_count = len(list(set(token) & set(negative_corpus)))
    positive_words_count = len(list(set(token) & set(positive_corpus)))
    
    positive_words = list(set(token) & set(positive_corpus))
    negative_words = list(set(token) & set(negative_corpus))
    
    return negative_words_count,positive_words_count, positive_words , negative_words

def length_range(length):
    
    if length <= 50:
        return 50
    elif (length > 50  and length <= 100) :
        return 100
    elif (length > 100  and length <= 150) :
        return 150
    elif (length > 150  and length <= 200) :
        return 200
    elif (length > 200  and length <= 250) :
        return 250
    else:
        return 300

def check_Upper_Words(tokens):
    upper_words = [word for word in tokens if word.isupper()]
    upper_words = [word for word in upper_words if word.lower() not in stopwords.words('english')]
    return upper_words

def check_questions(string):
    result = re.findall(r'\?+',string)
    return result

def check_exclamations(string):
    result = re.findall(r'\!+',string)
    return result

def check_fullstop(string):
    result = re.findall(r'\.+',string)
    return result 

def main_handler():
    df  = pd.read_csv(r'C:\Users\J554696\Desktop\Sentiment Analysis\Clean_test.csv')
    df.dropna(inplace = True)
    df.drop(index = df[df["length"] == "#NAME?"].index,inplace = True)
    df["length"] = df["length"].astype("int")
    df = generalize_ratings(df)
    df['Sentiment'] = df['reviews.rating'].apply(sentiment)
    
    print(df.info())
    print(df.head())
    
    lang = []
    for i in df['reviews.text']:
        try:
            lang.append(detect(i))
        except:
            lang.append('No Lang')
            
          
    df['Language'] = lang
    df.drop(df[df['Language'] != 'en'].index , axis = 0 , inplace = True)
    df['Count_QuestionMarks'] = df['reviews.text'].apply(check_questions)
    df['Full_Stops'] = df['reviews.text'].apply(check_fullstop)    
    df['length_range'] = df['length'].apply(length_range)
    df['tokenize'] = df['reviews.text'].apply(tokenize)
        
    df['Negative-Positive-Count'] = df['tokenize'].apply(find_count)
    df['Exclamation'] = df['reviews.text'].apply(check_exclamations)
    df['Upper_case'] = df['tokenize'].apply(check_Upper_Words)
    
    neg_count = []
    pos_count = []
    positive = []
    negative = []
    for i , j , k , l in df['Negative-Positive-Count']:
        try:
            neg_count.append(i)
            pos_count.append(j)
            positive.append(k)
            negative.append(l)
        except:
            neg_count.append(0)
            pos_count.append(0)
            positive.append(0)
            negative.append(0)
            
    df['Negative-count'] = neg_count
    df['positive-count'] = pos_count
    df['Positive_words'] = positive
    df['Negative_words'] = negative
    df.drop('Negative-Positive-Count', axis = 1 , inplace = True)
    
    
    ## Checking if positive or negative words are in Upper case
    ## Lemmatization of tokens
    
    negative_corpus , positive_corpus = import_pos_neg_corpus()
    pos_uc_words = []
    neg_uc_words = []
    for index , row in df.iterrows():
        list1 = row['Upper_case']
        pos_count = 0
        neg_count = 0
        
        for  i in list1:
    
            if i.lower() in set(positive_corpus):
                pos_count+=1
            elif i.lower() in set(negative_corpus):
                neg_count+=1
    
        pos_uc_words.append(pos_count)        
        neg_uc_words.append(neg_count)
        
        
    df['Positive_Upper_case_words'] = pos_uc_words
    df['Negative_Upper_case_words'] = neg_uc_words
    print(df.head())
    
if __name__== "__main__":
     main_handler()
    
