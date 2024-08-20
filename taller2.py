import numpy as np
mu = 3
sigma =0.5
n =2000
val = np.random.normal(loc=mu, scale=sigma, size=n)
print (val)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=val, bins=30)
plt.title("histograma")
plt.xlabel("tiempo")
plt.xlabel("frecuencia")
plt.show

print(count)
print(bins)