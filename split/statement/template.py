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

# Write this function
def get_s(x, y):
  return 47

x, y = load_data(sys.argv[1])
print get_s(x, y)
