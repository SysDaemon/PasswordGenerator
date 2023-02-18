#!/usr/bin/python
# -*- coding: latin-1 -*-

import random
import requests

while True:
    lower_character = "abcdefghijklmnopqrstuvwxyz"
    upper_character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%&*()_+=´^~{[}]:;.>,<"
    numbers = "0123456789"
    
    string = lower_character + upper_character + symbols + numbers

    # Get the random seed for choices in string
    response = requests.get('https://www.random.org/integers/?num=1&min=1&max=1000&col=1&base=10&format=plain&rnd=new') 
    random.seed(a =response.text, version=2)
    try:
        # comment: Trying to get inputted values
            password_length = int(input("What length would you like your password to be: "))
            password_count =  int(input("How many password would you like: "))
    except EOFError as e:
        raise e
    # end try
    
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_length):
            password_char   = random.choice(string)
            password        = password + password_char
        print(password)
    # end try
#end of While
