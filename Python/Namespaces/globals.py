import random
g = globals().copy()
for k in g:
    print(f"{k}: {g[k]}")
print("\n")
first_name = "Jaya"
last_name = "Bodegard" 
 
def print_variables():
  random_number = random.randint(0,9)
  print(first_name)
  print(last_name)
  print(random_number)

g = globals().copy()
for k in g:
    print(f"{k}: {g[k]}")
