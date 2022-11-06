import math
import time
import random
from tqdm import tqdm, trange
from joblib import Parallel, delayed

results = []
results2 = []
results3 = []

for i in tqdm(range(5000), colour='cyan'):
    results.append(math.factorial(i))

results2 = [math.factorial(x) for x in tqdm(range(5000), colour='green')]

results3 = Parallel(n_jobs=-1)(delayed(math.factorial)(x) for x in tqdm(range(8000), colour='blue'))

with trange(50) as t:
    for i in t:
        t.set_description(f"Iteration Number {i + 1}")
        t.colour = 'green'
        sleeping_time = random.randint(1, 100) / 100
        t.set_postfix(something=random.randint(0, 100), sleeping_time=sleeping_time)
        time.sleep(sleeping_time)
        if i % 100 == 0:
            for _ in trange(10):
                time.sleep(0.5)






