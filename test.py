import pandas as pd
import tensorflow as tf
import numpy as np
i_list = []
for i in range(0, 10):
    i_list.append(i)

i_list = pd.DataFrame(i_list)

i_list.to_csv('i_list.csv')
