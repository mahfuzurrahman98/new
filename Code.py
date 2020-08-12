import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ds=pd.read_csv("datasetRegression.csv")
ds=np.array(ds)
x,t=[],[]


#Task 1
def Prepare_Dataset():
    for i in range(len(ds)):
        t.append(ds[i][7])
        tmp=[1]
        for j in range(7):
            tmp.append(ds[i][j])
        x.append(tmp)

Prepare_Dataset()
x=np.array(x)
t=np.array(t)


#Task 2
def Plot_Data():
    plt.figure()
    plt.figure(figsize=(15,20))

    for i in range(1,8):
        xx=x[:,i]
        plt.subplot(4,2,i)
        plt.scatter(xx,t)

Plot_Data()