try:
    print("In try Block 1")
except:
    print("In except Block 1")
print()
try:
    print("In try Block 2")
    raise Exception
except:
    print("In except Block 2")
print()     # ----------------------------------- #
try:
    print("In try Block with multiple exceptions")
except (TypeError, NameError):
    print("In except Block with multiple exceptions")
print()
try:
    print("In try Block with multiple exceptions")
    raise NameError
except (TypeError, NameError):
    print("In except Block with multiple exceptions")
print()     # ----------------------------------- #
try:
    print("In try Block with else")
except:
    print("In except Block with else")
else:
    print("In else Block")
print()
try:
    print("In try Block with else")
    raise Exception
except:
    print("In except Block with else")
else:
    print("In else Block")
print()     # ----------------------------------- #
try:
    print("In try Block with finaly")
except:
    print("In except Block with finaly")
finally:
    print("In finaly Block")
print()
try:
    print("In try Block with finaly")
    raise Exception
except:
    print("In except Block with finaly")
finally:
    print("In finaly Block")
print()     # ----------------------------------- #
try:
    print("In try Block with else and finaly")
except:
    print("In except Block with else and finaly")
else:
    print("In else Block")
finally:
    print("In finaly Block")
print()
try:
    print("In try Block with else and finaly")
    raise Exception
except:
    print("In except Block with else and finaly")
else:
    print("In else Block")
finally:
    print("In finaly Block")
print()     # ----------------------------------- #
try:
    print("In try Block")
finally:
    print("In finally Block")
print()
try:
    print("In try Block")
    raise Exception
finally:
    print("In finally Block")