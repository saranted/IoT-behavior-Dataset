# Import Dependencies
import numpy as np
import pandas as pd

# Load Dataset
df1 = pd.read_csv('benign_traffic_qbot1.csv')
df2 = pd.read_csv('MALIGN_traffic_qbot.csv')
df = pd.read_csv('traffic_qbot1.csv')
y=df.columns.size
y=y-1
list1=[]
for i in range(0, y):
    feature=df.columns[i]
    mu = (np.sum(df[df.columns[i]], axis=0))/ df.shape[0]
    #label benign
    x = np.sum(df1, axis=0) 
    X = np.sum(x, axis=0)
    n_1 = X;
    # Calculate the mean of each feature = $\mu_{i}$
    mu_1 = (np.sum(df1[df.columns[i]], axis=0))/ df1.shape[0]
    var_1 = np.var(df1[df.columns[i]])
    #label malware
    x = np.sum(df2, axis=0) 
    X = np.sum(x, axis=0)
    n_2 = X;
    mu_2 = (np.sum(df2[df.columns[i]], axis=0))/ df2.shape[0]
    var_2 = np.var(df2[df.columns[i]])
    inter_class = pow(mu_1-mu,2)*n_1 + pow(mu_2-mu,2)*n_2
    intra_class = (n_1-1)*var_1 + (n_2-1)*var_2
    score = inter_class / intra_class
    print (df.columns[i], score) 
    list1.append((df.columns[i], score))


Fisher_score = pd.DataFrame(list1, columns = ['Feature', 'Fisher Score']) 
dff=Fisher_score.sort_values(by='Fisher Score', ascending=False)   

dff.to_csv('fisher_score.csv')