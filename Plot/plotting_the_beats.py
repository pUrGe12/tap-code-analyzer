import librosa 
import librosa.display
import pandas as pd
import numpy as np

path = ''

def plot(path):
    '''
    use num1 and num2 to scale the plot
    '''
    
    raw_data, screen_rate = librosa.load(path)
    
    num1 = 1
    num2 = 300000
    
    new = [abs(i) for i in raw_data[num1:num2]]
    pd.Series(np.array(new)).plot(figsize=(11,5),lw=0.5)
    
plot(path)