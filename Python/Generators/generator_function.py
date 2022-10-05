def class_standing_generator():
  yield "Freshman"
  yield "Sophomore"
  yield "Junior"
  yield "Senior"

class_standings = class_standing_generator()

for cs in class_standings:
  print(cs)

print(class_standings)