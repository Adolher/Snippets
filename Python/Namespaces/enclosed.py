global_variable = 'global'
 
def outer_function():
  outer_value = "outer"
  def inner_function():
    inner_value = "inner"
    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    print(locals())
  inner_function()
outer_function()