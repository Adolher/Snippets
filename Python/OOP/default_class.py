class Default:
    class_variable = 1
    def __init__(self):
        self.instance_variable = Default.class_variable
        Default.class_variable += 1

    def instance_method(self):
        print(f"My instance variable is {self.instance_variable}")

default_obj_1 = Default()
default_obj_1.instance_method()
default_obj_2 = Default()
default_obj_2.instance_method()

print("\nThe Object 'default_obj has the following methods and attributes:\n", dir(default_obj_1))
default_obj_1.new_instance_variable = "new"
print(f"\nAdded a new instance variable to 'default_obj' with 'default_obj.new_instance_variable = \"new\" '\n", dir(default_obj_1))
