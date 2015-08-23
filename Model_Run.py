# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:54:19 2015

@author: arkag
"""
from sklearn.externals import joblib
from Main import data_clean
from Main import tokenize
import nltk

def bigram(token_data):
    bigram = joblib.load("Bigram.pkl")
    model = bigram[token_data[0]]
    try:
        token_data.append(model.max())
    except:
        print "Sorry no match found"
        return None
    return model.max()

def trigram(token_data):
    tri_list=[]
    most_common =""
    trigrams = joblib.load("Trigram.pkl")
    second_last = token_data[0]
    last = token_data[1]
    for gram in trigrams:
        if str(gram[0]) == str(second_last) and str(gram[1]) == str(last):
            tri_list.append(gram[2])
    try:
        fdist1 = nltk.FreqDist(tri_list) 
        most_common = fdist1.max()    
    except:
        print "Sorry no match found"
    return most_common

def fourgram(token_data1):
    four_list=[]
    most_common1=""
    fourgrams = joblib.load("Fourgram.pkl")
    third_last =  token_data1[0]
    second_last = token_data1[1]
    last = token_data1[2]
    for grams in fourgrams:
        if str(grams[0]) == str(third_last) and str(grams[1]) == str(second_last) and str(grams[2]) == str(last):
            four_list.append(grams[3])
    try:
        fdist2 = nltk.FreqDist(four_list) 
        most_common1 = fdist2.max()
    except:
        print "Sorry second word not found"
    return most_common1
    
    
def fivegram(token_data2):
    five_list=[]
    most_common2=""
    fivegrams = joblib.load("Fivegram.pkl")
    fourth_last = token_data2[0]
    third_last =  token_data2[1]
    second_last = token_data2[2]
    last = token_data2[3]
    for grams in fivegrams:
        if str(grams[0]) == str(fourth_last) and str(grams[1]) == str(third_last) and str(grams[2]) == str(second_last) and str(grams[3]) == str(last):
            five_list.append(grams[4])
    try:
        fdist3 = nltk.FreqDist(five_list) 
        most_common2 = fdist3.max()
    except:
        print "Sorry second word not found"
    return most_common2
    
    
def sixgram(token_data3):
    six_list=[]
    most_common3=""
    sixgrams = joblib.load("Sixgram.pkl")
    fifth_last = token_data3[0]
    fourth_last = token_data3[1]
    third_last = token_data3[2]
    second_last = token_data3[3]
    last = token_data3[4]
    for grams in sixgrams:
        if str(grams[0]) == str(fifth_last) and str(grams[1]) == str(fourth_last) and str(grams[2]) == str(third_last) and str(grams[3]) == str(second_last) and str(grams[4]) == str(last):
            six_list.append(grams[5])
    try:
        fdist3 = nltk.FreqDist(six_list) 
        most_common3 = fdist3.max()
    except:
        print "Sorry second word not found"
    return most_common3
def match_complete(tokenized):
    matched = ""
    dataset = joblib.load("Dataset.pkl")
    for vals in dataset[0]:
        if vals == tokenized:
            output = tokenized
            print output
            matched = "Yes"
    return matched

def run_main():
    val = "Test"
    enter_input = str(raw_input(("Please enter the text: ")))
    clean_data = data_clean(enter_input,val)
    tokenized_data = tokenize(clean_data,val)
    flag ="N"
    match = match_complete(tokenized_data)
    if match == "Yes":
        flag = "Y"
    if flag =="N":
        if len(tokenized_data) == 1:
            newval = bigram(tokenized_data)
            tokenized_data.append(newval)
            match = match_complete(tokenized_data)
            if match == "Yes":
                print str(newval)
                print "That is the end of sentence"
                exit
            output = trigram(tokenized_data)
            print "The new predicted two words are : "+str(newval)+" "+str(output)
        elif len(tokenized_data) == 2:
            print tokenized_data
            newval1 = trigram(tokenized_data)
            tokenized_data.append(newval1)
            match = match_complete(tokenized_data)
            if match == "Yes":
                print str(newval1)
                print "That is the end of sentence"
                exit
            output1 = fourgram(tokenized_data)
            print "The new predicted two words are : "+str(newval1)+" "+str(output1)
        elif len(tokenized_data) == 3:
            print tokenized_data
            newval = fourgram(tokenized_data)
            tokenized_data.append(newval)
            match = match_complete(tokenized_data)
            if match == "Yes":
                print str(newval)
                print "That is the end of sentence"
                exit
            output = fivegram(tokenized_data)
            print "The new predicted two words are : "+str(newval)+" "+str(output)
        elif len(tokenized_data) == 4:
            print tokenized_data
            newval = fivegram(tokenized_data)
            tokenized_data.append(newval)
            match = match_complete(tokenized_data)
            if match == "Yes":
                print str(newval)
                print "That is the end of sentence"
                exit
            output = sixgram(tokenized_data)
            print "The new predicted two words are : "+str(newval)+" "+str(output)
        elif len(tokenized_data) > 4:
            tokenized_data = tokenized_data[-4:] 
            newval = fivegram(tokenized_data)
            match = match_complete(tokenized_data)
            if match == "Yes":
                print str(newval)
                print "That is the end of sentence"
                exit
            tokenized_data.append(newval)
            output = sixgram(tokenized_data)
            print "The new predicted two words are : "+str(newval)+" "+str(output)
        else:
            print "Please eneter text"
        

if __name__ == "__main__":
    run_main()           

