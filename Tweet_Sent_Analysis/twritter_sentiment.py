#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time


# In[2]:


import sentiment_mod as s


# In[3]:


count = 0
with open('part-00000-a2063ab0-7b44-489f-a5d5-1f3ef8cc9dd5-c000.csv', encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if count <=500:
                count = count +1 
               # print(count)
                row1=str(row)
      #  row = [entry.decode("utf8") for entry in row]
                sentiment_value, confidence = s.sentiment(row1)
                print(sentiment_value)
        


# In[4]:


if confidence*100 >= 80:
    output = open("twitter-out.txt","a")
    output.write(sentiment_value)
    output.write('\n')
    output.close()


# In[5]:


style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[0:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()


# In[ ]:




