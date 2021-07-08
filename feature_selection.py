import pandas as pd
import numpy as np
import math
from matplotlib import pyplot
from scipy.stats import mannwhitneyu
import statsmodels.api as sm

def civalue(x):
    mx=np.mean(x)
    ci=np.zeros((2))
    ci[0]=mx-1.96*x.std()/math.sqrt(len(x))
    ci[1]=mx+1.96*x.std()/math.sqrt(len(x))
    return ci
  
  civ=np.zeros((20,4))
p=np.zeros((20))
fname='E:/matlab/data1/arc.csv'
df=np.genfromtxt(fname,delimiter=',')
df=df[1:,4:]
bugs=df[:,-1]
in0=np.where(bugs==0)
in1=np.where(bugs==1)
for i in range(0,df.shape[1]):
    fv=df[:,i]
    print(in0)
    civ[i,0:2]=civalue(fv[in0])
    civ[i,2:4]=civalue(fv[in1])
    x=np.zeros((2,2))
    w,p[i]=mannwhitneyu(fv[in0],fv[in1])
    x[0:2,0]=civ[i,0:2]
    x[0:2,1]=civ[i,2:4]
    pyplot.boxplot(x,labels=['Not-faulty','Faulty'])
    pyplot.grid(True)
    pyplot.xlabel('Metrics')
    pyplot.ylabel('95%CI')
    fna='C:/Users/lov/Documents/dsv/'+str(i)+".png"
    pyplot.savefig(fna)
    pyplot.close()
print("significant metrics=",np.where(p<=0.05))
suncf=[]
sigf=np.where(p<=0.05)
bugs[np.where(bugs>0)]=1
sigf=np.array(sigf)
suncf.append(sigf)
p1=np.zeros((sigf.shape[1]))
print(sigf)
