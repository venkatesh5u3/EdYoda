# -*- coding: utf-8 -*-
""".ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18wE00YuxYZ5ob8B3PBVTxk3cfaaUueea
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))
print('Number of even numbers : ',even_count)
print('Number of odd numbers : ',odd_count)

