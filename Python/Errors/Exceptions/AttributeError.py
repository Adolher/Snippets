class A_Class:
  pass
 
an_object = A_Class()
 
try:
  an_object.an_attribute
except AttributeError as e:
  print(e)