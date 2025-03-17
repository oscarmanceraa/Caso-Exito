import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression

data = {
    "Study Hours": [10, 15, 12, 8, 14, 5, 16, 7, 11, 13, 9, 4, 18, 3, 17, 6, 14, 2, 20, 1],
    "Final Grade": [3.8, 4.2, 3.6, 3, 4.5, 2.5, 4.8, 2.8, 3.7, 4, 3.2, 2.2, 5, 1.8, 4.9, 2.7, 4.4, 1.5, 5, 1]
}

df = pd.DataFrame(data)

x = df[["Study Hours"]] 
y = df[["Final Grade"]]

model = LinearRegression()
model.fit(x,y) 

def calculate_grade (hours):
    result = model.predict([[hours]])[0]
    if result > 5:
        result = 5;
    return result

def graph():
    plt.figure(6,4)
    
    plt.xlabel('Horas de estudio')
    plt.ylabel('nota a sacar')
    #return render_template()

