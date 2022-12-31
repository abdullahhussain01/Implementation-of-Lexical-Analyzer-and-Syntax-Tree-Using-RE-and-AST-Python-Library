# -*- coding: utf-8 -*-
"""2009010.42_Assign_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MeAC6WBivSdCKjpx7fBUB0rVxmyedZJY
"""

import re

def tokenize(expression):
  # Build a regular expression to match all the tokens in the expression
  token_regex = re.compile(r'\d+|[a-zA-Z]+|[+-/*()]')

  # Use the regular expression to find all the tokens in the expression
  tokens = token_regex.findall(expression)

  # Return the list of tokens
  return tokens

expression = "a+(b*c)"
tokens = tokenize(expression)
print(tokens)
# Output: ['a', '+', '(', 'b', '*', 'c', ')']

import re

def tokenize(expression):
  # Build a regular expression to match all the tokens in the expression
  token_regex = re.compile(r'\d+|[a-zA-Z]+|[+-/*()]')

  # Use the regular expression to find all the tokens in the expression
  tokens = token_regex.findall(expression)

  # Return the list of tokens
  return tokens

expression = "3+(5*2)"
tokens = tokenize(expression)
print(tokens)
# Output: ['3', '+', '(', '5', '*', '2', ')']