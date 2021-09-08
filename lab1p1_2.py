import numpy as np
import pandas as pd

mu = 480
sigma = 24
num = 1000
e = 2.7128

def calcSub(num):
    num = num / 1000
    ans = pow(e, -1 * num / (1.5 * 0.026)) * 10
    return ans

def calcOn(num):
    num = num / 1000
    ans = 45 * (1.2 - num) * (1.2 - num)
    return ans

def subthreshold(arr):
    ans = []
    for item in arr:
        ans.append(round(calcSub(item), 8))
    return ans

def on(arr):
    ans = []
    for item in arr:
        ans.append(round(calcOn(item), 4))
    return ans

all_data = np.zeros([num, 3], dtype='float')
rand_data = np.random.normal(mu, sigma, num)
rand_data = rand_data.round(2)

all_data[:,0] = rand_data
subthreshold_current = subthreshold(all_data[:, 0])
all_data[:,1] = subthreshold_current
on_current = on(all_data[:,0])
all_data[:,2] = on_current

last_Row = []

last_Row.append("-")

max_Subthreshold = max(all_data[:, 1])
min_Subthreshold = min(all_data[:, 1])
last_Row.append(max_Subthreshold / min_Subthreshold)

max_OnCurrent = max(all_data[:, 2])
min_OnCurrent = min(all_data[:, 2])
last_Row.append(max_OnCurrent / min_OnCurrent)
new_last_row = np.asarray(last_Row).reshape(1,3)

valid_data = pd.DataFrame(all_data, columns=["VT Value(mV)", "Subthreshold Current(uA)", "ON Current(uA)"])
valid_data.index = valid_data.index + 1
summary = pd.DataFrame(new_last_row, index=["Imax/Imin"] , columns=["VT Value(mV)", "Subthreshold Current(uA)", "ON Current(uA)"])
final_data = pd.concat([valid_data, summary], axis = 0)
final_data.index.names = ["Sample Number"]
doc = open('variation_analysis.txt ','w')
pd.set_option('display.max_rows', None)
print(final_data, file=doc)
