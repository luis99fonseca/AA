import numpy as np
import matplotlib.pyplot as plt
import string
import random

d = np.random.normal(14, 3.5, 1000000).astype(np.int)
# plt.hist(d)
print(len(d))
print(d[:11])
print(d.shape)
print(np.unique(d))
print(len(np.unique(d)))
print("--")
print(len(string.ascii_lowercase))

a = [string.ascii_lowercase[i] if i >= 0 and i < len(string.ascii_lowercase) else random.choice(string.ascii_lowercase) for i in d]
print(len(np.unique(a)))
# stream_list = [i for i in d]
# plt.hist(stream_list)
#
# plt.show()