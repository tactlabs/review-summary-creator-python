#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Aug 26, 2017

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
from nltk.sentiment.vader import SentimentIntensityAnalyzer




reviews = [
        {
            "company_name" : "Credit Mantri",
            "title" : "Looks bad from the outside but it's worst inside",
            "info" : "I worked at CreditMantri full-time (More than a year)",
            "pros" : "I gave it a thought but couldn't think of anything positive about the company except for the co-workers, the colleagues were great.",
            "cons" : "They think that we don't have any life outside of the company. No work life balance. Insane deadlines. Clumsy management.",
            "advice" : "Sell the company ASAP",
        },
        {
            "company_name" : "",
            "title" : "An overrated startup",
            "info" : "",
            "pros" : "Flexible timings, Healthy snacks provided",
            "cons" : "Over the last few months, you can see a lot of 5 star reviews from current employees. To get more candidates, it looks like a deliberate attempt to improve their glassdoor rating. This company has not done much during their first five years. So, they are desperately trying to make up for lost time. As a result, there is unnecessary pressure on everyone (especially on the sales team to deliver). Founders are never happy. They don't appreciate anyone and at times, they give impossible deadlines. Developers generally don't deliver anything on time. Company loses a lot of prospects because of poor delivery. If you are a developer, you can consider joining this company as you can learn a lot from tech-savy founders. But for other roles, think again before joining. Especially if you want to join the sales/pre-sales teams.",
            "advice" : "",
        },
        {
            "company_name" : "",
            "title" : "Embedded intern",
            "info" : "I worked at Energyly as an intern",
            "pros" : "Highly interactive. Its not a team, its a family. Excellent support is given by them. Learned a lot. Friendly environment.",
            "cons" : "No cons. Everything is fine.",
            "advice" : "",
        },
        {
            "company_name" : "",
            "title" : "Data Analyst",
            "info" : "I have been working at Energyly as an intern",
            "pros" : "very Good support for work.",
            "cons" : "Not much interaction with the fellows.",
            "advice" : "",
        },
        {
            "company_name" : "",
            "title" : "Great team and working culture. Friendly CEO.",
            "info" : "I have been working at Energyly full-time (More than a year)",
            "pros" : "Very good opportunity for freshers. Where they can both learn and earn from other professionals. As they hire internships from IIT, IIM, VIT",
            "cons" : "Office environment is small. But good infra structure. As you have to work individually, we lack of being a team player in MNCs.",
            "advice" : "Keep this same treatment towards employees",
        }
    ]


#print(reviews[0]["name"])

def analyze_local(sentence):
    sid = SentimentIntensityAnalyzer()
    
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
    print()
    print()

for rv in reviews:    
    #print(rv['company_name'])
    #print(rv['pros'])
    #analyze_local(rv['title'])
    analyze_local(rv['pros'])
    analyze_local(rv['cons'])
    
    
    
    