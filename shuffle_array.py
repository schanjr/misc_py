#function for shuffling data. 

'''
df - expecting a pandas.Dataframe() object or numpy array
n  - number of shuffling. The higher number, the more amount of times the data will be scrambled
axis - applies only when there are multiple axis.
'''

def shuffle(df, n=1, axis=0):
  import numpy as np
  df = df.copy()
  for _ in range(n):
      df.apply(np.random.shuffle, axis=axis)
  return df    
