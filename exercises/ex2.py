import numpy.random
import numpy

N = [5, 10, 100, 10000, 1000000]
S = 200

means_deviations = []

for n in N:
    means = []
    for s in range(S):
        x = numpy.random.normal(4, 1, n)
        x_mean = numpy.mean(x)
        means.append(x_mean)
    means_std = numpy.std(means)
    means_deviations.append(means_std)

print(N)
print(means_deviations)
