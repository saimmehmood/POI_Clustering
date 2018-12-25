

def foo(world) :
    return "Hello {} ".format(world)

def bar(): 
    return "Hello World"

print(foo("Earth"))

def function_debug(func):
    print("About to call function")
    result = func()
    print("Called function")
    return result

print(function_debug(bar))