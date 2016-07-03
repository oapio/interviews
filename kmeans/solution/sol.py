import sys
import numpy as np

def init(data, k):
  choices = np.random.choice(data.shape[0], k)
  return data[choices]

def dist(a, b):
  return np.sum((a - b)**2)

def kmeans(data, k):
  data = np.array(data)
  centers = init(data, k)

  last_assignment = None
  while True:
    dist_m = np.array([[dist(c, x) for c in centers] for x in data ])
    assignment = np.argmin(dist_m, axis=1)
    if last_assignment is not None and (assignment == last_assignment).all():
        break
    
    centers = np.zeros((k, 2))
    centers_count = np.zeros(k)
    for x, a in zip(data, assignment):
      centers[a] += x
      centers_count[a] += 1
    centers = (centers.T / centers_count).T
    last_assignment = assignment

  return centers

def load_data(fn):
  f = open(fn)
  data = []
  for l in f:
    row = map(float, l.strip().split())
    data.append(row)
  return data

data = load_data(sys.argv[1])
centers = kmeans(data, 4)

print centers
