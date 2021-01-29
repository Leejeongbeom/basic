import numpy as np

weights = np.array([86,74,59,95,80,68])

print(weights)
print(weights.reshape(3,2))
weights = np.ones(6)
print(weights)

heights = np.zeros(6)

print(heights.shape)
print(heights)
print(heights.mean())