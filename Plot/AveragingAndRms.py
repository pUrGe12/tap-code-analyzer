import librosa 
import pandas as pd
import numpy as np
import math

path = r'C:\Users\hello\Downloads\test.wav' 


raw_data, screen_rate = librosa.load(path)
num1 = 32000
num2 = 380000
    
initial_list = [abs(i) for i in raw_data[num1:num2]]

#pd.Series(np.array(initial_list)).plot(figsize=(11,5),lw=0.5)

'''
we have 2 sort of distinctions to make, 1st for counting how much space we give to the tap and 
2nd for differentitating between taps in the same group with others 
'''

'''
idea: try some sort of average function to reduce number of points within some specific ranges

idea2: instead of average try a rms function
'''

width = 1000

def average_the_plot(width, new_list=[], flag_1=0, flag_2=width+1, averageSum=0, initialisation=0):

    while initialisation <= len(initial_list)/width:
        try:
            for i in range(flag_1, flag_2):
                averageSum += initial_list[i]
            new_list.append(averageSum/width * 10)
            flag_1 = flag_2
            flag_2 += width
            initialisation += 1
            averageSum = 0
        except IndexError:
            break
    
    pd.Series(np.array(new_list)).plot(figsize=(11,5),lw=0.5)
    
def rms_the_plot(width, new_list=[], flag_1=0, flag_2=width+1, averageSum=0, initialisation=0):

    while initialisation <= len(initial_list)/width:
        try:
            for i in range(flag_1, flag_2):
                averageSum += initial_list[i] ** 2
            new_list.append(math.sqrt(averageSum/width))
            flag_1 = flag_2
            flag_2 += width
            initialisation += 1
            averageSum = 0
        except IndexError:
            break

    pd.Series(np.array(new_list)).plot(figsize=(11,5),lw=0.5)

average_the_plot(width)