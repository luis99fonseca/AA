import numpy as np
import matplotlib.pyplot as plt
import string

d = np.random.normal(14, 2, 10000000).astype(np.int)
# plt.hist(d)
print(len(d))
print(d[:11])
print(d.shape)
print(np.unique(d))
print(len(np.unique(d)))
print("--")
print(len(string.ascii_lowercase))

# stream_list = [i for i in d]
# plt.hist(stream_list)
#
# plt.show()