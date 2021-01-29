import string
import random
import numpy as np

for r in range(3):
    # if r == 0:
    #     continue

    for size in [100, 1000, 10000, 100000, 1000000, 10000000]:
        if r == 0:
            stream_list = [''.join(random.choice(string.ascii_lowercase)) for _ in range(size)]
        else:
            d = np.random.normal(13, 4.5, size).astype(np.int)
            # stream_list = [string.ascii_lowercase[i] for i in d]
            stream_list = [string.ascii_lowercase[i] if i >= 0 and i < len(string.ascii_lowercase) else
                           random.choice(
                string.ascii_lowercase) for i in d]

        with open(str(size) + "-" + ("Uniform" if r == 0 else "Normal") + " Distribution" + ".txt", "w") as file01:
            for s in stream_list:
                file01.write(s)
