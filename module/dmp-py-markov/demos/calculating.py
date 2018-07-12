import numpy as np

transition = np.array([[0.6, 0.4],
                       [0.4, 0.6]])

today = np.array([0.2, 0.8])

tomorrow = transition @ today

# 365 days later
day = today
for _ in range(365):
  day = transition @ day

print(day)

# OUTPUT:
# array([0.5, 0.5])

