import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


read_df = pd.read_excel('T_P_H.xlsx', header=None)

dummy = read_df[read_df.columns.tolist()[1]].replace(" ", "")
dummy = read_df[read_df.columns.tolist()[1]]
parsed_list = []
for d in list(dummy):
    try:
        t, p, h, m = d.split(',')
    except:
        continue
    row = []
    count = 0
    for i in [t, p, h, m]:
        try:
            var, trash = i.split('_')
        except:
            var = i
        try:
            trash, var = var.split(':')
        except:
            pass
        row.extend([float(var)])
        count += 1
    parsed_list.append(row)

parsed_df = pd.DataFrame(data=parsed_list)
parsed_df.columns = ['Temp','Press','RH','Minutes']
parsed_df = parsed_df[parsed_df['Minutes'] >= 500]

# fig, ax = plt.subplots()
plt.plot(np.array(parsed_df['Minutes']), np.array(parsed_df['Temp']))
plt.plot(parsed_df['Minutes'],parsed_df['RH'], 'g-')
plt.show()
plt.close()
