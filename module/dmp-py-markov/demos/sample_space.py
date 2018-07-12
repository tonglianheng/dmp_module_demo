import numpy as np

today = np.array([1,0])

transition = np.array(
  [[0.6, 0.4],
   [0.4, 0.6]]
)

tomorrow = transition @ today
p_sun, p_rain = tomorrow 

test = np.random.random()
if test < p_sun:              # sun
  tomorrow = np.array([1,0])
else:                         # rain
  tomorrow = np.array([0,1])
