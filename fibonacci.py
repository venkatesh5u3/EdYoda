# -*- coding: utf-8 -*-
""".ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18wE00YuxYZ5ob8B3PBVTxk3cfaaUueea
"""

n1, n2 = 0, 1
count = 0
while n1 < 50:
	print(n1)
	nth = n1 + n2
	n1 = n2
	n2 = nth
	count += 1