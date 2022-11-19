start = "Hello!"
end = "How are you?"
full = start + end
print(full)

full = start + " " + end
print(full)

start = "I am "
age = 37
end = " years old."
full = start + str(age) + end
print(full)
print(start, age, end)
print(start, age, end, sep="", end="# ")
msg = ""
msg += start
msg += str(age)
msg += end
print(msg)

msg = """Hello i'm
in 
    multi
lines"""
print(msg)