class CustomerCounter:
  def __iter__(self):
    self.count = 0
    return self
  def __next__(self):
    self.count += 1
    if self.count > 100:
      raise StopIteration
    else:
      return self.count

customer_counter = CustomerCounter()

for c in customer_counter:
  print(c)