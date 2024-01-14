import librosa 
import pandas as pd
import numpy as np
import math

path = r'C:\...\test.wav' # path to wav file

raw_data, screen_rate = librosa.load(path)
num1 = '' # start point
num2 = '' # end point
    
initial_list = [abs(i) for i in raw_data[num1:num2]]

'''
idea1: average function to reduce number of points within some specific ranges
idea2: RMS function to reduce number of points
'''

width = 1000

def average_the_plot(width, new_list=[], flag_1=0, flag_2=width+1, averageSum=0, initialisation=0):
    assert type(width) == int, 'enter valid width'  
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
    
    pd.Series(np.array(new_list)).plot(figsize=(11,5),lw=0.5) # comment this if you don't want to plot and check
    
def rms_the_plot(width, new_list=[], flag_1=0, flag_2=width+1, averageSum=0, initialisation=0):
    assert type(width) == int, 'enter valid width'
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

    pd.Series(np.array(new_list)).plot(figsize=(11,5),lw=0.5) # comment this if you don't want to plot and check
