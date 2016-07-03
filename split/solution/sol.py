import sys

def load_data(fn):
  f = open(fn)
  n = int(f.next())
  x = []
  y = []
  for l in f:
    a, b = map(int, l.strip().split())
    x.append(a)
    y.append(b)

  return x, y


def get_s(x, y):

  # It is sufficient to minimize sum(a-)^2/|A-|+sum(a+)^2/|A+|.

  # Sort data by x
  data = list(zip(x, y))
  data.sort()

  # Do prefix sums y.
  sum_y = [0] 
  for _, y in data:
    sum_y.append(sum_y[-1]+y)

  # Solve the task using prefix sums
  n = len(data)
  maxi = -1
  for i in range(1, n):
    if data[i-1][0] == data[i][0]:
      continue
    value = sum_y[i]**2/float(i)+(sum_y[n]-sum_y[i])**2/float(n-i)
    if value > maxi:
      maxi = value
      result = (data[i][0] + data[i-1][0]) / 2
  return result

x, y = load_data(sys.argv[1])
print get_s(x, y)
