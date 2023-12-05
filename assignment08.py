# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import pandas
import matplotlib
import psycopg2


thistuple = ("apple", "banana", "cherry")
print(thistuple[1]);

df = pandas.read_csv(r"E:\NDSU\Database\Assignments\Parisa-assignment/train.csv");
print(df.head(10))



df['LoanAmount'].hist(bins=50)


#connect to an existing DB
conn = psycopg2.connect(
    host="",
    database="Assignment8",
    user="postgres",
    password="Parisa4653")

cur = conn.cursor()

#with open(r"E:\NDSU\Database\Assignments\Parisa-assignment/train.csv") as f:
  #  next(f)
   # cur.copy_from(f, 'loan01', sep=',')

    #conn.commit()
    
    