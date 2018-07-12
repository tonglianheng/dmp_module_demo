import numpy as np

today = np.array([1,0])

transition = np.array(
  [[0.6, 0.4],
   [0.4, 0.6]]
)

n_events = 10
n_rain_days = 0
for _ in range(n_events):
  for _ in range(365):
    today = transition @ today  
    p_sun, p_rain = today 
    if np.random.random() < p_sun:
      today = np.array([1,0])
    else:
      today = np.array([0,1])
      n_rain_days += 1

print(
 'days of rain:', 
  n_rain_days / n_events
)

